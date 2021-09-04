from flask import Flask, render_template,request
import requests
import json
import time

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=["POST","GET"])
def search():
    if request.method == 'GET':
        pin_code = request.args.get('pin')
        date = request.args.get('date')
        para = {"pincode":pin_code , "date":date}
        uri = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',}
        
        
        x = requests.get(url = uri , headers = headers , params = para , stream = True)
        data = x.json()
        #if(not data['sessions']):
        
    return data 


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
