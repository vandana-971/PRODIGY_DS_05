#!/usr/bin/env python
# coding: utf-8

# In[7]:


#importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')


# In[ ]:





# In[8]:


#load and read the file
df=pd.read_csv(r"C:\Users\KIIT\Downloads\rta\RTA Dataset.csv")
df.head()


# In[9]:


df.shape


# In[8]:


df.info


# In[ ]:





# EXPLORATORY DATA ANALYSIS

# In[10]:


df['Accident_severity'].value_counts()


# In[11]:


#plotting the final class
sns.countplot(x = df['Accident_severity'])
plt.title('Distribution of Accident severity')


# DATA VISUALIZATION

# In[12]:


#plotting relationship between Number_of_casualties and Number_of_vehicles_involved
sns.scatterplot(x=df['Number_of_casualties'], y=df['Number_of_vehicles_involved'], hue=df['Accident_severity'])


# In[13]:


#joint Plot
sns.jointplot(x='Number_of_casualties',y='Number_of_vehicles_involved',data=df)


# In[14]:


#storing numerical column names to a variable
numerical=[i for i in df.columns if df[i].dtype!='O']
print('The numerica variables are',numerical)


# In[15]:


#distribution for numerical columns
plt.figure(figsize=(10,10))
plotnumber = 1
for i in numerical:
    if plotnumber <= df.shape[1]:
        ax1 = plt.subplot(2,2,plotnumber)
        plt.hist(df[i],color='red')
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.title('frequency of '+i, fontsize=10)
    plotnumber +=1


# In[16]:


categorical=[i for i in df.columns if df[i].dtype=='O']
print('The categorical variables are',categorical)


# In[ ]:


#count plot for categorical values
plt.figure(figsize=(10,200))
plotnumber = 1

for col in categorical:
    if plotnumber <= df.shape[1] and col!='Pedestrian_movement':
        ax1 = plt.subplot(28,1,plotnumber)
        sns.countplot(data=df, y=col, palette='muted')
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.title(col.title(), fontsize=14)
        plt.xlabel('')
        plt.ylabel('')
    plotnumber +=1


# In[25]:


df2=df.drop(['Owner_of_vehicle', 'Type_of_vehicle', 'Road_surface_conditions', 'Pedestrian_movement',
         'Casualty_severity','Educational_level','Day_of_week','Sex_of_driver','Road_allignment',
         'Sex_of_casualty'],axis=1)
df2.head()


# In[26]:


dummy=pd.get_dummies(df2[['Age_band_of_driver', 'Vehicle_driver_relation', 'Driving_experience',
                          'Area_accident_occured', 'Lanes_or_Medians', 'Types_of_Junction', 'Road_surface_type', 
                          'Light_conditions', 'Weather_conditions', 'Type_of_collision', 'Vehicle_movement', 
                          'Casualty_class', 'Age_band_of_casualty', 'Cause_of_accident']],drop_first=True)
dummy.head()


# In[29]:


df3=pd.concat([df2,dummy],axis=1)
df3.head()


# In[30]:


x=df3.drop(['Accident_severity'],axis=1)
x.shape


# In[31]:


y=df3.iloc[:,2]
y.head()


# In[32]:


#plotting count plot using seaborn
sns.countplot(x = y, palette='muted')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




