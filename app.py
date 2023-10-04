import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd
import requests

#Create an app object using the Flask class. 
app = Flask(__name__)
model = pickle.load(open('model/model1.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
#Load the trained model. (Pickle file)
@app.route("/predict", methods=['POST'])
#Define the route to be home. 

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        date = str(request.form['dates'])
        n_sick = int(request.form['Number of sick driver'])
        calls = int(request.form['Number of calls'])
        n_duty = int(request.form['Number of drivers on duty'])
        dafted=  int(request.form['Dafted'])

        data={'date':pd.to_datetime(date),'n_sick':n_sick , 'calls':calls ,'n_duty':n_duty, 'dafted':dafted}

        df = pd.DataFrame(data,index=['date'])
        df = df.set_index('date')
        new_input = df
# get prediction for new input
        output = model.predict(new_input)
        output = output.round()
        output = output.astype(int)


    #int_features = [float(x) for x in request.form.values()] #Convert string inputs to float.
    #features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
    #prediction = model.predict(features)  # features Must be in the form [[a, b]]

        return render_template('index.html', prediction_text='Number of standby rescue drivers needed:{}'.format(output))
if __name__=="__main__":
    app.run(debug=True)