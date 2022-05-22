import streamlit as st
import backtrader as bt
import yfinance as yf
st.write('hi')
data = bt.feeds.PandasData(dataname=yf.download('AAPL', '2014-01-01', '2017-01-01'))
print(data)
st.dataframe(data)
