import uvicorn ##ASGI
from fastapi import FastAPI
from Input import Input

from Model1 import PredictDisease
# import pickle
# 2. Create the app object
app = FastAPI()
# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)



# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Krish Youtube Channel': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_banknote(data:Input):
    data = data.dict()
    s1=data['s1']
    s2=data['s2']
    s3=data['s3']
    s4=data['s4']
    predict =PredictDisease(s1+s2+s3+s4)
    return {
        'prediction': predict["final_prediction"]
    }
    
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
  
    
# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn main:app --reload