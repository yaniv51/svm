import tkFileDialog, os, threading
from Tkinter import *
import tkMessageBox
from svm_handler import SVMHandler
from mail import send_email


class SVMGui:
    def __init__(self):
        self.root = Tk()
        self.err_percent = -1
        self.is_running = False
        self.already_tested = False
        self.root.title("SVM GUI")
        self.init_widgets()

    def init_widgets(self):
        path_lable_string = StringVar()
        path_lable = Label(self.root, textvariable=path_lable_string, relief=RAISED)
        path_lable_string.set("Data Path: ")

        data_path = Text(self.root, height=1, width=70)
        data_path.insert(END, os.getcwd() + "/data/")
        data_path.configure(state='disabled')
        path_lable.grid(row=0, column=0)
        data_path.grid(row=0, column=1)

        def data_path_callback():
            dir_name = tkFileDialog.askdirectory()
            if len(dir_name) > 0:
                data_path.configure(state='normal')
                data_path.delete("1.0", END)
                data_path.insert(END, dir_name)
                data_path.configure(state='disabled')

        def activate_train():
            if self.is_running:
                self.show_error("In progress. Please wait")
                return
            self.svm_handler = SVMHandler()
            path = data_path.get("1.0", 'end-1c')
            if not path.endswith('/'):
                path+="/"
            path += "adult.test"
            t = threading.Thread(target=self.run_test, args=(path, True,))
            t.start()

        def activate_test():
            if self.is_running:
                self.show_error("In progress. Please wait")
                return
            if not self.already_tested:
                self.show_error("You have to train machine first!")
                return
            path = data_path.get("1.0", 'end-1c')
            if not path.endswith('/'):
                path += "/"
            path += "adult.data"
            t = threading.Thread(target=self.run_test, args=(path, False,))
            t.start()

        def send_mail():
            t = threading.Thread(target=self.send_message, args=(self.generate_message(self.err_percent),))
            t.start()

        data_path_button = Button(self.root, text="Open", command=data_path_callback)
        data_path_button.grid(row=0, column=2)

        training_button = Button(self.root, text="Train", command=activate_train)
        training_button.grid(row=1, column=0)

        active_button = Button(self.root, text="Active test!", command=activate_test)
        active_button.grid(row=1, column=1)

        send_email_button = Button(self.root, text="Send results", command=send_mail)
        send_email_button.grid(row=2, column=0)

    def show_error(self, error):
        tkMessageBox.showinfo("Error", error)

    def run(self):
        self.center_window()
        self.root.mainloop()

    def generate_message(self, value):
        if value < 0:
            message = "Testing send Email by Yaniv Israel program"
        else:
            message = "Error percent: " + "%.3f" % value + " by SVM machine learning"
        return message

    def send_message(self, text):
        result = send_email(text)
        tkMessageBox.showinfo("EMail information", result)

    def center_window(self, width=680, height=100):
        # get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def run_test(self, path, train):
        self.is_running = True
        tkMessageBox.showinfo("Wait", "In progress...")
        try:
            if train:
                self.svm_handler.run_training(path)
                self.already_tested = True
            else:
                self.svm_handler.run_test(path)
                self.err_percent = self.svm_handler.get_error_Percent()
                self.svm_handler.print_results()

                tkMessageBox.showinfo("Error Percent", self.err_percent)
        except IOError:
            self.show_error("Could not open file: "+path)
        self.is_running = False
        tkMessageBox.showinfo("Wait", "Finished")


def run_gui():
    gui = SVMGui()
    gui.run()

if __name__ == "__main__":
    run_gui()