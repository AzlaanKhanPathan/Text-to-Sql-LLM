from dotenv import load_dotenv
load_dotenv() ## Load all the environment variables 

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## Configure our API Key 

genai.configure(api_key = os.getenv("AIzaSyDvKJuHCXmyAnD5lV08OzaXKSiHFYH4Dhg"))

# Function to load Google Gemini Model and provide sql query as response 

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text


# Function to retrieve query from the sql database 

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


## Define Your Prompt 

prompt = [
    '''
    You are an expert in converting English questions to SQL query !
    The SQL database has the name STUDENT and has the following columns - NAME,CLASS,
    SECTION and MARKS \n\n For example, \n Example 1- How many entries of records are present ? ,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \n Example 2 - Tell me all the students studying in Data Science class ?,
    the SQL Command will be something like this SELECT * FROM STUDENT 
    where CLASS= "Data Science";
    also the sql code should not have ``` in the beginning or end and sql word in the outcome


'''
]

## Streamlit App 

st.set_page_config(page_title="I can Retrieve any SQL Query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input('Input: ', key="input")

submit = st.button("Ask the question")


## If sumbit is clicked 
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The Response is ")
    for row in data:
        st.write(row)  # Use st.write for better formatting