import streamlit as st
import backtrader as bt
import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import matplotlib
from rsi import RSIStrategy
st.set_option('deprecation.showPyplotGlobalUse', False)
def get_fundamentals():
    try:
        # Find fundamentals table
        fundamentals = pd.read_html(str(html), attrs = {'class': 'snapshot-table2'})[0]
        
        # Clean up fundamentals dataframe
        fundamentals.columns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        colOne = []
        colLength = len(fundamentals)
        for k in np.arange(0, colLength, 2):
            colOne.append(fundamentals[f'{k}'])
        attrs = pd.concat(colOne, ignore_index=True)
    
        colTwo = []
        colLength = len(fundamentals)
        for k in np.arange(1, colLength, 2):
            colTwo.append(fundamentals[f'{k}'])
        vals = pd.concat(colTwo, ignore_index=True)
        
        fundamentals = pd.DataFrame()
        fundamentals['Attributes'] = attrs
        fundamentals['Values'] = vals
        fundamentals = fundamentals.set_index('Attributes')
        return fundamentals

    except Exception as e:
        return e
    
def get_news():
    try:
        # Find news table
        news = pd.read_html(str(html), attrs = {'class': 'fullview-news-outer'})[0]
        links = []
        for a in html.find_all('a', class_="tab-link-news"):
            links.append(a['href'])
        
        # Clean up news dataframe
        news.columns = ['Date', 'News Headline']
        news['Article Link'] = links
        news = news.set_index('Date')
        return news

    except Exception as e:
        return e

def get_insider():
    try:
        # Find insider table
        insider = pd.read_html(str(html), attrs = {'class': 'body-table'})[0]
        
        # Clean up insider dataframe
        insider = insider.iloc[1:]
        insider.columns = ['Trader', 'Relationship', 'Date', 'Transaction', 'Cost', '# Shares', 'Value ($)', '# Shares Total', 'SEC Form 4']
        insider = insider[['Date', 'Trader', 'Relationship', 'Transaction', 'Cost', '# Shares', 'Value ($)', '# Shares Total', 'SEC Form 4']]
        insider = insider.set_index('Date')
        return insider

    except Exception as e:
        return e
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
    elif s_fundament=='Check fundamentals':
        symbol=st.sidebar.text_input("Ticker", value='AAPL', max_chars=10)
        pd.set_option('display.max_colwidth', 25)
        st.subheader(f"{symbol}'s Fundamentals ")
        # Set up scraper
        url = ("https://finviz.com/quote.ashx?t=" + symbol.lower())
        req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
        webpage = urlopen(req)
        html = bs(webpage, "html.parser")
        fundament=get_fundamentals()
        inside=get_insider()
        news=get_news()
        st.write(fundament)
        st.write('Several important indicators which could be used like marketcap, P/E, PEG, Debt/Eq, ROI etc have been indicated within the dataframe above. These can be used to find entry and exit positions and see if the company is fundamentally sound.')
        st.write('_______________________________________________________________________________________________')
        st.subheader("\n\nRecent trades made by company's officials")
        st.write(inside)
        st.write('**When Insiders Buy, Should Investors Join Them?**\n \n')
        st.write('''This question doesn't have any right answers but one could sure speculate based on this information.\n
Tips for beating the market tend to come and go quickly, but one has held up extremely well: if executives, directors, or others with inside knowledge of a public company are buying or selling shares, investors should consider doing the same thing. Research shows that insider trading activity is a valuable barometer of broad shifts in market and sector sentiment.

However, before chasing each insider move, outsiders need to consider the factors that dictate the timing of trades and the factors that conceal the motivations and also that information is made public after a delay of the transaction made.''')
        st.write('_______________________________________________________________________________________________')
        st.subheader(f'Recent news on {symbol} stock')
        st.write(news)
        st.write('')
        st.write("\nStocks correlate the performance with the current market conditions and business news. They also predict the performance of the stock market and advise on buying and selling of stocks, mutual funds, and other securities.")

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
