from sklearn import svm
from sklearn import preprocessing
from parse_data import parse_data
from calc_error_pct import *


class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """
    def __init__(self):
        self.clf = svm.SVC(kernel='linear', C=1.0)

    def run_training(self, file_path):
        x, y = parse_data(file_path)
        #normelize X values for better preformnce
        x_scaled = preprocessing.scale(x)
        self.clf.fit(x_scaled, y)

    def run_test(self, file_path):
        x, y = parse_data(file_path)
        predict = self.clf.predict(preprocessing.scale(x))
        self.y = y
        self.predicted_y = predict

    def get_error_Percent(self):
        return calculate_error_percentage(self.y, self.predicted_y)

    def print_results(self):
        false_pos = 0
        true_neg = 0
        accur = 0

        for i in range(len(self.y)):
            if self.y[i] == self.predicted_y[i]:
                accur = accur+1
            if self.y[i] == 1 and self.predicted_y[i] == 0:
                true_neg = true_neg +1
            if self.y[i] == 0 and self.predicted_y[i] == 1:
                false_pos = false_pos+1

        print "false pos: ", false_pos, ". true neg: ", true_neg, ". accure: ", accur

