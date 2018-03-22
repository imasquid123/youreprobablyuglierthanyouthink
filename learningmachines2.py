import tensorflow as tf
import csv


def BigBang():

	thefirstweeb = Learnmachine()
	thefirstweeb.put_data()
	



class Learnmachine:
	def __init__(self):
		self.dataholder = {}

		#input_training_data()

	#def input_training_data(TRAIN_URL):
	#	tf.data.Dataset.from_tensors(TRAIN_URL)
	def put_data(dataholder):

		path = "/home/maya/machinelearning2/PRECIP_HLY_sample_csv.csv"

		with open(path) as csv_file:
			reader = csv.reader(csv_file, delimiter = ',')

			for row in reader:

				#first, make data into tensors
				#Does row reference the individual data point?
				dataobject = tf.Variable(row, tf.float64)
				#next, move each tensor to a dictionary				
				#for now, names of the feature are just ints but i know that's gross				
				label = label + 1
				labelobject = tf.Variable(label, string)
				dataholder[label] = dataobject


		return dataholder, labelobject


BigBang()
#I know that this could create a local instantiation of datamover and I don't want that, but I tried changing the datamover in putdata to succ and still nothing so idk
