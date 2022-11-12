#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
#title of the app
st.markdown('''
# Exploratry Data Analysis Web Application
 __This app will show information about pakistan areas__''')
# upload data file form pc

with st.sidebar.header('Upload your dataset'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    df= sns.load_dataset('titanic')
    st.sidebar.markdown ("Eample Dataset CSV file")
# profile report pandas

if uploaded_file is not None:
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv 
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Pandas Profiling Report**')
    st.write(df)
    st.write('---')
    st.header('**Profile report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # example data
        @st.cache
        def load_data():
            a = pd.DataFrame( np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e'])
            return a
        df = load_data()
    pr=ProfileReport(df, explorative=True)
    st.header('**Pandas Profiling Report**')
    st.write(df)
    st.write('---')
    st.header('**Profile report with pandas**')
    st_profile_report(pr)
