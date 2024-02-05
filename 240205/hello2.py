from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
  return 'Hello world'

@app.route('/about')
def about():
  return 'This is about page'

@app.route('/contact')
def contact():
  return 'This is contack page'

if __name__ == '__main__':
  app.run(debug=True, port=80, host='0.0.0.0')
