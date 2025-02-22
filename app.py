from flask import Flask
import os

import datetime

app = Flask(__name__)

def get_top_output():
    try:
        return os.popen("top").read()
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return 'Welcome to flask app built by @imshanu28, please go to /htop route to see top data.'

@app.route('/htop')
def htop():
    name = "Shanu Kumar"
    username = os.getenv("USER") or os.getenv("iamshanu28") or "Unknown"
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = get_top_output().replace("\n", "<br>")

    return f"""
    <html>
    <head><title>HTOP Endpoint</title></head>
    <body>
        <h2>Name: {name}</h2>
        <h2>Username: {username}</h2>
        <h2>Server Time (IST): {server_time}</h2>
        <h3>Top Output:</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)