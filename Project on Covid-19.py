#!/usr/bin/env python
# coding: utf-8

# # Project On Covid-19
# 
# ## Table of Contents
# <ul>
# <li><a href="intro">Introduction</a></li>
# <li><a href="#assessment">Data Assessment</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#eeda">Explanatory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# <li><a href="#limitations">Limitations</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# >This is a project on covid 19 cases among different continents. In this python project, we will be evaluating dataset from different region(continents) to determine the rate/effect of covid 19. We will be looking out for 5 most affected regions. we will also check the death rate by age group and how it varies across different continents. basically checking the total cases reported, total deaths, and if covid 19 has any effect on birth rate and its effect across different continents.
# >The dataset we will be using for this project is a .csv file and the data is from 2020 to 2022

# <a id='assessment'></a>
# ## Data Assessment
# 
# >Let us import our dataset to check if we have errors to fix before we proceed to data cleaning/wrangling

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
covid = pd.read_csv(r'C:\Users\USER\Desktop\Data Analytics class\PYTHON\covid-data.csv')
covid.head()


# In[2]:


covid.describe()


# In[3]:


covid.shape


# >we have imported our data. we have 189999 rows and 34 columns in our dataset. lets assess our data to check for null values, duplicates, wrong datatype and outliers

# In[4]:


sum(covid.duplicated())


# In[5]:


covid.info()


# >from the information above, we can see that our date datatype is written as object instead of datetime. continent has missing values too which we will fill up. we will also drop some tables that we dont need for our analysis

# In[6]:


#covid["date"]=covid["date"].astype("datetime64[ns]")


# In[6]:


covid['date']=pd.to_datetime(covid['date']) #we have change our date datatype


# In[7]:


data_type = covid['date'].dtype
print(data_type)


# In[8]:


covid = covid.dropna(subset=['date'])  


# In[9]:


covid["date"].isnull().sum() #because we dont have missing values in our date column, this code returned zero


# In[10]:


covid['date'].dt.year.value_counts() #we have the complete 3 years as shown in our dataset


# In[11]:


summary_stats = covid['date'].describe(datetime_is_numeric=True)
print(summary_stats)


# In[12]:


covid['continent'].value_counts() # here we have just 6 continents showing instead of 7, meaning we have missing values


# In[13]:


covid.isnull().sum()


# >the missing values we have is in continent as we observed earlier. lets fill it up

# In[14]:


covid.fillna('Unknown', inplace = True)


# In[15]:


covid['continent'].value_counts() # missing value filled with unknown


# In[16]:


covid['location'].value_counts()


# our location has incorrect entries like lower middle income, lower income,high income, and international written as states

# In[17]:


incorrect_locations = {'Lower middle income': 'Unspecified', 'lower incone': 'Unspecified', 'International': 'Unspecified', 'High income': 'Unspecified'}
covid['location'].replace(incorrect_locations, inplace = True)


# In[18]:


covid['location'].value_counts() # incorrect locations corrected


# <a id='eda'></a>
# ## Exploratory Data Analysis

# In[19]:


covid.describe() 


# lets check for correlation between relevant numerical variables

# In[20]:


numeric_variables = covid.iloc[:,4:34]
numeric_variables.head(5)


# In[21]:


corr = numeric_variables.corr()
corr


# In[22]:


covid_corr = covid[['population', 'total_tests', 'positive_rate', 'total_deaths', 'human_development_index']]


# In[23]:


corr = covid_corr.corr()
corr


# In[24]:


plt.figure(figsize=(10,7))
sns.heatmap(covid_corr.corr(), annot=True, cmap='cool', vmin=-1, vmax=1, linewidth=0.5)
plt.title('Correlation Between variables', pad = 30)
plt.show()


# from the above visual, we can note that correlation exist between population, total_deaths, positive rate, human development index. judging by the human population, we recorded high percentage of covid test that came out positive same way we recorded high covid 19 deaths. the human development index has a positive rate too as it affected a large number of the population.

