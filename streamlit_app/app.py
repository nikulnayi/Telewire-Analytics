import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
import numpy as np
import seaborn as sns
from pathlib import Path

# from preprocessing
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
import dill
from sklearn import set_config

# from model
from xgboost import XGBClassifier,plot_importance

import sys

# import the pipeline file
sys.path.insert(0,'../src')
#import predict

st.set_page_config(
    page_title="Telewire Dashboard",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeqOxnyNX_UCarYAKSkIsY7CWQZlBzULPyMg&usqp=CAU",
)
col1,col2 = st.columns([0.75,6])

# with col2:
col1, mid, col2 = st.columns([200,20,20])
with col1:
    st.header('Cell Tower Anomaly Detection')
    
with col2:
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeqOxnyNX_UCarYAKSkIsY7CWQZlBzULPyMg&usqp=CAU.png', width=100)
    

# st.title("Cell Tower Anomaly Detection")
# st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeqOxnyNX_UCarYAKSkIsY7CWQZlBzULPyMg&usqp=CAU.png")
st.markdown("This is a web app that uses the Cell Tower Log data to predict if the current sample corresponds to normal or abnormal behaviour.")   
with st.sidebar:
    
    st.header("Upload Data file here for prediction")

    file = st.file_uploader("", type=["csv"])


    opt = st.radio(label = 'Who is viewing', options = ['Management','Data Science Team','Summary'])
    

 
