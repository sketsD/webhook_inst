from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = "your_verify_token_here"

# Проверка токена для валидации вебхука
@app.route('/webhook', methods=['GET'])
def verify_webhook():
    print(request.headers)
    print(request.get__json())
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    if token == VERIFY_TOKEN:
        print("Проверка токена прошла успешно")
        return challenge, 200
    return "Forbidden", 403

# Обработка входящих данных
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    print(data)
    if data:
        print("Получено событие:", data)
        # Здесь можно добавить обработку входящих сообщений
        for entry in data.get('entry', []):
            for messaging_event in entry.get('messaging', []):
                print("Событие Direct Messages:", messaging_event)
    return "EVENT_RECEIVED", 200

if __name__ == "__main__":
    app.run(port=8080, debug=True)
