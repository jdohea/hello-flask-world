from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
        # Get the UTM parameters from the query string
    token = request.args.get('accessToken')

    return 'Web App with Python Flask! - ' + token

app.run(host='0.0.0.0', port=80)
