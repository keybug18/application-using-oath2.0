from flask import Flask, redirect, request, session, url_for
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'http://localhost:5000/callback'
authorization_base_url = 'https://provider.com/oauth/authorize'
token_url = 'https://provider.com/oauth/token'
scope = 'YOUR_SCOPES'

@app.route('/')
def home():
    return 'Welcome to the OAuth 2.0 demo! <a href="/login">Login with OAuth 2.0</a>'

@app.route('/login')
def login():
    return redirect(f"{authorization_base_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}")

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_response = requests.post(token_url, data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
    })
    token_json = token_response.json()
    session['oauth_token'] = token_json['access_token']
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    token = session['oauth_token']
    user_info = requests.get('https://provider.com/userinfo', headers={
        'Authorization': f'Bearer {token}'
    })
    return user_info.json()

if __name__ == '__main__':
    app.run(debug=True)
