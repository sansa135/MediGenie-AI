import joblib
import numpy as np

model = joblib.load('models/medical_model.pkl')
encoder = joblib.load('models/label_encoder.pkl')
symptom_columns = joblib.load('models/symptom_columns.pkl')


def predict_disease(user_symptoms):

    input_data = [0] * len(symptom_columns)

    for symptom in user_symptoms:

        symptom = symptom.strip().lower()

        if symptom in symptom_columns:

            index = symptom_columns.index(symptom)

            input_data[index] = 1

    input_array = np.array(input_data).reshape(1, -1)

    prediction = model.predict(input_array)

    disease = encoder.inverse_transform(prediction)

    return disease[0]