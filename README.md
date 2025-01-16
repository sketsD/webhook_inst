# Flask Webhook with ngrok

This repository provides a simple Flask application for handling Facebook/Instagram webhooks. It also includes instructions to set up `ngrok` for local testing.

## Prerequisites

- Python 3.7+
- [ngrok](https://ngrok.com/) installed

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sketsD/webhook_inst.git
   cd webhook_inst
   ```

2.Install dependencies:
pip install -r requirements.txt

3.Start the Flask application:
python main.py

4.Start ngrok to expose the local server (install ngrok for your machine https://dashboard.ngrok.com/get-started/setup/windows and get your authtoken):
ngrok http http://localhost:8080

5.Note the public URL provided by ngrok. For example:
https://d76c-84-117-7-20.ngrok-free.app

6.Set up the webhook in the Facebook App:

Go to Meta for Developers dashboard.
Under Webhooks, add your ngrok URL (e.g., https://d76c-84-117-7-20.ngrok-free.app/webhook) as the webhook callback URL.
Add the your_verify_token specified in main.py (VERIFY_TOKEN).

7.Manage and test Webhooks:
Select webhooks to test and subscribe to it.
