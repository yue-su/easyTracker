from .models import Stock
import yfinance as yf

def update_stock_info():
    ticker_list = Stock.objects.all()
    ticker_symbols = [ticker.ticker for ticker in ticker_list]
    tickers = yf.Tickers(' '.join(ticker_symbols))

    # extract keys from tickers object
    for ticker in ticker_list:
        ticker_info = tickers.tickers[ticker.ticker].info
        # extract currentPrice, open, previousClose, dayLow, dayHigh, and calculate change in price and percent change
        current_price = round(float(ticker_info['currentPrice']), 2)
        previous_close = round(float(ticker_info['previousClose']), 2)
        change = round((current_price - previous_close), 2)
        change_percent = round((change / previous_close) * 100, 2)

        # get the history data from the ticker object for the past 7 days
        history = tickers.tickers[ticker.ticker].history(period='7d')
        # check each day changes in percentage and add to the list with other info in the row;
        history_list = []
        for index, row in history.iterrows():
            open_price = round(row['Open'], 2)
            close_price = round(row['Close'], 2)
            day_change = round((close_price - open_price), 2)
            day_change_percent = round((day_change / open_price) * 100, 2)
            history_list.append({
                'date': index.strftime('%Y-%m-%d'),
                'open': open_price,
                'close': close_price,
                'change': day_change,
                'changePercent': day_change_percent
            })
        # add the list to the ticker history
        ticker.history = history_list
        
        isLastTwoDaysChangeNegative = history_list[-1]['change'] < 0 and history_list[-2]['change'] < 0;
        isLastThreeDaysChangeNegative = history_list[-1]['change'] < 0 and history_list[-2]['change'] < 0 and history_list[-3]['change'] < 0;

        if isLastTwoDaysChangeNegative:
            last_two_days_change_negative = 'Yes'
        else:
            last_two_days_change_negative = 'No'
        
        if isLastThreeDaysChangeNegative:
            last_three_days_change_negative = 'Yes'
        else:
            last_three_days_change_negative = 'No'
        
        ticker.info = {
            'currentPrice': current_price,
            'previousClose': previous_close,
            'open': round(ticker_info['open'], 2),
            'dayLow': round(ticker_info['dayLow'], 2),
            'dayHigh': round(ticker_info['dayHigh'], 2),
            'change': change,
            'changePercent': change_percent,
            'lastDayChange': history_list[-1]['change'],
            'lastDayChangePercent': history_list[-1]['changePercent'],
            'theDayBeforeLastDayChange': history_list[-2]['change'],
            'theDayBeforeLastDayChangePercent': history_list[-2]['changePercent'],
            'ifLastTwoDaysChangeNegative': last_two_days_change_negative,
            'ifLastThreeDaysChangeNegative': last_three_days_change_negative,
        }
        ticker.save()
    
    