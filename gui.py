import tkFileDialog, os
from Tkinter import *
from svm_handler import *
from svm_handler import SVMHandler
from calc_error_pct import *
#import ttk
#from mail import sendemail
#import threading

class SVMGui(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
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
            self.svm_handler = SVMHandler()
            tkMessageBox.showinfo("Hello Python", data_path.get("1.0", 'end-1c') + "adult.test")
            self.svm_handler.initialize_training(data_path.get("1.0",'end-1c')+ "adult.test")
            tkMessageBox.showinfo("Hello Python", "End train")

        def activate_test():
            tkMessageBox.showinfo("Hello Python", data_path.get("1.0", 'end-1c') + "adult.data")
            y, predicted_y = self.svm_handler.init_data(data_path.get("1.0",'end-1c')+ "adult.data")
            err_precent = calculate_error_percentage(y, predicted_y)
            tkMessageBox.showinfo("Error precent", err_precent)

        def send_mail():
            tkMessageBox.showinfo("Hello Python", "Send email")

        data_path_button = Button(self.root, text="Open", command=data_path_callback)
        data_path_button.grid(row=0, column=2)

        training_button = Button(self.root, text="Train", command=activate_train)
        training_button.grid(row=1, column=0)

        active_button = Button(self.root, text="Active test!", command=activate_test)
        active_button.grid(row=1, column=1)

        send_email_button = Button(self.root, text="Send results", command=send_mail)
        send_email_button.grid(row=2, column=0)

def run_gui():
    root = Tk()
    root.title("SVM GUI")
    gui = SVMGui(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()