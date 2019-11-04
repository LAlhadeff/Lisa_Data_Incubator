# importing the required module
from numpy.random import randn
from numpy.random import seed
from numpy import cov 
import matplotlib.pyplot as plt 

f = open( 'likes.txt', 'r' )
f2 = open( 'talked_about.txt', 'r' )

likes = []
talked_about = []

for line in f:
	likes.append(int(line))
for line2 in f2:
	talked_about.append(int(line2))

# importing the required module 
import matplotlib.pyplot as plt 

size = len(likes)
#size = 10
# # x axis values 
x = likes[0:size] 
#x = likes[0:3000]
y = talked_about[0:size]
# # corresponding y axis values 
#y = talked_about[0:3000]

def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)
    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2
    b = numer / denum   
    a = ybar - b * xbar
    print('best fit line:\ny = {:.4f} + {:.4}x'.format(a, b))
    return(a, b)

# Best fit line
(a, b) = best_fit(x, y)

# plot points and fit line
import matplotlib.pyplot as plt

plt.scatter(x, y, s=10, c='b', marker='.')
yfit = [a + b * xi for xi in x]
plt.plot(x, yfit, c = 'r')
# naming the x axis 
plt.xlabel('Likes') 
# naming the y axis 
plt.ylabel('Talked About') 
  
# giving a title to my graph 
plt.title('Correlation between number of likes and people talking about') 


covariance = cov(x, y)
print("\nCovariance data:")
print(covariance)
# function to show the plot 
plt.show() 

# Consider correlation coefficients: Pearson and Spearmans
from scipy.stats import pearsonr
from scipy.stats import spearmanr

# calculate Pearson's correlation
corr, _ = pearsonr(x, y)
print('\nPearsons correlation: %.3f' % corr)

# calculate spearman's correlation
corr, _ = spearmanr(x, y)
print('Spearmans correlation: %.3f' % corr)

"""
We see that the pearson's correlation is 0.471: that is to say, 
that there is indeed a positive correlation between likes and
""talking about".
"""

## Import the packages
import numpy as np
from scipy import stats

#Sample Size
N = len(likes)
a = x
b = y

## Investigating t and P values
t, p = stats.ttest_ind(x,y)
print("\nt-value is:  %.5f" % t)
print("p-value is:  %.10f" % p)

"""
What is interesting from the plot, is that the data appears different 
for smaller values. For example, if we reconsider the case for the first 
100 points.

So is there a relationship between number of points considered and P-value?
i.e. is the relationship more significant at higher values?
"""
## NB I would have liked to write a function to get these, but i ran out
## of time
