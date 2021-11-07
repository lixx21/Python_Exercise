#!/usr/bin/env python
# coding: utf-8

# In[1]:


# FELIX PRATAMASAN
   
import mysql.connector
import pandas


# In[2]:


#Cencus data
connection1 = mysql.connector.connect(host="localhost", database="yourDATABASENAME", user="yourUSERNAME", password="yourPASSWORD")


# In[114]:


cursor = connection1.cursor()
cursor.execute('SELECT * FROM census_data')
results = cursor.fetchall()


# In[66]:


df = pandas.read_sql('SELECT * FROM census_data', connection1)
df.head()


# In[67]:


# Find the total number of crimes recorded in the CRIME table.
cursor.execute('SELECT COUNT(*) FROM chicago_crime_data')
res = cursor.fetchall()

res


# In[68]:


# List community areas with per capita income less than 11000.

cursor.execute('SELECT COMMUNITY_AREA_NAME, COMMUNITY_AREA_NUMBER FROM census_data WHERE per_capita_income < 11000' )
res = cursor.fetchall()

res


# In[69]:


# List all case numbers for crimes involving minors

cursor.execute('SELECT CASE_NUMBER FROM chicago_crime_data WHERE DESCRIPTION LIKE "%minor%" ' )
res = cursor.fetchall()

res


# In[70]:


# List all kidnapping crimes involving a child?(children are not considered minors for the purposes of crime analysis)

cursor.execute('SELECT CASE_NUMBER, PRIMARY_TYPE,DESCRIPTION FROM chicago_crime_data WHERE PRIMARY_TYPE LIKE "Kidnapping" AND DESCRIPTION LIKE "%child%" ' )
res = cursor.fetchall()

res


# In[71]:


# What kind of crimes were recorded at schools?

cursor.execute('SELECT primary_type FROM chicago_crime_data WHERE location_description LIKE "%school%"')
res = cursor.fetchall()

res


# In[72]:


# List the average safety score for all types of schools.

cursor.execute('SELECT AVG(SAFETY_SCORE) FROM chicago_public_schools')
res = cursor.fetchall()

res


# In[120]:


# List 5 community areas with highest % of households below poverty line.
#
cursor.execute('SELECT community_area_name, PERCENT_HOUSEHOLDS_BELOW_POVERTY FROM census_data ORDER BY PERCENT_HOUSEHOLDS_BELOW_POVERTY DESC LIMIT 5')
res = cursor.fetchall()

res


# In[115]:


# Which community area(number) is most crime prone?

cursor.execute('SELECT MAX(community_area_number) FROM chicago_crime_data')
res = cursor.fetchall()

res


# In[82]:


# Use a sub-query to find the name of the community area with highest hardship index.

cursor.execute('SELECT community_area_name FROM census_data WHERE HARDSHIP_INDEX = (SELECT MAX(HARDSHIP_INDEX) FROM census_data)')
res = cursor.fetchall()

res


# In[89]:


# Use a sub-query to determine the Community Area Name with most number of crimes?

cursor.execute('SELECT community_area_name FROM census_data WHERE community_area_number = (SELECT max(community_area_number) FROM census_data) ')
res = cursor.fetchall()

res


# In[6]:


#create table

cusor.execute('CREATE TABLE test(ID char(2) PRIMARY KEY NOT NULL, FirstName varchar(50) NOT NULL, LastName varchar(50) NOT NULL)')
result = cur.fetchall()

result


# In[121]:


cursor.close()
connection1.close()


# In[ ]:




