from flask import Flask, request, jsonify
import random
import anonymize

app = Flask(__name__)

APT_SECRET='aws'

@app.route('/anonymize', methods=['POST'])
def get_anonymize():
    auth_header = request.headers.get('Authorization')
    if auth_header != 'Bearer %s' % APT_SECRET:
        return {"msg": "Invalid Authorization header"}, 403
    message = request.json.get('message', None)
    if message is None:
        return jsonify({
            'status': 'error',
            'errorInfo': 'No message provided',
            'data': None
        })
    result = anonymize.handle(message)
    return result    

@app.route('/weather', methods=['POST'])
def get_weather():
    auth_header = request.headers.get('Authorization')
    if auth_header != 'Bearer hanfangyuan':
        return {"msg": "Invalid Authorization header"}, 403
    city = request.json.get('city', None)
    if city is None:
        return jsonify({
            'status': 'error',
            'errorInfo': 'No city provided',
            'data': None
        })

    # 随机生成温度，风速和风向
    temperature = f'{random.randint(10, 20)}℃'
    windspeed = f'{random.randint(1, 5)}级' 
    winddirect = random.choice(['北风', '南风', '西风', '东风'])  # 随机选择风向
    # 返回JSON格式的响应
    # return jsonify({
    #     'status': 'OK',
    #     'errorInfo': None,
    #     'data': {
    #         'city': city,
    #         'temp': temperature,
    #         'windspeed': windspeed,
    #         'winddirect': winddirect
    #     }
    # })
    # 返回对LLM友好的字符串格式的响应
    return f"{city}今天是晴天，温度{temperature}, 风速{windspeed}, 风向{winddirect}"

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False, port=4397)