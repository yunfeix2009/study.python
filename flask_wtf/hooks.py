from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    print("hello world")
    return 'Hello World!'
@app.before_first_request
def before_first_request():
    print('before_first_request')
@app.before_request
def before_request():
    print('before_request')
@app.after_request
def after_request(response):
    print('after_request')
    print(response)
    return response
@app.teardown_request
def teardown_request(error):
    print('teardown_request:error %s' % error)
if __name__=='__main__':
    app.run(debug=True)