from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/add/<int:a>/<int:b>')

def add(a,b):

    result = a+b

    return jsonify({

        "num1": a,
        "num2": b,
        "result": result
    })

app.run(host="0.0.0.0", port=5000)