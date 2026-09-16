import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import streamlit as st


st.sidebar.title("California Housing Real Estate")
page = st.sidebar.selectbox("Select page",["Data Exploration 🔮","Data Visualization 📊"])




st.image("house.png")


if page == "Data Exploration 🔮":
    ## Part 1 Data exploration 
    st.subheader("01 Data Exploration")

    st.markdown("##### Display Dataset")

    ## Uploading the dataset
    df = pd.read_csv('housing.csv')

    ## for creating a slider on the number of rows we want to display 
    row=st.slider("Select a # of rows",3,100)
    ## displaying the dataset 
    st.dataframe(df.head(row))

    ## describe 
    st.markdown("##### Display statistical summary")
    st.dataframe(df.describe())


    ## check missing values 
    st.markdown("### Missing values")

    missing = df.isnull().sum()
    st.write(missing)

    if missing.sum()==0:
        st.success("The Dataset is clean 🧹")
    else:
        st.warning("⚠️ the dataset needs to be cleaned")


elif page == "Data Visualization 📊":
    st.subheader("02 Data Viz")
    df = pd.read_csv('housing.csv')

    col_x = st.selectbox('Select X axis variable',df.columns,index=0)
    col_y = st.selectbox('Select Y axis variable',df.columns,index=1)

    tab1, tab2, tab3 = st.tabs(["Bar Chart 📊","Line Chart📈","Heatmap 🔥"])


    with tab1: 
        st.markdown("#### Bar Chart - Streamlit")
        st.bar_chart(df[[col_x,col_y]].sort_values(by=col_x),use_container_width=True)

    with tab2:
        st.markdown("#### Line chart - Streamlit")
        st.line_chart(df[[col_x,col_y]].sort_values(by=col_x),use_container_width=True)




    with tab3:
        ## Create a correlation matrix 
        df2 = df.drop(["ocean_proximity"],axis=1)

        fig_corr, ax_corr= plt.subplots(figsize=(12,6))
        sns.heatmap(df2.corr(),annot=True)
        st.pyplot(fig_corr)