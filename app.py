from flask import Flask, request, jsonify
import pandas as pd
import pickle
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
ct = pickle.load(open('column_transformer.pkl', 'rb'))
sc = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return "Welcome to the Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.json  # Expecting a single customer record as a dictionary
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Convert the input data to a DataFrame with a single row
        try:
            df = pd.DataFrame([data])  # Wrap the dictionary in a list to create a single-row DataFrame
        except Exception as e:
            return jsonify({'error': f'Error creating DataFrame: {str(e)}'}), 400

        # Ensure required columns are present
        required_columns = ['Status', 'Rating', 'Source', 'Revenue', 'Number of Employees']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            return jsonify({'error': f'Missing columns: {missing_columns}'}), 400

        # Transform the data using the saved ColumnTransformer
        try:
            X = df.drop(columns=['Name', 'Company'])
            X = ct.transform(X)
        except Exception as e:
            return jsonify({'error': f'Error transforming data: {str(e)}'}), 500

        # Standardize the data using the saved StandardScaler
        try:
            X = sc.transform(X)
        except Exception as e:
            return jsonify({'error': f'Error scaling data: {str(e)}'}), 500

        # Make predictions
        try:
            prediction = model.predict(X)[0]  # Get the single prediction
        except Exception as e:
            return jsonify({'error': f'Error making predictions: {str(e)}'}), 500

        # Prepare the response
        response = {
            'Prediction': prediction
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)