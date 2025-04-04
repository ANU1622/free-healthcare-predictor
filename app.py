import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle
#create flask app
app=Flask(__name__,template_folder="templates")

#load pickle model
with open('model.pkl','rb') as file:
    model=pickle.load(file)
print("loaded model type:",type(model))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    float_features=[float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    prediction=model.predict(features)
    if prediction == 0:
        text = "Person has not utilized free care check"
    else:
        text = "Person has utilized free care check"
    return render_template("index.html", prediction_text=text)

if __name__=="__main__":
    app.run(debug=True)