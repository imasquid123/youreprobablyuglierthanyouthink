import tensorflow as tf
import csv
TRAIN_URL = "PRECIP_HLY_sample_csv.csv"

def __init__(self):
	datamover = PyDict_SetItem()
	dict[dataholder] = []
	input_training_data()
	put_data()

def input_training_data(TRAIN_URL):
	tf.data.Dataset.from_tensors(TRAIN_URL)

def put_data(datamover, TRAIN_URL):

	with open("PRECIP_HLY_sample_csv.csv") as csv_file:
		reader = csv.reader("PRECIP_HLY_sample_csv.csv", delimiter = ',')

	for row in reader ():

		#first, make data into tensors
		#Does row reference the individual data point?

		dataobject = tf.Variable(row, tf.float64)
		
		#next, move each tensor to a dictionary
		
		datamover(dataholder, label, dataobject)
		#for now, names of the feature are just ints but i know that's gross
		
		label = x+1

		labelobject = tf.Variable(label, string)
	return dataholder, labelobject