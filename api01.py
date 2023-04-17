from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/Ac2', methods = ['GET'])
def main():
    return jsonify (nome = 'David', sobrenome = 'Belissimo', ra = '2201593')

if __name__ == '__main__':
    app.run(port=5000, debug= True)