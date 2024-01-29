#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
uploaded_file = st.file_uploader(r"C:\Users\Dell\Downloads\day 16 task2 csv.csv", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)


# In[2]:


import pandas as pd
import ipywidgets as widgets
from IPython.display import display
df = pd.read_csv(r"C:\Users\Dell\Downloads\day 16 task2 csv.csv")
dropdown = widgets.Dropdown(options=['', 'Name', 'Department', 'Salary'])
search_input = widgets.Text()
sort_button = widgets.Button(description="Sort")

def sort_data(b):
    if dropdown.value:
        display(df.sort_values(dropdown.value))

def search_data(change):
    if change['type'] == 'change' and change['name'] == 'value':
        display(df[df[dropdown.value].str.contains(search_input.value)])

dropdown.observe(search_data)
sort_button.on_click(sort_data)

display(dropdown, search_input, sort_button)


# In[3]:


import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output

df = pd.DataFrame({
    'Name': ['Employee1', 'Employee2'],
    'Department': ['Sales', 'Marketing'],
    'Salary': [50000, 60000]
})

dropdown = widgets.Dropdown(options=df['Name'].unique())
name_input = widgets.Text(value=df.loc[0, 'Name'])
department_input = widgets.Text(value=df.loc[0, 'Department'])
salary_input = widgets.IntText(value=df.loc[0, 'Salary'])
update_button = widgets.Button(description="Update")

def update_data(b):
    df.loc[df['Name'] == dropdown.value, 'Name'] = name_input.value
    df.loc[df['Name'] == dropdown.value, 'Department'] = department_input.value
    df.loc[df['Name'] == dropdown.value, 'Salary'] = salary_input.value
    with output:
        clear_output()
        display(df)

def on_dropdown_event(change):
    if change['type'] == 'change' and change['name'] == 'value':
        row = df[df['Name'] == dropdown.value]
        name_input.value = row['Name'].values[0]
        department_input.value = row['Department'].values[0]
        salary_input.value = row['Salary'].values[0]

dropdown.observe(on_dropdown_event)
update_button.on_click(update_data)

output = widgets.Output()
display(dropdown, name_input, department_input, salary_input, update_button, output)


# In[4]:


name_input = widgets.Text(placeholder='Enter Name')
department_input = widgets.Text(placeholder='Enter Department')
salary_input = widgets.IntText(placeholder='Enter Salary')
add_button = widgets.Button(description="Add")


def add_data(b):
    new_data = {'Name': name_input.value, 'Department': department_input.value, 'Salary': salary_input.value}
    df.loc[len(df)] = new_data
    with output:
        clear_output()
        display(df)

add_button.on_click(add_data)


output = widgets.Output()
display(name_input, department_input, salary_input, add_button, output)


# In[5]:


dropdown = widgets.Dropdown(options=df['Name'].unique())
delete_button = widgets.Button(description="Delete")

def delete_data(b):
    df.drop(df[df['Name'] == dropdown.value].index, inplace=True)
    dropdown.options = df['Name'].unique()
    with output:
        clear_output()
        display(df)

delete_button.on_click(delete_data)

output = widgets.Output()
display(dropdown, delete_button, output)


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'Name': ['Employee1', 'Employee2', 'Employee3', 'Employee4'],
    'Department': ['Sales', 'Marketing', 'Sales', 'HR'],
    'Salary': [50000, 60000, 70000, 80000]
})


plt.figure(figsize=(10, 6))
plt.hist(df['Salary'], bins=10, alpha=0.5)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Count')
plt.show()


plt.figure(figsize=(10, 6))
df['Department'].value_counts().plot(kind='bar')
plt.title('Department-wise Employee Count')
plt.xlabel('Department')
plt.ylabel('Count')
plt.show()


# In[7]:


import pandas as pd
import ipywidgets as widgets
from IPython.display import display, clear_output

df = pd.DataFrame({
    'Name': ['Employee1', 'Employee2', 'Employee3', 'Employee4'],
    'Department': ['Sales', 'Marketing', 'Sales', 'HR'],
    'Salary': [50000, 60000, 70000, 80000]
})

department_dropdown = widgets.Dropdown(options=[''] + list(df['Department'].unique()))
min_salary_input = widgets.IntText(value=df['Salary'].min())
max_salary_input = widgets.IntText(value=df['Salary'].max())
filter_button = widgets.Button(description="Filter")

def filter_data(b):
    filtered_df = df[(df['Department'] == department_dropdown.value) & 
                     (df['Salary'] >= min_salary_input.value) & 
                     (df['Salary'] <= max_salary_input.value)]
    with output:
        clear_output()
        display(filtered_df)

filter_button.on_click(filter_data)

output = widgets.Output()
display(department_dropdown, min_salary_input, max_salary_input, filter_button, output)


# In[8]:


df.to_csv('employee_data.csv', index=False)


# In[9]:


users = {
    'user': 'user'    
}

def login(username, password):
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

login('user', 'user')


# In[10]:


import ipywidgets as widgets
from IPython.display import display, clear_output

feedback_input = widgets.Textarea(placeholder='Enter your feedback here...')
submit_button = widgets.Button(description="Submit")

def submit_feedback(b):
    with output:
        clear_output()
        print("Thank you for your feedback!")

submit_button.on_click(submit_feedback)

output = widgets.Output()
display(feedback_input, submit_button, output)


# In[ ]:




