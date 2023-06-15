
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px

#For Latitude and longitude
from geopy.geocoders import Nominatim
   

import warnings 
warnings.filterwarnings('ignore')

pd.set_option('display.max_rows' , None)
pd.set_option('display.max_columns' , None)

import os
import streamlit as st


st.title('Customer Prediction Analysis')


def read_dataset(filepath) : 
    data_import = pd.read_csv(filepath)
    return data_import 

data_import = read_dataset('customer_data.csv')


fig ,ax = plt.subplots()
freq_table = pd.crosstab(data_import['name'] , data_import['purchase_frequency'])
sns.barplot(x = 'name' , y = 'purchase_frequency' , data = data_import)
st.pyplot(fig)


fig ,ax = plt.subplots()
freq_table = pd.crosstab(data_import['country'] , data_import['purchase_frequency'])
sns.heatmap(freq_table, cmap='YlOrRd', annot=True, fmt='d')
st.pyplot(fig)



data_viz_df = data_import.drop(['name','country'] , axis = 1)

st.markdown("Pairplot of dataset with hue as purchase frequency")
fig,ax = plt.subplots()
sns.pairplot(data_viz_df , hue = 'purchase_frequency')
plt.savefig('pairplot_purhcase.png')
st.image("pairplot_purhcase.png")

fig,ax = plt.subplots()
sns.jointplot(x='age', y='purchase_frequency', data=data_import)
plt.savefig('age_purchase.png')
st.image('age_purchase.png')

fig,ax = plt.subplots()
sns.jointplot(x='gender', y='purchase_frequency', data=data_viz_df)
plt.savefig('gender_purchase.png')
st.image('gender_purchase.png')


fig,ax = plt.subplots()
sns.jointplot(x='education', y='purchase_frequency', data=data_viz_df)
plt.savefig('education_purchase.png')
st.image('education_purchase.png')



fig,ax = plt.subplots()
sns.jointplot(x='income', y='purchase_frequency', data=data_viz_df)
plt.savefig('income_purchase.png')
st.image('income_purchase.png')



fig,ax = plt.subplots()
sns.jointplot(x='spending', y='purchase_frequency', data=data_viz_df)
plt.savefig('spending_purchase.png')
st.image('spending_purchase.png')


st.write('Top 10 Countries with most purchases')
data_import.groupby('country')['purchase_frequency'].count().sort_values(ascending = False)[:10].plot(kind = 'pie' , autopct = '%1.1f%%' , shadow = True , explode = [0.1,0,0,0,0,0,0,0,0,0])
fig = plt.gcf()
plt.show()
st.pyplot(fig)


fig , ax = plt.subplots()
x = data_import.groupby('country')['purchase_frequency'].count().sort_values(ascending = False).index 
y = data_import.groupby('country')['purchase_frequency'].count().sort_values(ascending = False).values 
ax = sns.barplot(x = x , y = y)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
fig.set_size_inches(28, 9)
plt.show()
st.pyplot(fig)



