import tensorflow as tf
import csv
label = 0

def BigBang():

	thefirstweeb = Learnmachine()
	thefirstweeb.put_data()
	



class Learnmachine:
	def __init__(self):
		self.dataholder = {}
		self.intholder = {}
		self.stringholder = {}
		self.keys = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
		# should i do this? Can i define dictionaries without lists?
		self.garretsuglyface = ['garret', 'is', 'an', 'ugly', 'individual', 'i', 'hate', 'him', 'so', 'much']
		#input_training_data()

	#def input_training_data(TRAIN_URL):
	#	tf.data.Dataset.from_tensors(TRAIN_URL)
	def put_data(dataholder, stringholder, intholder):
		global label

		path = "/home/maya/youreprobablyuglierthanyouthink/PRECIP_HLY_sample_csv.csv"
		with open(path) as csv_file:
			csvdata = csv.reader(csv_file, delimiter = ',')
			label = 0
			
			#put the csvdata into a dictionary because python is stupid and you can't assign to literals even if it's an object
			for row in csvdata:
				row = []
				
				#Put the list type 'row' into the dictionary 'stringholder' as a string
				stringholder = ''.join(row) 
				
				#Check the current string for isalpha
				itsastring = stringholder.isalpha()
				#value of the csv data as a Tensor, sorted by string vs. num
				if itsastring:
					tensorstring = tf.Variable(row, tf.string)			
				else:
					tensorint = tf.Variable(row, tf.int64)
				#count up for the labels
				label = label + 1

				#tensor for the labels
				labelobject = tf.Variable(label, tf.float64)

				stringholder = tensorstring
				intholder = tensorint

				#dictionary with the keys as feature names and the values as Tensors
				dataholder[keys] = labelobject

				stringholder.update(intholder,dataholder)


		return dataholder, labelobject


BigBang()
#I know that this could create a local instantiation of datamover and I don't want that, but I tried changing the datamover in putdata to succ and still nothing so idk
