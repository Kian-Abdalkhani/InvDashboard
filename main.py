from id_stock import id_ticker



def main() -> None:
    
    #id the type of ticker input
    tick = id_ticker("AAPL")
    print(tick.dividend_yield)
    
    '''items that should be able to be returned for analysis are:
            - Price Data: Close, Volume, CAGR statistics for price and/or Dividends(if any)
            
        If the selected ticker pays dividends, it should include the following:
            - Dividend Data: All dividend payouts and their dates, Dividend CAGR
            - Dividend Yield
        If ticker is ETF, it should include the following:
            - Expense Ratio
        If ticker is an individual company/stock, it should include the following:
            - Financial Data: Income Statement, Balance Sheet, select analytics to perform Yoy or Qoq analysis on
            '''
    
    
if __name__ == "__main__":
    main()