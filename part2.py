## NB I would have liked to write a function to get these, but i ran out
## of time


points = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000, 3621391]
T_Value = [2.06260, 2.11530, 2.27152, 1.38720, 2.49376, 4.249376, 6.00618]
P_Value = [0.05391, 0.04100, 0.02530, 0.16694,0.01304, 0.00003, 0.00000]
Pearson_Corr = [0.533, 0.424, 0.904, 0.343, 0.458, 0.482,0.466,0.446,0.663,0.772,0.796,0.807,0.803,0.724,0.359]
print(points)

## Find pearson correlation vs number of points
plt.scatter(points, Pearson_Corr, s=10, c='m', marker='.')
plt.xscale('log')
plt.xlabel('Number of data points') 
plt.ylabel('Pearson Correlation Coefficient') 
plt.title('Number of data points vs Pearson Correlation') 
plt.show()

"""
The correlation doesn't appear to change for the number of data points
investigated: that is to say, we don't improve correlation by taking
more data. This really serves to support the apparent outcome: that
number of mentions does not increase with number of likes.
"""

## Find T-Value vs number of points
plt.scatter(points[0:len(T_Value)], T_Value, s=10, c='c', marker='o')
plt.xscale('log')
plt.xlabel('Number of data points') 
plt.ylabel('T-Value') 
plt.title('Number of data points vs T-Value') 
plt.show()

"""
On the whole, T-value shows that conclusions about the significance 
numbers of likes for numbers of mentions become more valid with
more data points. This is unsurprising.

"""

plt.scatter(points[0:len(P_Value)], P_Value, s=10, c='g', marker='o')
plt.xscale('log')
plt.xlabel('Number of data points') 
plt.ylabel('T-Value') 
plt.title('Number of data points vs P-Value') 
plt.show()


## I would like to further investigate this: if talking about doesn't relate to
## likes, this may relate to the fact that people talk negatively. I would be
## useful to get data on the content of the "talking about" posts, scraping this
## data and identifying useful "positive" keywords. In this way, we can determine
## whether the hypothesis that more people talk negatively is true and therefore
## consider how companies may structure social media posts so that people will 
## "talk about" those posts or events, thus increasing the number of people who
## like the company to post.

## As we expect, P-Value is less for a much larger dataset. Yet correlation is not 
## more stable because of the clusters seen on the graph. More insight into the 
## formation of these "clusters" would allow companies to target a cluster - i.e.
## receive a proportional amount of mentions to likes.
## This would indicate a more active customer base, rather than a passive base who
## will like the page but are not actively loyal.