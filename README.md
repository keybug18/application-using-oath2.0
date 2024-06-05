# application-using-oath2.0
This code demonstrates a basic implementation of OAuth 2.0 Authorization Code Flow using the Flask web framework in Python.
# Flask OAuth 2.0 Demo

This repository contains a basic implementation of OAuth 2.0 Authorization Code Flow using the Flask web framework in Python. The application demonstrates how to authenticate users via an OAuth provider and access their profile information.

## Features

- OAuth 2.0 Authorization Code Flow
- Securely obtain and use access tokens
- Display user profile information

## Prerequisites

- Python 3.x
- Flask
- Requests library

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/flask-oauth2-demo.git
    cd flask-oauth2-demo
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up OAuth credentials:**

    Register your application with your OAuth provider to obtain the Client ID and Client Secret. Then, create a `.env` file in the root directory and add your credentials:

    ```env
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    REDIRECT_URI=http://localhost:5000/callback
    AUTHORIZATION_BASE_URL=https://provider.com/oauth/authorize
    TOKEN_URL=https://provider.com/oauth/token
    USER_INFO_URL=https://provider.com/userinfo
    ```

## Running the Application

1. **Run the Flask application:**

    ```bash
    flask run
    ```

2. **Visit the home page:**

    Open your web browser and go to `http://localhost:5000/`. You should see a welcome message with a link to log in using OAuth 2.0.

3. **Log in and authorize:**

    Click the "Login with OAuth 2.0" link. You will be redirected to the OAuth provider's login page. After logging in and authorizing the application, you will be redirected back to your application.

4. **View user profile:**

    After successful authorization, you will be redirected to the profile page where you can see your user profile information.




