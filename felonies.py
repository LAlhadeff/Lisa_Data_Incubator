######### File 3 - felonies.py ##########
## Import Entire dataset. excluding 2019 and offenses 
## considered misdemeanors.
## Write to a text file, trends.txt

import re
f = open( 'Arrest_Data.csv', 'r' )
crimes_felonies = []
dates = []
for line in f:
    cells = line.split( "," ) ## Split into cells
    regex = re.compile('../../2019') ## We're looking for the date format, 
								 ## and it ends in 2018
    matches = [string for string in cells if re.match(regex, string)]
    if matches == []: ## if it matches the date format, append it
    	if "Drunkeness" in line:
    		continue
    	elif "Moving Traffic Violations" in line:
    		continue 
    	elif "Prostitution/Allied" in line:
    		continue
    	elif "Disorderly Conduct" in line:
    		continue
    	elif  "Gambling" in line:
    		continue
    	elif  "Disturbing the Peace" in line:
    		continue
    	elif  "Driving Under Influence" in line:
    		continue
    	else:
    		crimes_felonies.append(line.strip())
f.close() # Data stored locally so close file
#print(dates)
#print(crimes_18)
print(f'There were: ', len(crimes_felonies), " crimes in 2010-2018")
## Write 2018 dates to a new file to save on analysis time
with open("trends.txt", 'w') as f:
	for item in crimes_felonies:
		f.write("%s\n" % item)