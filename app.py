from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-2.5-pro-exp-03-25')
    response=model.generate_content([prompt,question])
    return response.text



#function to retrieve to query from database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    rows=None
    # print(type(sql))
    sql = sql.replace("```","")
    sql = sql.replace("sql","")
    try:
        cur.execute(sql)
        rows=cur.fetchall()
    except:
        print("Error occured")
    finally:
        if(rows):
            for row in rows:
                print(row)
            
        conn.commit()
        conn.close()
    
    return rows
    

prompt='''
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns- NAME, CLASS, SECTION and MARKS
For example, Example 1 - How many entries of records are present, the SQL command will be something like
SELECT COUNT(*) from STUDENT;
\nExample 2 - Tell me all the students studying in Data Science class., the SQL command will be something like 
SELECT * from STUDENT where CLASS='Data Science';
also the generated sql code should not have ``` in beginining or end and sql word in the output
'''


#Stream lit app

st.set_page_config(page_title='I can retrieve any SQL query')
st.header('Text-to-sql model to retrieve SQL Data')

question=st.text_input('Input: ',key='input')

submit=st.button('Ask the question')

if submit:
    response=get_gemini_response(question,prompt)
    # response=get_response(question,prompt)
    print(response)
    data=read_sql_query(response,'student.db')
    st.subheader(f'Generated query is\n:{response}')
    st.subheader('The responses is')
    for row in data:
        print(row)
        st.header(row)