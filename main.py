from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = "your_verify_token"

# Checking the token for webhook validation
@app.route('/webhook', methods=['GET'])
def verify_webhook():

    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if token == VERIFY_TOKEN:
        print("Token verification was successful")
        return challenge, 200
    return "Forbidden", 403

# Processing incoming data
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()

    if data:
        print("Received event:", data)
        # Here you can add processing of incoming messages
        for entry in data.get('entry', []):
            for messaging_event in entry.get('messaging', []):
                print("Event Direct Messages:", messaging_event)
    return "EVENT_RECEIVED", 200

if __name__ == "__main__":
    app.run(port=8080, debug=True)
