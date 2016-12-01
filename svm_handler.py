from sklearn import svm
from parse_data import parse_data
from calc_error_pct import *
import tkMessageBox


class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """
    def __init__(self):
            print "hello"


    def initializeTraining(self, filePath):
        X, Y = parse_data(filePath)
        print Y


