from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

locations = ['Coimbatore', 'Chennai', 'Madurai', 'Bangalore']
history = []

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            area = float(request.form['area'])
            bedrooms = int(request.form['bedrooms'])
            bathrooms = int(request.form['bathrooms'])
            location = request.form['location']
            
            input_df = pd.DataFrame([[area, bedrooms, bathrooms, location]],
                                    columns=['Area', 'Bedrooms', 'Bathrooms', 'Location'])
            
            prediction = round(model.predict(input_df)[0], 2)
            history.append({
                "area": area,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "location": location,
                "price": prediction
            })
        except:
            prediction = "Invalid Input!"
    
    return render_template("index.html", prediction=prediction, locations=locations, history=history)

if __name__ == '__main__':
    app.run(debug=True)
