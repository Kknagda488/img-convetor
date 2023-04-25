from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>this is img editor</h1>"

if __name__ =="__main__":
    app.run(debug=True)