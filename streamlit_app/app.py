import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(
    page_title="Telewire Dashboard",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeqOxnyNX_UCarYAKSkIsY7CWQZlBzULPyMg&usqp=CAU",
)
col1,col2 = st.columns([0.75,6])

# with col2:
st.title("Cell Tower Anomaly Detection")
st.markdown("This is a web app that uses the Cell Tower Log data to predict if it perfroms abnormal or not. The source code of this app is available on [Github](https://github.com/Anupriya-Sri/TBC-AIP-2023-A7_Telewire-Analytics)")   
with st.sidebar:
    
    st.header("Upload Data file here for prediction")

    file = st.file_uploader("", type=["csv"])



if file is not None:
    df = pd.read_csv(file,encoding='windows-1254')
    

    with st.spinner('Processing...'):
    # Do some time-consuming computation
        # time.sleep(0.75)

    # Once the computation is done, remove the spinner
        st.success('Processing done!')
        
        count_normal = df[df['Unusual']==0]['Unusual'].count()
        count_abnormal = df[df['Unusual']==1]['Unusual'].count()

        # new_data = pd.DataFrame({'No of Normal/Abnormal':[count_normal,count_abnormal]},index=['Count of Nomal Tower','Count of Abnormal Tower'])
        # st.dataframe(new_data)

        # create the columns 
        kpi1,kpi2 = st.columns(2)
        kpi1.metric(
            label="Count of Nomal Cell Tower",
            value=count_normal
        )
        kpi2.metric(
            label="Count of Abnormal Cell Tower",
            value=count_abnormal
        )

        # create a pie chart with the data
        sizes = [count_normal,count_abnormal]
        explode = (0, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=df['Unusual'].replace({0:"Unusual",1:"Usual"}).unique(),explode=explode, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')

        st.pyplot(fig1)
        
        # Bar graph
        # group by 'Cell Name' and count the number of occurrences of 0 and 1
        counts = df.groupby(['CellName', 'Unusual'])['Unusual'].count()

        # convert counts to a DataFrame and unstack the 'Status' index level
        counts_df = counts.unstack(level='Unusual', fill_value=0)

        st.bar_chart(counts_df)

        # Abnormal count
        # st.write("Total no of Unusual Cell Tower:",count_abnormal)
        # st.write(df[df['Unusual']==1])

        # Celltower and time
        # fig, ax = plt.subplots()

        # ax.bar(df_grouped[df_grouped['Unusual'] == 0]['CellName'], 
        #         df_grouped[df_grouped['Unusual'] == 0]['Time'], label='X')
        # ax.bar(df_grouped[df_grouped['Unusual'] == 1]['CellName'], 
        #         df_grouped[df_grouped['Unusual'] == 1]['Time'], label='Y')
    
        # Create an Altair chart
        chart = alt.Chart(df).mark_circle(size=100).encode(
            x='CellName',
            y='Time',
            color='Unusual'
        ).properties(
            width=700,
            height=500
        )

        # Render the chart in Streamlit
        st.altair_chart(chart, use_container_width=True)
