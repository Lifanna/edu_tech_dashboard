import streamlit as st
import pandas as pd
import numpy as np
import dashboard_charts

st.markdown("<h1 style='text-align: center;'>Dashboard for Educational Technologies Hackathon</h1>", unsafe_allow_html=True)

DATE_COLUMN = 'ApplicantName'
DATA_URL = ('PreProcessing.csv')

def load_data():
    data = pd.read_csv(DATA_URL)

    return data

data_load_state = st.text('Loading data...')

data = load_data()

data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

def get_stud_rating():
    st.pyplot(dashboard_charts.students_by_cgpa(data))

stud_rating_btn = st.button("Students rating", key=None, help=None, on_click=get_stud_rating, args=None, kwargs=None, disabled=False)

def get_stud_attention():
    st.pyplot(dashboard_charts.students_by_attention(data))

stud_attempts_btn = st.button("Students attention", key=None, help=None, on_click=get_stud_attention, args=None, kwargs=None, disabled=False)

def get_stud_attempts():
    st.pyplot(dashboard_charts.students_by_attempts(data))

stud_attempts_btn = st.button("Students attempts", key=None, help=None, on_click=get_stud_attempts, args=None, kwargs=None, disabled=False)
