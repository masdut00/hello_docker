from flask import Flask

app = Flask(__name__)

@app.get('/')
def route_hello():
    return 'Hello World'

app.run(host='0.0.0.0', port=8081)