import streamlit as st
import backtrader as bt
import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import matplotlib
from rsi import RSIStrategy
st.set_option('deprecation.showPyplotGlobalUse', False)
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
