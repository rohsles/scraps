import os
import sys
import pickle
import pandas
pickle_file = open('data/07102.pickle', 'r')

b = pickle.load(pickle_file)
df = pandas.DataFrame(b)

print df