# In[25]:


covid = covid.copy() # we make a copy of our previous dataset so that we can be able to work with the entire columns


# In[26]:


covid.columns


# In[27]:


total_cardiovasc_death_rate = covid['cardiovasc_death_rate'].sum()
total_cardiovasc_death_rate


# In[28]:


death_corr = covid.groupby('continent')['cardiovasc_death_rate'].sum().sort_values(ascending = False)
plt.figure(figsize = [9,5])
plt.bar(death_corr.index, death_corr.values, width = 0.5, color = 'red')
plt.xlabel('Continent')
plt.ylabel('Cardiovasc Death Cases Reported')
plt.title('Total cardiovasc death by continent', loc = 'center', pad = 10)
plt.xticks(rotation = 50)
plt.show()


# We noted that we have more cardiovasc death cases in african continent and less in South America

# In[31]:


# some columns wont be needed for our analysis so lets drop them


# In[29]:


covid.drop(['total_boosters', 'life_expectancy', 'tests_units', 'diabetes_prevalence', 'new_cases', 'new_deaths', 'hospital_beds_per_thousand', 'new_vaccinations', 'hosp_patients', 'tests_units', 'stringency_index', 'iso_code', 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million', 'people_fully_vaccinated', 'population_density', 'new_vaccinations', 'total_vaccinations'], axis = 1, inplace =True)
covid.head()


# <a id='eeda'></a>
# ## Explanatory Data Analysis

# ### Problem Statement 1
# Generate relevant KPI's or metrics regarding the dataset: such as
# 
# Total cases reported
# 
# Total Deaths
# 
# Case Fatality Rate (CFR): Percentage of confirmed COVID-19 cases that result in death.

# In[30]:


total_cases_reported = covid["total_cases"].sum()
total_cases_reported


# In[31]:


total_deaths_reported = covid["total_deaths"].sum()
total_deaths_reported


# In[32]:


total_cardiovasc_death_rate = covid['cardiovasc_death_rate'].sum()
total_cardiovasc_death_rate


# In[33]:


cfr = (8294940569 / 548591469648)
print(cfr)


# In[34]:


cfr = (8294940569 / 548591469648) * 100
print("The Case Fatality Rate (CFR) is: {:.3f}%".format(cfr)) 


# From the record above, 1.5percent is a high rate. this shows that more people with covid 19 died as against people with cardiovasc disease

# ### Problem Statement 2
# Show how total number of covid-19 cases vary over different continents illustrating atleast top 5 continents with the highest covid cases.

# In[35]:


covid['continent'].value_counts()


# In[36]:


cases_by_continent = covid.groupby('continent')['total_cases'].sum().reset_index()
cases_by_continent.sort_values(by='total_cases',ascending = False)


# In[37]:


cases_by_continent = cases_by_continent.sort_values(by='total_cases', ascending=False)
top_5_continents = cases_by_continent.head(5)
top_5_continents


# In[38]:


plt.figure(figsize=(10, 5))
plt.bar(top_5_continents.continent, top_5_continents.total_cases, width = 0.5, color='red')
#plt.bar_label(plt.bar(top_5_continents.continent, top_5_continents.total_cases, width = 0.5, color='blue'))
plt.xlabel('Continent')
plt.ylabel('Total Cases Reported')
plt.title('Total COVID-19 Cases by Continent (Top 5)', loc = 'center')
plt.xticks(rotation=20)
plt.show()


# We couldnt identify the country with the highest covid case as we have some unknown values in our data set. that not withstanding, we also noted that we recorded less cases in Africa and Oceania

# ### Problem Statement 3
# Which countries have experienced significant fluctuations in the reproduction rate (R-value) of COVID-19 transmission?

# In[39]:


fluctuations_in_reproduction = covid.groupby('continent')['reproduction_rate'].sum().sort_values(ascending = False)
fluctuations_in_reproduction


# In[40]:


plt.figure(figsize= [10,5])
plt.bar(fluctuations_in_reproduction.index, fluctuations_in_reproduction.values, width = (0.6), color='blue')
plt.xlabel('Continent')
plt.ylabel('Reproduction_rate')
plt.title('Fluctuation_In_Reproduction_Rate')
plt.show()


# Oceania and South Africa has the lowest reproduction rate due to covid effect. Africa wasnt affected much either because (fromthe previous analysis) it recorded more cardiovasc deaths and low covid 19 deaths

# ### Problem Statement 4
# What is the distribution of COVID-19 cases and deaths among different age groups, and how does it vary across continents?

# In[41]:


# since our value is given in percentage, lets calculate distribution of cases and deaths among age groups for each country
covid['cases_65_old_dist'] = covid['aged_65_older'] * covid['total_cases'] / 100
covid['cases_70_old_dist'] = covid['aged_70_older'] * covid['total_cases'] / 100
covid['deaths_65_old_dist'] = covid['aged_65_older'] * covid['total_deaths'] / 100
covid['deaths_70_old_dist'] = covid['aged_70_older'] * covid['total_deaths'] / 100


# In[42]:


grouped_data = covid.groupby('continent').agg({
    'cases_65_old_dist': 'sum',
    'cases_70_old_dist': 'sum',
    'deaths_65_old_dist': 'sum',
    'deaths_70_old_dist': 'sum'
}).reset_index()
grouped_data.head(7)


# In[43]:


# graphical representation of distribution of cases among age groups across continents
plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1)
sns.barplot(data=grouped_data, x='continent', y='cases_65_old_dist', color='blue', label='65 older')
sns.barplot(data=grouped_data, x='continent', y='cases_70_old_dist', color='red', label='70 older')
plt.title('Distribution of Cases Among Age Groups Across Continents')
plt.xlabel('Continent')
plt.ylabel('Number of Cases')
plt.xticks(rotation=90)
plt.tight_layout()
plt.legend()
plt.show()


# In[44]:


# Distribution of deaths among age groups across continents
plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 2)
sns.barplot(data=grouped_data, x='continent', y='deaths_65_old_dist', color='blue', label='65 older')
sns.barplot(data=grouped_data, x='continent', y='deaths_70_old_dist', color='red', label='70 older')
plt.title('Distribution of Deaths Among Age Groups Across Continents')
plt.xlabel('Continent')
plt.ylabel('Number of Deaths')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()


