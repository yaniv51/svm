from sklearn import svm
from sklearn import preprocessing
from parse_data import parse_data
from calc_error_pct import *
import tkMessageBox


class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """
    def __init__(self):
            self.clf = svm.SVC(kernel='linear', C=1.0)

    def initialize_training(self, file_path):
        x, y = parse_data(file_path)
        x_scaled = preprocessing.scale(x)
        self.clf.fit(x_scaled, y)

    def init_data(self, file_path):
        false_pos = 0
        true_neg = 0
        accur = 0
        x,y = parse_data(file_path)
        predict = self.clf.predict(preprocessing.scale(x))
        for i in range(len(y)):
            if y[i] == predict[i]:
                accur = accur+1
            if y[i] == 1 and predict[i] == 0:
                true_neg = true_neg +1
            if y[i] == 0 and predict[i] == 1:
                false_pos = false_pos+1

        self.y = y
        self.predicted_y = predict
        print "false pos: ", false_pos, ". true neg: ", true_neg, ". accure: ", accur
        return y, predict

    def get_error_Percent(self):
        return calculate_error_percentage(self.y, self.predicted_y)

