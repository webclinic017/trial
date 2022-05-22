import streamlit as st
import backtrader as bt
import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import matplotlib
from rsi import RSIStrategy
st.set_option('deprecation.showPyplotGlobalUse', False)
title="""
    <style>
    .stockify {
    text-align: center;
    margin-top: -100px;
    margin-left: 67px;
    font-size: 40px;
    font-family: Arial, Helvetica, sans-serif;
    letter-spacing: 2px;
    }
    </style>
    <body>
    <p1 class='stockify'>Stockify</p1>
    </body>
    """
st.sidebar.markdown(title, unsafe_allow_html=True)
st.sidebar.write('_______________________')
title_alignment2="""
    <style>
    .trial2 {
    text-align: center;
    margin-top: -30px;
    margin-left: -13px;
    font-size: 300px;
    }
    </style>
    <body>
    <h1 class='trial2'>Select your dashboard</h1>
    </body>
    """
st.sidebar.markdown(title_alignment2, unsafe_allow_html=True)
dashboard = st.sidebar.selectbox('', ('Home', 'Fundamental Analysis', 'Technical Indicators', 'Backtesting', 'Pattern Stocks'), 0)
st.title(dashboard)
st.write('___')
st.write('hi')
df = pdr.DataReader('AAPL', 'yahoo', start='2014-01-01', end='2017-01-01')
st.dataframe(df)
x=df['Close']
matplotlib.use('Agg')
fig=plt.title('AAPL' + ' Bollinger Bands')
fig=plt.xlabel('Days')
fig=plt.ylabel('Closing Prices')
fig=plt.plot(x, label='Closing Prices')
fig=plt.savefig(fname='hi')
st.pyplot(fig)