if file is not None:
    df = pd.read_csv(file,encoding='windows-1254')

    x = df.iloc[:, :-1]  # Using all column except for the last column as X
    y = df.iloc[:, -1]  # Selecting the last column as Y

    if opt == 'Management':
        with st.spinner('Processing..'):
    # Do some time-consuming computation
        # time.sleep(0.75)
    
    # Once the computation is done, remove the spinner
        # st.success('Processing done!')
            Unusual = df[df['Unusual']==1]
            Unusual = Unusual[['Time','CellName','Unusual']]
            st.write('Below is the list of unusual acitivties predicted. \
                      Kindly take a look and consider re-configuration of the Cell Towers')
            st.dataframe(Unusual)
            Unusual = (Unusual.drop('Unusual',axis=1)).sample(100)
            count_normal = df[df['Unusual']==0]['Unusual'].count()
            count_abnormal = df[df['Unusual']==1]['Unusual'].count()

            c = alt.Chart(Unusual).mark_circle(size=40).encode(
            x='CellName', y='Time').properties(
            width=700,
            height=500
        )


            st.altair_chart(c, use_container_width=True)


        # new_data = pd.DataFrame({'No of Normal/Abnormal's:[count_normal,count_abnormal]},index=['Count of Nomal Tower','Count of Abnormal Tower'])
        # st.dataframe(new_data)

        # create the columns 
        kpi1,kpi2 = st.columns(2)
        kpi1.metric(
            label="Count of Usual Cell Tower Activity",
            value=count_normal
        )
        kpi2.metric(
            label="Count of Unusual Cell Tower Activity",
            value=count_abnormal
        )
        col1,col2=st.columns(2)
        with col1:
            # create a pie chart with the data
            st.text("Percentage share of Usual and Unusual Activity")
            sizes = [count_normal,count_abnormal]
            explode = (0, 0.1)
            fig1, ax1 = plt.subplots()
            labels=df['Unusual'].replace({0:"Usual",1:"Unusual"}).unique()

            ax1.pie(sizes, labels=labels[::-1],explode=explode, autopct='%1.1f%%', startangle=90)
            ax1.axis('equal')

            st.pyplot(fig1)
        with col2:
            # Bar graph
            # group by 'Cell Name' and count the number of occurrences of 0 and 1
            
            counts = (df.groupby(['CellName', 'Unusual'])['Unusual']).count()
            # convert counts to a DataFrame and unstack the 'Status' index level
            counts_df = counts.unstack(level='Unusual', fill_value=0)
            st.bar_chart(counts_df)
            # fig, ax = plt.subplots()
           
            # ax.bar(df['Unusual'].head(20), df['Time'].head(20))
            # st.pyplot(fig)
        #     prb_usage = px.bar(
        #     df, 
        #     x='PRBUsageUL',
        #     y='Unusual',
        #     labels={'y':'Unusual','x':'PRBUsageUL'},
        #     title= 'Bar chart',width=500, height=400,
        #     color='Unusual')
        # st.plotly_chart(prb_usage)

        col1,col2 = st.columns(2)
        
        n = st.slider('Number of features', 1, 13,3)
        def XGBoost(x, y):
                x = df.drop(['Time','CellName','maxUE_UL+DL','Unusual'],axis=1)
                model = XGBClassifier()
                model.fit(x, y)
                feat_importances = pd.Series(model.feature_importances_, index=x.columns).sort_values(ascending=True)
                top_n_features = feat_importances[:n]
                figure = px.bar(top_n_features,
                 x=top_n_features.values,
                y=top_n_features.keys(), labels = {'x':'Importance Value', 'index':'Columns'},
                text=np.round(top_n_features.values, 2),
                title= ' Feature Importance Plot',
                    width=1000, height=400)
                figure.update_layout({
                    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
                st.plotly_chart(figure)
        XGBoost(x,y)

  
        #st.pyplot(plot_importance(df).figure)
        # with col1:
        #     st.text("Distribution of Time During Unusual")
        #     fig, ax = plt.subplots()
        #     # ax.tick_params(axis='x', rotation=90)
        #     hour_data = pd.to_datetime(df[df['Unusual']==1]['Time'],format='%H:%M').dt.hour
            
        #     ax.hist(hour_data, bins=10,range=(0,24))
        #     # set the x-axis label
        #     plt.xlabel('Hour')

        #     # set the y-axis label
        #     plt.ylabel('Frequency')
        #     st.pyplot(fig)
    
        
        
        # # Create an Altair chart
        # chart = alt.Chart(df).mark_circle(size=25).encode(
        #     x='CellName',
        #     y='Time',
        #     color='Unusual'
        # ).properties(
        #     width=700,
        #     height=500
        # )

        # # Render the chart in Streamlit
        # st.altair_chart(chart, use_container_width=True)


    if opt == 'Data Science Team':
        st.markdown("The source code of this app is available on [Github](https://github.com/Anupriya-Sri/TBC-AIP-2023-A7_Telewire-Analytics)")
        
        col1,col2 = st.columns(2)
        with col1:
                # Stastics Summary
                st.write("## Stastical Summary")
                st.write(pd.DataFrame(df).describe())
        with col2:
                # missing values
                st.write("## Columns with missing values")
                if (df.isna().sum()>0).any():
                    missing_value_count = df.isnull().sum()
                    columns_missing_values = missing_value_count[missing_value_count > 0].index
                    # Subset the original DataFrame with the selected columns
                    df_subset = df[columns_missing_values].isnull().sum()
                    st.dataframe(df_subset.transpose())
                else:
                    st.markdown("### There are no missing values in uploaded data")

            # heat map to see the relationship of features

        st.markdown("### Heatmap to show relationship between features")
        fig, ax = plt.subplots(figsize=(18,15))
            
        cmap = sns.diverging_palette(220, 10, as_cmap=True)
        sns.heatmap(df.corr(), ax=ax,annot=True,cmap=cmap)
        st.pyplot(fig)

    if opt == 'Summary':
        def get_table(df):
            datatable = df.drop('Unusual',axis=1)
            return datatable
        datatable = get_table(df)
        st.markdown("### Summary of uploaded data")
        st.markdown("The following table gives you a quick view of the uploaded data.")
        st.dataframe(datatable)# will display the table
    
    # df = predict.predict(df)  
    