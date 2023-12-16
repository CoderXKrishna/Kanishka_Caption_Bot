from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'VJBotz'


if __name__ == "__main__":
    app.run()

# Don't Remove Credit @Mr_Mrs_Krishna
# Ask Doubt on telegram @Mr_Mrs_Krishna
