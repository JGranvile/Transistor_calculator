from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

def calcular_transistor(vcc, rc, rb, beta):
    # Cálculos simplificados das correntes e tensões do transistor
    vbe = 0.7  # Tensão base-emissor típica
    ib = (vcc - vbe) / rb
    ic = beta * ib
    vc = vcc - ic * rc
    ve = 0
    vb = ve + vbe

    return {
        'ib': ib,
        'ic': ic,
        'vc': vc,
        've': ve,
        'vb': vb
    }

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('calcular_transistor')
def handle_calculate(data):
    vcc = float(data['vcc'])
    rc = float(data['rc'])
    rb = float(data['rb'])
    beta = float(data['beta'])

    resultados = calcular_transistor(vcc, rc, rb, beta)
    socketio.emit('resultado_transistor', resultados)

if __name__ == '__main__':
    socketio.run(app, debug=True)
