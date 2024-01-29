#!/usr/bin/env python
# coding: utf-8

# In[32]:


import streamlit as st
st.title("welcome to streamlit")
st.write("hello yusuf")


# In[33]:


from PIL import Image
image=Image.open(r"C:\Users\Dell\Pictures\foot.jpeg")
st.image(image, caption="Football!",use_column_width=True)


# In[34]:


name = st.text_input('yusuf')
if name:
    st.write(f'Hello, {name}!')


# In[35]:


if st.button('Click me'):
   
    st.write('Welcome to Streamlit!') 


# In[36]:


import streamlit as st
import pandas as pd


data_dict = {
    'Fruits': ['Apples', 'Bananas', 'Cherries', 'Dates'],
    'Quantity': [20, 34, 23, 17]
}


df = pd.DataFrame(data_dict)


st.write(df)


st.bar_chart(df.set_index('Fruits'))


# In[37]:


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)
    st.write(df)


# In[38]:


import numpy as np


num_bars = st.slider('Select the number of bars', min_value=1, max_value=10, value=5)


data = {'bars': range(num_bars), 'values': np.random.randint(0, 100, size=num_bars)}


df = pd.DataFrame(data)


st.bar_chart(df.set_index('bars'))


# In[39]:


import streamlit as st

def home():
    st.title("Home")
    st.write("This is the home page.")

def data():
    st.title("Data")
    st.write("This is the data page.")

def model():
    st.title("Model")
    st.write("This is the model page.")

def about():
    st.title("About")
    st.write("This is the about page.")

pages = {
    "Home": home,
    "Data": data,
    "Model": model,
    "About": about,
}

page = st.sidebar.selectbox("Choose a page", tuple(pages.keys()))

pages
page


# In[40]:


try:
    result = num1 / num2
    st.write('The result is ', result)
except ZeroDivisionError:
    st.error('Error: Division by zero is not allowed.')
except Exception as e:
    st.error(f'Error: An unexpected error occurred: {e}')


# In[ ]:




