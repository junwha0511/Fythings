from flask import Flask, send_file, request
import os
import base64

app = Flask(__name__)

@app.route('/')
def main():
    return 'server is initiated'

@app.route('/image1')
def returnImage1():
    return send_file('C:/b1.png')


@app.route('/image2')
def returnImage2():
    return send_file('C:/b2.png')

    
@app.route('/image3')
def returnImage3():
    return send_file('C:/b3.png')

    
@app.route('/image4')
def returnImage4():
    return send_file('C:/b4.png')

    
@app.route('/image5')
def returnImage5():
    return send_file('C:/b5.png')

@app.route('/upload',methods=['POST'])
def uploadImage():
    if request.method == 'POST':
        encodedFile = request.form['file']
        number = request.form['number']
        
        with open('C:/b'+number+'.png', 'wb') as f:
            f.write(base64.decodebytes(encodedFile.encode()))
            f.close()
    return 'succeed'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

