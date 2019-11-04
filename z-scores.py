######### File 2 - data_analysis.py ##########
## Find most arrests, age percentiles, z-scores
import collections
from collections import Counter
import statistics
import numpy as np
import math
import functools

f = open( 'crimes_2018.txt', 'r' )
crimes_18 = []
dates = []
areas = []
headers = ["Report ID", "Arrest Date", "Time", "Area ID", 
"Area Name", "Reporting District", "Age", "Sex Code", 
"Descent Code", "Charge Group Code", "Charge Group Description", 
"Arrest Type Code", "Charge", "Charge Description", "Address", 
"Cross Street", "Location"]
# We want everything under this header
header_index = headers.index('Area Name')

for line in f:
	crimes_18.append(line)

####### Functions ########

# Function to find the most arrests for each crime
def most_arrests(arrays, header_index):
	for line in crimes_18:
	    cells = line.strip().split( "," ) ## Split into cells
	    area_name = cells[header_index] ## We're looking for the index 
	    								## that contains area names
	    areas.append(area_name)
	Data = collections.Counter(areas)
	area_dict = {}
	cnt = Counter(Data)
	for key, value in cnt.items():
	    area_dict[key] = value

	#print(area_dict)
	most_common = max(area_dict, key=area_dict.get)  
	print(f"""The most arrestees were booked in {most_common}. 
There were {area_dict[most_common]} arrests.""")

# Produce a list of ages for each crime
def age_quantiles(interesting, array, keyword):
	arrestee_age = []
	crimes_of_interest = []
	for crime in interesting:
		for line in array:
			cells = line.strip().split( "," ) ## Split into cells
			if cells[crime_type] == crime: ## Check it's a crime we
				crimes_of_interest.append(cells)      ## care about
				arrestee_age.append(int(cells[headers.index(keyword)]))
	return(arrestee_age)

######## Most Arrests ##########
most_arrests(crimes_18, header_index) ## From the list of crimes in 2018

## Selective arrests
crime_type = headers.index("Charge Group Description")
#print(crime_type)
interesting_crimes =["Vehicle Theft", "Robbery", "Burglary", 
"Receive Stolen Property"]

####### Age quantiles question ##########
## call the function to get all the relevant ages!
ages = age_quantiles(interesting_crimes, crimes_18, 'Age') 

a = np.percentile(ages, 95) #calculate 95th percentile
print("The 95% quantile for age of arrestees in 2018 is" +"%10f" %a)
mean = sum(ages)/len(ages)

####### Z-Scores Question ########

## clear empty data, i.e. get ring of the things we're not interested in
crimes = []
crime = []
crime_desc = headers.index("Charge Group Description")
for line in crimes_18:
	cells = line.strip().split( "," ) ## Split into cells
	#description = cells[crime_desc]
	if cells[crime_desc] is not "":	
		if  (cells[crime_desc].strip() == "Pre-Delinquency" or 
			cells[crime_desc].strip() == "Non-Criminal Detention"):
			continue
		else:
			crimes.append(cells)
			crime.append(cells[crime_desc])
## Get the crime types (for grouping), and turn it into a list
crime_types = set(crime)
list_crime_types = list(crime_types)

aver_ages = [] ## to store average age for each crime
index_age=(headers.index('Age')) # gives the index of 'Age' in headers
index_desc=(headers.index('Charge Group Description')) 

"""
 Work through each type of crime. When we find it in "line" (the file line), add the age of the person to the total age for that crime. 
 Divide the total by the running counter, n, to get the average age for that crime.
 Repeat for all crimes.
 """
for c in list_crime_types:
	#print(c)
	n=0
	total_age = 0
	for line in crimes:
		if line[index_desc] == c: ## If we match the crime we're referring to
			#age.append(int(line[index_age])) ## append to age
			n= n+1 ## calaculating size of array
			total_age += int(line[index_age])
	aver_ages.append(total_age/n)

## Calculate z-scores
stdev_ages = statistics.stdev(aver_ages) ## Calculating mean and standard 
mean_ages = statistics.mean(aver_ages)	 ## deviations
z_scores = []
for aver in aver_ages:
	z_score = abs((aver - mean_ages)/stdev_ages) ## formula for z score, absoluted
	z_scores.append(z_score)
print(f'The maximum z-score is {max(z_scores):.9f}!')


