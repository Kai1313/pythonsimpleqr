from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
import datetime, time
from PIL import Image
from qrgenerator import qrgenerator

app = Flask(__name__, static_folder='templates/')
bootstrap = Bootstrap(app)

def qrCreate(typed):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    qr_name = "templates/assets/"+timestamp+".png"
    qrgenerator(typed, qr_name)
    time.sleep(3)
    # Display the QR code image
    # qr_image.show()
    return qr_name

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/phone')
def phone():
    return render_template('phone.html')

@app.route('/qrcode', methods=['POST'])
def qrcode():
    data = request.get_json()
    # Process the data
    qr = qrCreate(data.get('val'))
    response_data = {'message': 'AJAX request received', 'data': qr}
    return jsonify(response_data)
    # return render_template('index.html', qr=qr)

if __name__ == '__main__':
    # Bind Flask to your machine's IP address and port 5000
    app.run(host='0.0.0.0', port=5000)