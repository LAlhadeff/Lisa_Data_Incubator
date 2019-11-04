######### File 1 - data_analysis.py ##########
## Produce a text file containing only crimes from 2018
import re
f = open( 'Arrest_Data.csv', 'r' )
crimes_18 = []
for line in f:
    cells = line.split( "," ) ## Split into cells
    regex = re.compile('../../2018') ## We're looking for the 
    								 ## date format, and it 
    								 ## must end in 2018
    matches = [string for string in cells if re.match(regex, string)]
    if matches != []: ## if it matches the date format, append it
    	crimes_18.append(line.strip())
f.close() # Data stored locally so close file
#print(dates)
#print(crimes_18)
print(f'There were: ', len(crimes_18), " crimes in 2018")
## Write 2018 dates to a new file to save on analysis time
with open("crimes_2018.txt", 'w') as f:
	for item in crimes_18:
		f.write("%s\n" % item)