import csv 

exemplefile = open('frutas.csv')
exempleReader = csv.reader(exemplefile)
exempleData = list(exempleReader)
exempleData 

print(exempleData[0][0])
print(exempleData[0][1])
print(exempleData[0][2])
print(exempleData[1][1])
print(exempleData[6][1])