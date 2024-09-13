# from flask import Flask, request, render_template
# import joblib
# import re
# from scipy.sparse import hstack

# # Initialize the Flask application
# app = Flask(__name__)

# # Load the model and the TF-IDF objects
# model = joblib.load('Fake_news_predictor.pkl')
# tfidf_title = joblib.load('tfidf_title.pkl')
# tfidf_text = joblib.load('tfidf_text.pkl')

# # Define a function for processing text
# def text_processing(text):
#     if isinstance(text, str):
#         text = text.lower()
#         text = re.sub(r'http\S+|https\S+|www\S+', '', text)  # Remove URLs
#         text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
#         text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation marks
#         text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespaces
#     return text

# # Define the home route to render the form
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Define the prediction route
# @app.route('/predict', methods=['POST'])
# def predict():
#     title = request.form['title']
#     text = request.form['text']

#     # Process the input text
#     new_title = text_processing(title)
#     new_text = text_processing(text)

#     # Transform the input using the loaded TF-IDF vectorizers
#     new_title_tfidf = tfidf_title.transform([new_title])
#     new_text_tfidf = tfidf_text.transform([new_text])

#     # Combine the title and text vectors
#     new_data_combined = hstack([new_title_tfidf, new_text_tfidf])

#     # Predict using the loaded model
#     prediction = model.predict(new_data_combined)

#     # Output the result
#     if prediction[0] == 0:
#         result = "The news is classified as REAL."
#     else:
#         result = "The news is classified as FAKE."

#     return render_template('index.html', prediction_text=result)

# if __name__ == "__main__":
#     app.run(debug=True)
# app.py
from flask import Flask, render_template, request
import joblib
from scipy.sparse import hstack
import re

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model and transformers
model = joblib.load('Fake_news_predictor.pkl')
tfidf_title = joblib.load('tfidf_title.pkl')
tfidf_text = joblib.load('tfidf_text.pkl')

# Text processing function
def text_processing(text):
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'http\S+|https\S+|www\S+', '', text)  # Remove URLs
        text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespaces
    return text

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    title = request.form['title']
    text = request.form['text']
    new_title = text_processing(title)
    new_text = text_processing(text)
    new_title_tfidf = tfidf_title.transform([new_title])
    new_text_tfidf = tfidf_text.transform([new_text])
    new_data_combined = hstack([new_title_tfidf, new_text_tfidf])
    prediction = model.predict(new_data_combined)
    
    result = "REAL" if prediction[0] == 0 else "FAKE"
    
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
