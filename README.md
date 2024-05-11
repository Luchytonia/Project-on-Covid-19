# Project on Covid 19 
## Table of content

   - [Introduction](#introduction)

   - [Data Assessment](#data-assessment)
   
   - [Data Wrangling](#data-wrangling)
   
   - [Exploratory Data Analysis](#exploratory-data-analysis)

   - [Exlanatory Data Analysis](#explanatory-data-analysis)
   
   - [Conclusion](#conclusion)

   - [Limitations](#limitations)
     
## Introduction
This is a project on covid 19 cases among different continents. In this python project, we will be evaluating dataset from different region(continents) to determine the rate/effect of covid 19. We will be looking out for 5 most affected regions. we will also check the death rate by age group and how it varies across different continents. basically checking the total cases reported, total deaths, and if covid 19 has any effect on birth rate and its effect across different continents. The dataset we will be using for this project is a .csv file and the data is from 2020 to 2022.

### Tools
- Numpy
- Pandas
- Seaborn
- Matplotlib
  
#### Lets import our data and the pasckages we will need for this analysis
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
covid = pd.read_csv(r'C:\Users\USER\Desktop\Data Analytics class\PYTHON\covid-data.csv')
covid.head()
```
![Imported data](https://github.com/Luchytonia/Project-on-Covid-19/assets/54556297/4d1e45b2-3e99-4675-9006-14f75d12bb53)

## Data Assessment

After importing our data, we changed out date datatype to datetime, we had missing values in some columns which was fixed, then outliers were corrected. this is is to help us have a clean dataset for our analysis. our dataset doesnt have any duplicates.
```
covid.describe()
```
![data describe](https://github.com/Luchytonia/Project-on-Covid-19/assets/54556297/ce65ef47-a33b-4817-b16d-8dc44bdfc9ab)

```
covid.shape
```
we have imported our data. we have 189999 rows and 34 columns in our dataset. lets assess our data to check for null values, duplicates, wrong datatype and outliers
```
sum(covid.duplicated())
```
We have 0 duplictaes
```
covid.info()
```
![covid info](https://github.com/Luchytonia/Project-on-Covid-19/assets/54556297/0167f1a2-5b6a-4939-9426-5795c6c08a92)

## Data Wrangling
from the information above, we can see that our date datatype is written as object instead of datetime. continent has missing values too which we will fill up. we will also drop some tables that we dont need for our analysis.
```
covid['date']=pd.to_datetime(covid['date'])
```
```
data_type = covid['date'].dtype
print(data_type)
```
we have change our date datatype
```
data_type = covid['date'].dtype
print(data_type)
```
because we dont have missing values in our date column, this code returned zero
```
covid['date'].dt.year.value_counts()
```

we have the complete 3 years as shown in our dataset
```
covid['continent'].value_counts()
```
![covid continent](https://github.com/Luchytonia/Project-on-Covid-19/assets/54556297/6b3c74ec-39ac-4215-8df1-00bd3af0c697)

here we have just 6 continents showing instead of 7, meaning we have missing values
```
covid.isnull().sum()
```
![covid isnull](https://github.com/Luchytonia/Project-on-Covid-19/assets/54556297/c7a9bf5a-5908-4139-b716-c0d646fb6c8d)

the missing values we have is in continent as we observed earlier. lets fill it up
```
covid.fillna('Unknown', inplace = True)
```
covid['continent'].value_counts()
```
missing value filled with unknown
```
covid['location'].value_counts()
```
our location has incorrect entries like lower middle income, lower income,high income, and international written as states
```
incorrect_locations = {'Lower middle income': 'Unspecified', 'lower incone': 'Unspecified', 'International': 'Unspecified', 'High income': 'Unspecified'}
```
covid['location'].replace(incorrect_locations, inplace = True)
```
```
covid['location'].value_counts()
```
incorrect locations corrected

## Exploratory Data Analysis
Here we analysed our dataset to understand correlation. lets check for correlation between relevant numerical variables
```
numeric_variables = covid.iloc[:,4:34]
numeric_variables.head(5)
```
```
corr = numeric_variables.corr()
corr
```
```covid_corr = covid[['population', 'total_tests', 'positive_rate', 'total_deaths', 'human_development_index']]
```
Here we selected the columns we want to work on
```
corr = covid_corr.corr()
corr
```
```
plt.figure(figsize=(10,7))
sns.heatmap(covid_corr.corr(), annot=True, cmap='cool', vmin=-1, vmax=1, linewidth=0.5)
plt.title('Correlation Between variables', pad = 30)
plt.show()
```
from the above visual, we can note that correlation exist between population, total_deaths, positive rate, human development index. judging by the human population, we recorded high percentage of covid test that came out positive same way we recorded high covid 19 deaths. the human development index has a positive rate too as it affected a large number of the population.
```
covid = covid.copy()
```
we make a copy of our previous dataset so that we can be able to work with the entire columns
```
covid.columns
```
Lets check cardiac deaths by continent
```
total_cardiovasc_death_rate = covid['cardiovasc_death_rate'].sum()
total_cardiovasc_death_rate
```
We noted that we have more cardiovasc death cases in african continent and less in South America

Meanwhile, some columns wont be needed for our analysis so lets drop them.
```
covid.drop(['total_boosters', 'life_expectancy', 'tests_units', 'diabetes_prevalence', 'new_cases', 'new_deaths', 'hospital_beds_per_thousand', 'new_vaccinations', 'hosp_patients', 'tests_units', 'stringency_index', 'iso_code', 'total_cases_per_million', 'new_cases_per_million', 'total_deaths_per_million', 'people_fully_vaccinated', 'population_density', 'new_vaccinations', 'total_vaccinations'], axis = 1, inplace =True)
covid.head()
```
## Explanatory Data Analysis
#### Problem Statement 1
Generate relevant KPI's or metrics regarding the dataset: such as

Total cases reported

Total Deaths

Case Fatality Rate (CFR): Percentage of confirmed COVID-19 cases that result in death.
```
total_cases_reported = covid["total_cases"].sum()
total_cases_reported
```
```
total_deaths_reported = covid["total_deaths"].sum()
total_deaths_reported
```
```
total_cardiovasc_death_rate = covid['cardiovasc_death_rate'].sum()
total_cardiovasc_death_rate
```
```
cfr = (8294940569 / 548591469648)
print(cfr)
```
```
cfr = (8294940569 / 548591469648) * 100
print("The Case Fatality Rate (CFR) is: {:.3f}%".format(cfr))
```
From the record above, 1.5percent is a high rate. this shows that more people with covid 19 died as against people with cardiovasc disease
#### Problem Statement 2
Show how total number of covid-19 cases vary over different continents illustrating atleast top 5 continents with the highest covid cases.
```
covid['continent'].value_counts()
```
```
cases_by_continent = covid.groupby('continent')['total_cases'].sum().reset_index()
cases_by_continent.sort_values(by='total_cases',ascending = False)
```
```
cases_by_continent = cases_by_continent.sort_values(by='total_cases', ascending=False)
top_5_continents = cases_by_continent.head(5)
top_5_continents
```
```
plt.figure(figsize=(10, 5))
plt.bar(top_5_continents.continent, top_5_continents.total_cases, width = 0.5, color='red')
#plt.bar_label(plt.bar(top_5_continents.continent, top_5_continents.total_cases, width = 0.5, color='blue'))
plt.xlabel('Continent')
plt.ylabel('Total Cases Reported')
plt.title('Total COVID-19 Cases by Continent (Top 5)', loc = 'center')
plt.xticks(rotation=20)
plt.show()
```
We couldnt identify the country with the highest covid case as we have some unknown values in our data set. that not withstanding, we also noted that we recorded less cases in Africa and Oceania
### Problem Statement 3
Which countries have experienced significant fluctuations in the reproduction rate (R-value) of COVID-19 transmission?
```
fluctuations_in_reproduction = covid.groupby('continent')['reproduction_rate'].sum().sort_values(ascending = False)
fluctuations_in_reproduction
```
```
plt.figure(figsize= [10,5])
plt.bar(fluctuations_in_reproduction.index, fluctuations_in_reproduction.values, width = (0.6), color='blue')
plt.xlabel('Continent')
plt.ylabel('Reproduction_rate')
plt.title('Fluctuation_In_Reproduction_Rate')
plt.show()
```
Oceania and South Africa has the lowest reproduction rate due to covid effect. Africa wasnt affected much either because (fromthe previous analysis) it recorded more cardiovasc deaths and low covid 19 deaths
### Problem Statement 4
What is the distribution of COVID-19 cases and deaths among different age groups, and how does it vary across continents?

Since our value is given in percentage, lets calculate distribution of cases and deaths among age groups for each country
```
covid['cases_65_old_dist'] = covid['aged_65_older'] * covid['total_cases'] / 100
covid['cases_70_old_dist'] = covid['aged_70_older'] * covid['total_cases'] / 100
covid['deaths_65_old_dist'] = covid['aged_65_older'] * covid['total_deaths'] / 100
covid['deaths_70_old_dist'] = covid['aged_70_older'] * covid['total_deaths'] / 100
```
```
grouped_data = covid.groupby('continent').agg({
    'cases_65_old_dist': 'sum',
    'cases_70_old_dist': 'sum',
    'deaths_65_old_dist': 'sum',
    'deaths_70_old_dist': 'sum'
}).reset_index()
grouped_data.head(7)
```
graphical representation of distribution of cases among age groups across continents
```
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
```
Distribution of deaths among age groups across continents
```
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
```
Europe has the highest number of cases and death rate for individuals aged 65 as against Africa and Oceania which recorded few cases and deaths
## Conclusion
In conclusion,from the analysis carried out,we recorded total number of 48591469648 covid 19 cases with 8294940569 reported total deaths. we observed that continents like Europe, South America and Asia recorded the highest covid deaths than other continents, also Africa, Asia, and Europe recorded more cardiovasc death. comparing the reported covid cases with the reported deaths, we have a case fatality rate of 1.5% which is quite high. Comparing the reproduction rate with continent, we observed that the reproduction rate in Oceania dropped due to covid 19 while the reproduction rate in continents like Europe, Africa and Asia remained almost same. Checking the effect of covid 19 cases on people fron age 65 upwars, we observed that Europe, South America and Asia the highest number of covid cases and deaths for individuals within that age range with Europe having the highest number. Generally its safe to say that Europe was affected more in the covid 19 case that was reported/recorded from 2020 to 2022.
## Limitations
The dataset i used for this analysis is quite dirty, we had records like lower middle income, international, middle income recorded as continents and we have so many missing values under continent which made our analysis a bit hard. from the bar chat above, we can see that the continent that recorded the highest covid case is showing as unknown as we had inconsistent data. from the data provided, we are unable to confirm the exact continent with high covid case

Click [here](https://github.com/Luchytonia/Project-on-Covid-19/blob/main/Project%20on%20Covid-19.py) to view the full project
