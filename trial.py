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
if dashboard=='Home':
    file_ = open("C:/Users/Utki/Desktop/code/stock/Picture1.png", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.header('Welcome to Stockify')
    title_alignment2='''
    <style>
    .trial {
    width: 55px;
    margin-top: -425px;
    margin-left: 130px;
    }
    </style>
    <body>
    <img src="https://img.icons8.com/nolan/344/home-page.png" alt="House" class='trial'></img>
    </body>
    '''
    image1='''
    <style>
    .stocks {
    width: 50px;
    margin-top: -165px;
    margin-left: 320px;
    }
    </style>
    <body>
    <img src="https://img.icons8.com/external-xnimrodx-lineal-gradient-xnimrodx/344/external-stock-economy-xnimrodx-lineal-gradient-xnimrodx.png" alt="House" class='stocks'></img>
    </body>'''
    #st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True,)
    st.markdown(title_alignment2, unsafe_allow_html=True)
    st.markdown(image1, unsafe_allow_html=True)
    st.subheader('What is stockify?')
    st.write('Stockify is a web application developed on python using the streamlit library which aims to provide you with the tools necessary to make trading and investing much simpler.\n ')
    st.write('''You can use this web app to do\n
1. Fundamental Analysis\n
2. Technical Analysis\n
3. Backtesting''')
if dashboard=='Fundamental Analysis':
    s_fundament = st.sidebar.selectbox('What would you like to do?', ('Learn', 'Check fundamentals'), 0)
    if s_fundament=='Learn':
        st.subheader('What Is Fundamental Analysis?')
        st.write('''• Fundamental analysis is a method of determining a stock's real or "fair market" value.\n
• Fundamental analysts search for stocks that are currently trading at prices that are higher or lower than their real value.\n
• If the fair market value is higher than the market price, the stock is deemed to be undervalued and a buy recommendation is given.\n
• In contrast, technical analysts ignore the fundamentals in favor of studying the historical price trends of the stock.\n''')
        st.subheader('Understanding Fundamental Analysis')
        st.write('''All stock analysis tries to determine whether a security is correctly valued within the broader market. Fundamental analysis is usually done from a macro to micro perspective in order to identify securities that are not correctly priced by the market.\n
For stocks, fundamental analysis uses revenues, earnings, future growth, return on equity, profit margins, and other data to determine a company's underlying value and potential for future growth. All of this data is available in a company's financial statements.\n''')
        st.subheader('Financial Statements: Quantitative Fundamentals to Consider')
        st.write('Financial statements are the medium by which a company discloses information concerning its financial performance. Followers of fundamental analysis use quantitative information gleaned from financial statements to make investment decisions. The three most important financial statements are income statements, balance sheets, and cash flow statements.')
        st.write('')
        st.write('''**Check the fundamentals of any stock by entering the ticker in the sidebar on the next page.**\n''')

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
