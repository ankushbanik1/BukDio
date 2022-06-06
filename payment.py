
import requests
import json
import webbrowser

def payment():

        
    url = "https://sandbox.cashfree.com/pg/orders"

    payload = {
        "customer_details": {
            "customer_phone": "9091203984",
            "customer_email": "ankushbanik123@gmail.com",
            "customer_id": "125373"
        },
        "order_amount": 100,
        "order_currency": "INR"
    }
    headers = {
        "Accept": "application/json",
        "x-client-id": "1737782e51daec5ffc36b56c72877371",
        "x-client-secret": "49fc541b91838f319acb1972839e57c769e5c3a5",
        "x-api-version": "2022-01-01",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

  


    dct = response.json()
    payment_link = dct['payment_link']

    webbrowser.open(payment_link)

payment()    