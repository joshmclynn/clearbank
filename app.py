from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


##def index():
 ##   req = requests.get('https://api.thecatapi.com/v1/images/search?limit=5&page=10&order=Desc')
##    data = json.loads(req.content)
##    return render_template('index.html', data=data)

@app.route('/', methods = ['GET'])
def index():
    
    url = "https://api.thecatapi.com/v1/images/search"
    query = {'limit':'5'}
    headers = {'x-api-key': 'a0f726fe-78bf-4e30-b0a3-422e28ee4f79'}
    response = requests.request("GET", url, headers=headers, params=query)
    data = json.loads(response.text)
    return render_template('index.html', data = data)
    