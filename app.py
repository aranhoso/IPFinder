from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    ip = None
    location = None

    if request.method == 'POST':
        ip_with_port = request.form.get('ip')
        ip = ip_with_port.split(':')[0]
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        location = response.json()

    return render_template('index.html', ip=ip, location=location)


if __name__ == "__main__":
    app.run(debug=True)