# Europe has the highest number of cases and death rate for individuals aged 65 as against Africa and Oceania which recorded few cases and deaths

# <a id='conclusions'></a>
# ### Conclusions

# In conclusion,from the analysis carried out,we recorded total number of 48591469648 covid 19 cases with 8294940569 reported total deaths. we observed that continents like Europe, South America and Asia recorded the highest covid deaths than other continents, also Africa, Asia, and Europe recorded more cardiovasc death. comparing the reported covid cases with the reported deaths, we have a case fatality rate of 1.5% which is quite high. Comparing the reproduction rate with continent, we observed that the reproduction rate in Oceania dropped due to covid 19 while the reproduction rate in continents like Europe, Africa and Asia remained almost same. Checking the effect of covid 19 cases on people fron age 65 upwars, we observed that Europe, South America and Asia the highest number of covid cases and deaths for individuals within that age range with Europe having the highest number. Generally its safe to say that Europe was affected more in the covid 19 case that was reported/recorded from 2020 to 2022.

# <a id='limitation'></a>
# ### Limitations

# The dataset i used for this analysis is quite dirty, we had records like lower middle income, international, middle income recorded as continents and we have so many missing values under continent which made our analysis a bit hard. from the bar chat above, we can see that the continent that recorded the highest covid case is showing as unknown as we had inconsistent data. from the data provided, we are unable to confirm the exact continent with high covid case

# In[45]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Project_on_Covid19.ipynb'])


# In[ ]:




