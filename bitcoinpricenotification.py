import requests
import time
from datetime import datetime

BITCOIN_PRICE_THRESHOLD = 50000  # Set this to whatever you like

coin_API_key = '0a4ed4d7-b56a-42d1-9467-a8efd2e93c6f' 
BITCOIN_API_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

ifttt_API_key =  ## Get your API key from your IFTTT account
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{0}/with/key/{1}'

def get_latest_bitcoin_price():  
    # This method gets the bitcoin data from coinmarketcap 

    parameters = {
    'start':'1',
    'limit':'5000',
    'convert':'USD'
    }

    # Get key from your coinmarketcap account
    
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': coin_API_key, 
    }

    print ("Send request")
    response = requests.get(BITCOIN_API_URL, params=parameters, headers = headers)
    response_json = response.json()

    print ("Got response")
    # Bitcoin data is the first element of the list
    bitcoin_data = response_json['data'][0] 
    price_USD = bitcoin_data['quote']['USD']['price']

    print (price_USD)
    return float(price_USD)

# We created two new IFTTT applets: one for emergency Bitcoin price notifications and one for regular updates.
def post_ifttt_webhook(event, value):
    # The payload that will be sent to IFTTT service
    data = {'value1': value}
    
    # inserts our desired event
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event, ifttt_API_key)

    # Sends a HTTP POST request to the webhook URL
    response = requests.post(ifttt_event_url, json=data)
    print (response.text)
    

def format_bitcoin_history(bitcoin_history):
    rows = []
    for bitcoin_price in bitcoin_history:
        # Formats the date into a string: '24.02.2018 15:09'
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']
        # <b> (bold) tag creates bolded text
        # 24.02.2018 15:09: $<b>10123.4</b>
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)

    # Use a <br> (break) tag to create a new line
    # Join the rows delimited by <br> tag: row1<br>row2<br>row3
    return '<br>'.join(rows)

# This method gets the latest price of bitcoin and send a notification if necessary
def main():
    
    bitcoin_history = []
    while True:
        price = get_latest_bitcoin_price()

        date = datetime.now()
        bitcoin_history.append({'date': date, 'price': price})

        # Send an emergency notification
        if price < BITCOIN_PRICE_THRESHOLD:
            post_ifttt_webhook('bitcoin_price_emergency', price)
            print ("After")

        # Send a Telegram notification
        # Once we have 5 items in our bitcoin_history send an update
        if len(bitcoin_history) == 5:
            post_ifttt_webhook('bitcoin_price_update', 
                               format_bitcoin_history(bitcoin_history))
            # Reset the history
            bitcoin_history = []

        # Sleep for 5 minutes 
        # (For testing purposes you can set it to a lower number)
        time.sleep(5 * 60)
        

if __name__ == '__main__':
    main()
