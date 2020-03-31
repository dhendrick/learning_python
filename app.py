from flask import Flask, send_from_directory

app = Flask(__name__)
print(__name__)

@app.route('/')
def home_page():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=True, debug=True)
