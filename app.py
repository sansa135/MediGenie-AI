from flask import Flask, render_template, request, jsonify

from services.prediction_service import predict_disease

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict')
def predict_page():
    return render_template('predict.html')


@app.route('/predict-disease', methods=['POST'])
def predict_disease_route():

    symptoms = request.form['symptoms']

    symptom_list = symptoms.split(',')

    result = predict_disease(symptom_list)

    return jsonify({
        'disease': result
    })


if __name__ == '__main__':
    app.run(debug=True)
