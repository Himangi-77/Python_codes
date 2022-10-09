'''
	Look at the data given below. Plot the data, find the outliers and find out  μ,σ,σ^2

Name of company	Measure X
Allied Signal	24.23%
Bankers Trust	25.53%
General Mills	25.41%
ITT Industries	24.14%
J.P.Morgan & Co.	29.62%
Lehman Brothers	28.25%
Marriott	25.81%
MCI	24.39%
Merrill Lynch	40.26%
Microsoft	32.95%
Morgan Stanley	91.36%
Sun Microsystems	25.99%
Travelers	39.42%
US Airways	26.71%
Warner-Lambert	35.00%

'''

#BOXPLOT
import numpy as np
arr = np.array([24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39.42,26.71,35.00])
import matplotlib.pyplot as plt
%matplotlib inline
plt.boxplot(arr, vert=False)

#There is one outlier namely 91.36%

mean = np.mean(arr)
s = np.std(arr)
variance = np.var(arr)
print("Mean = ", mean, " Standard Deviation = ", s, " Variance = ", variance)
