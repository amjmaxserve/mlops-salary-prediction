from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load('../model/salary_model.pkl')
label_encoders = joblib.load('../model/label_encoders.pkl')
target_encoder = joblib.load('../model/target_encoder.pkl')

@app.route('/')
def home():
    return "ML Salary Prediction API Running"

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    education = label_encoders['education'].transform([
        data['education']
    ])[0]

    occupation = label_encoders['occupation'].transform([
        data['occupation']
    ])[0]

    input_data = pd.DataFrame([{
        'age': data['age'],
        'education': education,
        'hours_per_week': data['hours_per_week'],
        'occupation': occupation,
        'experience': data['experience']
    }])

    prediction = model.predict(input_data)

    result = target_encoder.inverse_transform(prediction)

    return jsonify({
        'prediction': result[0]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)