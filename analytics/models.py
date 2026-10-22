from joblib import load

prediction_model=load("models/price_prediction_model.joblib")
occupancy_model=load("models/occupancy_model.joblib")

def predict_price(df):
    return prediction_model.predict(df)

def predict_occupancy(df):
    return occupancy_model.predict(df)[0]