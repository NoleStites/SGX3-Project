from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!\n"

@app.route('/<name>', methods=['GET'])
def hello_name(name):
    return f'Hello, {name}!\n'

# Get parameters out of the URL
# Ex: http://35.206.76.195:8071/hello?name=John&favnum=16
@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name')
    number = request.args.get('favnum')
    return f'Hello, {name}!\nYour favourite number is {number}.\n'


# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8071)
