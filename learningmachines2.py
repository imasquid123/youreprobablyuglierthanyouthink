import tensorflow as tf
import csv
label = 0

def BigBang():

	thefirstweeb = Learnmachine()
	thefirstweeb.put_data()
	



class Learnmachine:
	def __init__(self):
		self.dataholder = {}
		self.keys = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
		#input_training_data()

	#def input_training_data(TRAIN_URL):
	#jciownfsoifdpejrytlhiewbqrpivdpgteibtumrlnlegdfu
	#	tf.data.Dataset.from_tensors(TRAIN_URL)
	def put_data(dataholder):
		global label

		path = "/home/maya/machinelearning2/PRECIP_HLY_sample_csv.csv"
		with open(path) as csv_file:
			csvdata = csv.reader(csv_file, delimiter = ',')
			label = 0
			for row in csvdata:
				#value of the csv data as a Tensor
				csvdataobject = tf.Variable(csvdata, tf.string)			
				
				#count up for the labels
				label = label + 1

				#tensor for the labels
				labelobject = tf.Variable(label, tf.float64)

				#giving the dictionary 'dataholder' access to the Tensors containing the csv data
				dataholder.__setitem__(self, keys, csvdataobject)

				#dictionary with the keys as feature names and the values as Tensors
				dataholder[keys] = labelobject


		return dataholder, labelobject


BigBang()
#I know that this could create a local instantiation of datamover and I don't want that, but I tried changing the datamover in putdata to succ and still nothing so idk
