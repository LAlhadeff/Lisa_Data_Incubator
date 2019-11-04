######### File 4 - trends.py ##########
## Import felonies.py, and look for numger of felonies
## per year. Produce straight line coefficients for 
## y = mx + c and return for y = m*2019 + c
import collections
from collections import Counter
import statistics
from statistics import mean
import numpy as np
import math
import functools
## Open the file we cut down to include only 2010 -2019
f = open( 'trends.txt', 'r' )
dates = []
n=0
headers = ["Report ID", "Arrest Date", "Time", "Area ID", 
"Area Name", "Reporting District", "Age", "Sex Code", 
"Descent Code", "Charge Group Code", "Charge Group Description", 
"Arrest Type Code", "Charge", "Charge Description", "Address", 
"Cross Street", "Location"]
# We want everything under this header
header_index = headers.index('Arrest Date')

for line in f:
	cells = line.strip().split( "," ) ## Split into cells
	date = cells[header_index]
	dates.append(date[-4:]) ## We only want the year
burglaries = []
year = []

Dates = collections.Counter(dates)
date_dict = {}
cnt = Counter(Dates)
for key, value in cnt.items():
	date_dict[key] = value
	burglaries.append(value)
	year.append(key)

burglaries = burglaries[1:] ## cut off the "title imposed by 
							## counter"
burglaries2 = []

## Convert to correct type (i.e from string to integer).
for i in burglaries:
	burglaries2.append(int(i))
year = year[1:]
year2 = []
for j in year:
	#print(j)
	year2.append(int(j))

meanb = mean(burglaries2)
meany = mean(year2)

multi_wise = [a*b for a,b in zip(year2,burglaries2)] ## xs * ys
x_squared = [a*b for a,b in zip(year2,year2)] ## xs * xs
print(x_squared)

## Gradient:
# m = (((mean(xs)*mean(ys)) - mean(xs*ys)) / ((mean(xs)*mean(xs)) - 
# mean(xs*xs)))
m = (((meany*meanb) - mean(multi_wise)) / ((meany*meany) - mean(x_squared)))
## Y-interecpt:
# c = mean(ys) - m*mean(xs)
c = meanb - m*meany

predicted_2019 = m*2019 + c

print(f"The number of felonies predicted in 2019 is {predicted_2019:.0f}")
