import streamlit as st
import backtrader as bt
import yfinanceas as yf
st.write('hi')
data = bt.feeds.PandasData(dataname=yf.download('AAPL', '2014-01-01', '2017-01-01'))
st.dataframe(data)
