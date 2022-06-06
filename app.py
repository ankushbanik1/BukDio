from flask import Flask
from flask import redirect, url_for, request, render_template, send_file
from io import BytesIO
import flask
import pyttsx3
import PyPDF2
import selenium
import requests
import webbrowser
import os
app = Flask(__name__)

@app.route('/payu')
def home2():
    print(f"[+] NEW USER VISITED THE SERVER. [+] USER IP - {flask.request.remote_addr}")
    return render_template('sub.html')
@app.route('/upload')
def upload():
    print(f"[+] NEW USER VISITED THE SERVER. [+] USER IP - {flask.request.remote_addr}")
    return render_template('upload.html')

@app.route('/')
def home_page():
    print(f"[+] NEW USER VISITED THE SERVER. [+] USER IP - {flask.request.remote_addr}")
    return render_template('home.html')


@app.route('/get_pdf', methods=["GET", "POST"])
def get_pdf():
    if request.method == "POST":
        file = request.files['user_file']
        user_file_name = file.filename.replace(".pdf", "")
        full_text = ""
        reader = PyPDF2.PdfFileReader(file)
        audio_reader = pyttsx3.init()
        audio_reader.setProperty("rate", 150)       # This is the speed of reader.

        for page in range(reader.numPages):
            next_page = reader.getPage(page)
            content = next_page.extractText()
            full_text += content

        user_file_send = user_file_name.strip() + ".mp3"
        audio_reader.save_to_file(full_text, filename=user_file_send)
        audio_reader.runAndWait()
        
        return send_file(user_file_send, attachment_filename=user_file_send, as_attachment=True)

@app.route('/payment_cash', methods=["GET", "POST"])
def payment_cash():

    
        
    url = "https://sandbox.cashfree.com/pg/orders"

    payload = {
        "customer_details": {
            "customer_phone": "9091203984",
            "customer_email": "ankushbanik123@gmail.com",
            "customer_id": "125373"
        },
        "order_amount": 10,
        "order_currency": "INR",
        "returnUrl":"/"
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

    webbrowser.open_new_tab(payment_link)
    return render_template('upload.html')
        

@app.route('/payment_cash_plus', methods=["GET", "POST"])
def payment_cash349():

    
        
    url = "https://sandbox.cashfree.com/pg/orders"

    payload = {
        "customer_details": {
            "customer_phone": "9091203984",
            "customer_email": "ankushbanik123@gmail.com",
            "customer_id": "125373"
        },
        "order_amount": 349,
        "order_currency": "INR",
        "returnUrl":"/"
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

    webbrowser.open_new_tab(payment_link)
    return render_template('home.html')


@app.route('/payment_cash_premium', methods=["GET", "POST"])
def payment_cash499():

    
        
    url = "https://sandbox.cashfree.com/pg/orders"

    payload = {
        "customer_details": {
            "customer_phone": "9091203984",
            "customer_email": "ankushbanik123@gmail.com",
            "customer_id": "125373"
        },
        "order_amount": 499,
        "order_currency": "INR",
        "returnUrl":"/"
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

    webbrowser.open_new_tab(payment_link)
    return render_template('home.html')

@app.route('/payment_cash_basic', methods=["GET", "POST"])
def payment_cash199():

    
        
    url = "https://sandbox.cashfree.com/pg/orders"

    payload = {
        "customer_details": {
            "customer_phone": "9091203984",
            "customer_email": "ankushbanik123@gmail.com",
            "customer_id": "125373"
        },
        "order_amount": 199,
        "order_currency": "INR",
        "returnUrl":"/"
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

    webbrowser.open_new_tab(payment_link)
    return render_template('home.html')


if __name__ == "__main__":

    app.run()
    
    #payment()
    # host="0.0.0.0", port=5000
