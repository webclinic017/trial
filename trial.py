import streamlit as st
import backtrader as bt
import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
st.write('hi')
df = pdr.DataReader('AAPL', 'yahoo', start='2014-01-01', end='2017-01-01')
st.dataframe(df)
x=df['Close']
fig=plt.title(symbol + ' Bollinger Bands')
fig=plt.xlabel('Days')
fig=plt.ylabel('Closing Prices')
fig=plt.plot(x, label='Closing Prices')
st.pyplot(fig)
