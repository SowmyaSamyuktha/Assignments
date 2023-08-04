#!/usr/bin/env python
# coding: utf-8

# In[1]:


#DESCRIPTIVE STATS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# In[ ]:





# In[ ]:


#Descriptive stats: 
    Question 1)


# In[2]:


x = pd.Series([24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39.42,26.71,35.00])


# In[22]:


y=['Allied Signal','Bankers Trust','General Mills','ITT Industries','J.P,Morgan & Co.','Lehman Brothers','Marriott','MCI','Merrill Lynch','Microsoft','Morgan Stanley','Sun Microsystems','Travelors','US Airways','Warner-Lambert']


# In[23]:


#Pie plot


# In[25]:


plt.pie(x, labels=y,autopct='%1.0f%%')
plt.show()


# In[17]:


#To find outliers using Boxplot


# In[18]:


sns.boxplot(x)


# In[19]:


x.mean()


# In[20]:


x.var()


# In[21]:


x.std()


# In[ ]:





# In[ ]:


#Set-2/Normal distribution


# In[2]:


#question 5


# In[4]:


#Mean profits from 2different companies is Mean1 + Mean2
Mean = 5 +7
print('Mean Profit is Rs', Mean*45, 'Million')


# In[4]:


#Variance of profit from 2 diff division 
SD = np.sqrt((9)+(16))
print('Standard Deviation is RS', SD*45, 'Million')


# In[10]:


# A)
print('Range is Rs' , (stats.norm.interval(0.95,540,225)), 'in Millions')


# In[11]:


# B)
#To compute 5th percentile , we use the formulae, X = µ + Z*sigma

X = 540 + (-1.645)*225
print('5th percentile of profit (in Million Rupees) is' , np.round(X, ) )


# In[12]:


#C)
#Probability of Division 1 making a loss P(X<0)
stats.norm.cdf(0,5,3)


# In[13]:


#Probability of Division 2 making a loss P(X<0)
stats.norm.cdf(0,7,4)


# In[ ]:





# In[2]:


# SET 3 Assignment
#Confidence interval
# Question 5


# In[1]:


#Apply one sample one tail Z-test


# In[ ]:





# In[19]:


z_scores = (0.046-0.05)/(np.sqrt(0.05*(1-0.05))/2000)


# In[20]:


z_scores


# In[23]:


#Find probability assuming null hypothesis ,so as to compare with Type 1 error


# In[ ]:





# In[26]:


p_value = 1 - stats.norm.cdf(abs(z_scores))


# In[27]:


p_value


# In[ ]:





# In[ ]:





# In[ ]:


#Set 4, question 3


# In[ ]:


#n = 100, popn mean = 50, SD = 40. As no of samples is more than 30, we consider it normal distribution


# In[ ]:


# For no investigation P(45<X<55)
# For investigation  1 - P(45<X<55)


# In[2]:


# Find z-score at x=45, z = (s_mean - P_mean)/(p_SD/sqrt(n))
z = (45-50)/(40/100**0.5)
z


# In[3]:


# Find z-score at x=55, z = (s_mean - P_mean)/(p_SD/sqrt(n))
z = (55-50)/(40/100**0.5)
z


# In[4]:


#For no investigation P(45<X<55) using z_scores =P(X<50)-P(X<45)
stats.norm.cdf(1.25)-stats.norm.cdf(-1.25)


# In[5]:


stats.norm.interval(0.7887, loc = 50, scale= 40/(100**0.5))


# In[6]:


#For Investigation 1 -P(45<X<55)
1-0.7887


# In[8]:


#Answer is D. 21.1%


# In[ ]:




