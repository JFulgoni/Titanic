import csv
import numpy as np
__author__ = 'johnfulgoni'

def get_train():
    filename = "Data/train.csv"
    csv_file_object = csv.reader(open(filename, 'rb'))
    header = csv_file_object.next()
    data = []

    for row in csv_file_object:
        data.append(row[0:])
    data = np.array(data)

    return header, data