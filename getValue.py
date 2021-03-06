import yfinance as yf
import datetime

#define the ticker symbol
#tickerSymbol = https://finance.yahoo.com/quote/%5ETWII?p=^TWII&.tsrc=fin-srch

tickerSymbol = '2330.TW'

#get data on this ticker

def showValue(tic):
	tickerSymbol=tic
	startD=(datetime.datetime.now()-datetime.timedelta(days=10)).strftime("%Y-%m-%d")
	endD=datetime.datetime.now().strftime("%Y-%m-%d")
	tickerData = yf.Ticker(tickerSymbol)
	tickerDf = tickerData.history(period='1d', start=startD, end=endD)
	print("\n\n\n %s\n" % tickerSymbol)
	print(tickerDf.__dict__)
	print(dir(tickerDf))
	print(tickerDf)

showValue('MSFT')
showValue('2330.TW')
showValue('^DJI')
showValue('0050.TW')
showValue('^TWII')

