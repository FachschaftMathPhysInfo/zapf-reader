import string
import pprint
import numpy as np

# Inserts names from csv file

name_file = "vorlagen/redeliste.csv"

input_file  = "plenum/wahlen.tex"
output_file = "plenum/wahlen_neu.tex"

with open(input_file, "r") as f1:
	text_in = f1.read()

with open(name_file, "r") as f2:
	redeliste = f2.readlines()
	redeliste = [[y[0], y[1], y[2], y[3]] for y in [x.split(";") for x in redeliste]]

for person in redeliste:
	print(person[3])
	text_in = text_in.replace("-"+person[3]+"-", person[0] + " " + person[1] + " - " + person[2] + ": ")

with open(output_file, "w") as f3:
	f3.write(text_in)
