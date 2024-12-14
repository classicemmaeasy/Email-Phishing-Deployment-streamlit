import pandas as pd
from fastapi import FastAPI
import pickle
from data_model import Phish  # Pydantic model

app = FastAPI(
    title="Phishing mail prediction",
    description="Predicting phishing emails"
)


with open(r"C:/Users/HP/Documents/Email Phishing/RF.pkl", "rb") as f:
    model = pickle.load(f)

with open(r"C:/Users/HP/Documents/Email Phishing/vect.pkl", "rb") as e:
    vectorizer = pickle.load(e)

@app.get('/')
def getit():
    return {"message": "Welcome to the Phishing mail app"}

@app.post('/predict')
def model_predict(phish: Phish):
    # Extract the email text from the Pydantic object
    email_text = [phish.Email_Text]  # List of strings for vectorizer.transform()

    # Transform the input text using the loaded vectorizer
    transformed_text = vectorizer.transform(email_text)

    # Perform the prediction
    pred = model.predict(transformed_text)

    # Return a response based on the prediction
    if pred[0] == 1:
        return {"prediction": "legitimate mail"}
    else:
        return {"prediction": "phishing mail"}







# import pandas as pd 
# from fastapi import FastAPI
# import pickle
# from sklearn.feature_extraction.text import TfidfVectorizer
# from data_model import Phish

# app=FastAPI(
#     title="Phishing mail prediction",
#     description="Predicting water Portability"
#     )

# with open(r"C:\Users\HP\Documents\phishing mail\RF.pkl","rb") as f:
#     model=pickle.load(f)

# with open(r"C:\Users\HP\Documents\phishing mail\vect.pkl","rb") as e:
#     vectorizer=pickle.load(e)

# @app.get('/')

# def getit():
#     return "welcome to the Phishing mail app"


# @app.post('/predict')

# def model_predict(phish:Phish):
#     sample=pd.DataFrame({
#         'Email_Text': [phish.Email_Text],
#     })

#     tansdata=vectorizer.transform([sample])

#     pred=model.predict(tansdata)

#     if pred == 1:
#       return "legitimate mail"
#     else:
#        return "phishing mail"