# Inserts names from csv file

name_file = "redeliste.csv"

input_file  = "plenum/anfang.tex"
output_file = "plenum/anfang_neu.tex"

with open(input_file, "r") as f1:
	text_in = f1.read()

with open(name_file, "r") as f2:
	redeliste = f2.readlines()
	redeliste = [[y[4], y[1], y[2], y[3]] for y in [x.split(";") for x in redeliste]]

for person in redeliste:
	text_in = text_in.replace("-"+person[0]+"-", person[1] + " " + person[2] + " - " + person[3] + ": ")

with open(output_file, "w") as f3:
	f3.write(text_in)