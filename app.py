
from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
  return render_template("intro.html")
@app.route('/index.html')
def map():
    return render_template("index.html")
if __name__ == '__main__':
  app.run(host="192.168.0.16", port=8080)