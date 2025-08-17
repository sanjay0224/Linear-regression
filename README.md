Linear Regression House Price Prediction
Project Overview

This is a Machine Learning Web Application built using Flask (backend) and HTML/CSS (frontend).
It predicts house prices based on input features such as:

Number of rooms

Area (sq. ft.)

Location

Other parameters

The prediction is powered by a Linear Regression model trained on a sample housing dataset.
Users can enter details in a form, and the app instantly returns the predicted house price.

Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/house_price_prediction.git
cd house_price_prediction

2. Create a Virtual Environment
python -m venv venv


Activate the environment:

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Train the Model
python train_model.py


This will generate house_price_model.pkl inside the model/ folder.

5. Run the Flask App
python app.py


The app will be available at: http://127.0.0.1:5000/

Features

User-friendly web interface

Instant predictions using Linear Regression

Modular structure for easy updates

Extendable with other ML models

Screenshots

<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/8ef1a9f5-ed76-4359-90f4-362045f3a535" />

Future Enhancements

Add support for multiple ML algorithms (Random Forest, XGBoost, etc.)

Integrate a database for storing past predictions

Deploy on Heroku, Vercel, or AWS

Add visualizations of prediction confidence

Tech Stack

Python 3.x

Flask (Web Framework)

Scikit-learn (Machine Learning)

Pandas, NumPy (Data Handling)

HTML, CSS (Frontend)
