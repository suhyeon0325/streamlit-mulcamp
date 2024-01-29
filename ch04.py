# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.graph_objects as go 
import plotly.express as px 
from plotly.subplots import make_subplots 
import plotly

@st.cache_data  
def load_data():
    df = sns.load_dataset('tips')
    return df  

def main():
    # st.write(mpl.__version__)
    st.title("Streamlit with Matplotlib")  
    tips = load_data()  

    # 데이터가공
    m_tips = tips.loc[tips['sex'] == 'Male', :]
    f_tips = tips.loc[tips['sex'] == 'Female', :]
    # 시각화 차트
    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    ax[0].scatter(x = m_tips['total_bill'], y = m_tips['tip'])
    ax[0].set_title('Male')
    ax[1].scatter(x = f_tips['total_bill'], y = f_tips['tip'])
    ax[1].set_title('Female')

    st.pyplot(fig)

    # seaborn
    fig, ax = plt.subplots()
    sns.barplot(x='sex', y='tip', data=tips, ax=ax)
    st.pyplot(fig)

    # plotly
    fig = px.bar(tips, x='day', y='tip', 
                 color='day', 
                 labels={'day': 'Day', 'sex': 'Sex'}, 
                 height=400,
                 title='Average Tips by Day')
    
    st.plotly_chart(fig, use_container_width=True)

if __name__== "__main__":
    main()
