# import os
# import pandas as pd
#
# DATA_FOLDER = "data"
#
# for filename in os.listdir(DATA_FOLDER):
#
#     # Process only cleaned CSVs (ignore .gz files)
#     if filename.endswith(".csv") and filename != "listings.csv":
#
#         filepath = os.path.join(DATA_FOLDER, filename)
#
#         # City name = filename without .csv
#         city = os.path.splitext(filename)[0]
#
#         df = pd.read_csv(filepath)
#
#         # Create/replace city column
#         df["city"] = city.capitalize()
#
#         df.to_csv(filepath, index=False)
#
#         print(f"✅ Updated {filename} -> city = {city.capitalize()}")
#
# print("\n🎉 All files updated successfully!")

from joblib import load

model = load("models/price_prediction_model.joblib")
import pandas as pd

sample = pd.DataFrame({
    "city": ["London"],
    "neighbourhood_cleansed": ["Westminster"],
    "room_type": ["Entire home/apt"],
    "accommodates": [4],
    "bathrooms": [1.0],
    "bedrooms": [2],
    "beds": [2],
    "longitude": [-0.1357],
    "latitude": [51.5074]
})

prediction_price = model.predict(sample)


print(f"Predicted Price: £{prediction_price[0]:.2f}")