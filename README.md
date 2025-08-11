🏠 Linear Regression House Price Prediction
📌 Project Overview
This project is a Machine Learning web application built using Flask for the backend and HTML/CSS for the frontend.
It predicts house prices based on input features like the number of rooms, area, location, and other parameters using a Linear Regression model.

The model is trained on a sample housing dataset and integrated into a Flask web app, allowing users to enter details in a form and get the predicted price instantly.

Project Structure
house_price_prediction/
│
├── static/
│   ├── style.css         # CSS styling for the frontend
│
├── templates/
│   ├── index.html        # Input form page
│   ├── result.html       # Output prediction page
│
├── model/
│   ├── house_price_model.pkl  # Trained Linear Regression model
│
├── app.py                # Flask application
├── train_model.py        # Script to train and save the model
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation


⚙️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/yourusername/house_price_prediction.git
cd house_price_prediction

2️⃣ Create a Virtual Environment
python -m venv venv
Activate the environment:

Windows:
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Train the Model
python train_model.py

5️⃣ Run the Flask App

python app.py
The app will run on http://127.0.0.1:5000/
