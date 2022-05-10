import uvicorn ##ASGI
from fastapi import FastAPI
# from scipy.stats import mode
from Input import Input
import numpy as np
import pickle
from Model1 import *

# import pickle
# 2. Create the app object
app = FastAPI()

# pickle_in = open("data_dict.pkl","rb")
# data_dict=pickle.load(pickle_in)

# pickle_in = open("final_nb_model.pkl","rb")
# final_nb_model=pickle.load(pickle_in)

# pickle_in = open("final_rf_model.pkl","rb")
# final_rf_model=pickle.load(pickle_in)

# pickle_in = open("final_svm_model.pkl","rb")
# final_svm_model=pickle.load(pickle_in)

# Defining the Function
# Input: string containing symptoms separated by commmas
# Output: Generated predictions by models

# def PredictDisease(symptoms):
#     symptoms = symptoms.split(",")

#     # creating input data for the models
#     input_data = [0] * len(data_dict["symptom_index"])
#     for symptom in symptoms:
#         index = data_dict["symptom_index"][symptom]
#         input_data[index] = 1

#     # reshaping the input data and converting it
#     # into suitable format for model predictions
#     input_data = np.array(input_data).reshape(1, -1)

#     # generating individual outputs
#     rf_prediction = data_dict["predictions_classes"][final_rf_model.predict(input_data)[
#         0]]
#     nb_prediction = data_dict["predictions_classes"][final_nb_model.predict(input_data)[
#         0]]
#     svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[
#         0]]

#     # making final prediction by taking mode of all predictions
#     final_prediction = mode(
#         [rf_prediction, nb_prediction, svm_prediction])[0][0]
#     predictions = {
#         "rf_model_prediction": rf_prediction,
#         "naive_bayes_prediction": nb_prediction,
#         "svm_model_prediction": nb_prediction,
#         "final_prediction": final_prediction
#     }
#     return predictions


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To RGS HealthCare': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data:Input):
    data = data.dict()
    s1=data['s1']
    s2=data['s2']
    s3=data['s3']
    s4=data['s4']
    res = ''
    if s1 != "" :
        res+=s1+","
    if s2 != "" :
        res+=s2+","
    if s3 != "" :
        res+=s3+","
    if s4 != "" :
        res+=s4
    
    predict = PredictDisease(res)
    print(predict)
    return {
        'prediction': predict
    }
    

  
    
# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn main:app --reload