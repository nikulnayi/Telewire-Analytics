import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt


col1,col2 = st.columns([0.75,6])

with col1:
    image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeqOxnyNX_UCarYAKSkIsY7CWQZlBzULPyMg&usqp=CAU'

    # Display the image with a caption
    st.image(image)
with col2:
    st.title("Cell Tower Anomaly Detection")
   
with st.sidebar:
    
    st.header("Upload Data file here for prediction")

    file = st.file_uploader("", type=["csv"])



if file is not None:
    df = pd.read_csv(file,encoding='windows-1254')
    

    with st.spinner('Processing...'):
    # Do some time-consuming computation
        time.sleep(0.75)

    # Once the computation is done, remove the spinner
    st.success('Processing done!')
    
    count_normal = df[df['Unusual']==0]['Unusual'].count()
    count_abnormal = df[df['Unusual']==1]['Unusual'].count()

    new_data = pd.DataFrame({'No of Normal/Abnormal':[count_normal,count_abnormal]},index=['Count of Nomal Tower','Count of Abnormal Tower'])
    st.dataframe(new_data)

    sizes = [count_normal,count_abnormal]
    # create a pie chart with the data
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=df['Unusual'].unique(), autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    st.pyplot(fig1)

    # st.dataframe(df.groupby('Unusual')['CellName'].value_counts())
    # print(df.groupby('CellName').aggregate({'Unusual':'count'}))
    # st.bar_chart()

