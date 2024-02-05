from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index1.html')

@app.route('/about')
def about():
  return 'This is about page'

@app.route('/contact')
def contact():
  return 'This is contack page'

if __name__ == '__main__':
  app.run(debug=True, port=80, host='0.0.0.0')
