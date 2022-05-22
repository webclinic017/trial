import streamlit as st
import backtrader as bt
import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
st.write('hi')
df = pdr.DataReader('AAPL', 'yahoo', start='2014-01-01', end='2017-01-01')
st.dataframe(df)
