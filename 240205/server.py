from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello Flask!"

if __name__ == "__main__":
  app.run(host = "192.168.0.143", port = "8080")
