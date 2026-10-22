from encodings import undefined

import pandas as pd
from pandas import read_csv

from analytics.charts import *
from analytics.kpi import *
from analytics.filters import *
from analytics.models import *
from flask import Flask,request,jsonify

app = Flask(__name__)

def get_dataframe():

    city = request.args.get("city")

    if city == "Paris":
        return pd.read_csv("data/paris.csv")

    elif city == "Amsterdam":
        return pd.read_csv("data/amsterdam.csv")

    elif city == "Newyork":
        return pd.read_csv("data/newyork.csv")

    else:
        return pd.read_csv("data/london.csv")
#"When someone visits /, run the function below."
@app.route("/")
def home():
    return "app is working"


@app.route("/filters")
def filters():
    df = get_dataframe()

    filtered_df = df.copy()

    return jsonify({
        "filtersdata": {
            "city": sorted(df["city"].unique().tolist()),
            "neighbourhood": sorted(filtered_df["neighbourhood_cleansed"].unique().tolist())
        }
    })

@app.route("/overview")
def overview():
    df = get_dataframe()

    filtered_df = apply_filters(df, request.args)

    return jsonify({

        "kpis": {
            "total_listings": total_listings(filtered_df),
            "average_price": average_price(filtered_df),
            "median_price": median_price(filtered_df),
            "average_reviews": average_reviews(filtered_df),
            "occupancy_rate": occupancy_rate(filtered_df),
            "revenue_potential": revenue_potential(filtered_df)
        },

        "charts": {
            "price_distribution": price_distribution(filtered_df),
            "average_price_by_room_type": average_price_by_room_type(filtered_df),
            "listings_by_room_type": listings_by_room_type(filtered_df),
            "revenue_by_bedrooms": revenue_by_bedrooms(filtered_df),
            "top_5_revenue_listings": top_5_revenue_listings(filtered_df)
        }

    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    #  request.get_json() converts that JSON request into a Python dictionary.
    price_df = pd.DataFrame([data["priceData"]])
    occupancy_df = pd.DataFrame([data["occupancyData"]])
    predicted_price = predict_price(price_df)[0]
    return jsonify({
        "predicted_price":float(predicted_price),
        "predicted_occupancy": int(predict_occupancy(occupancy_df))
    }
    )



# Run server
if __name__ == "__main__":
    app.run(debug=True)