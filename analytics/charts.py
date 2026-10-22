import pandas as pd

# I just learned five important Pandas concepts in one function:
#
# ✅ value_counts()
# ✅ pd.cut()
# ✅ sort_index()
# ✅ .index
# ✅ .values
# ✅ .tolist()

#  value_counts() to count listings in each room type.
#means value_count is used to count unique element means room type mein 4 types hain
#so un vo4 unique hue toh 62000 mein se kitne konse hain vo count kar dega
# .tolist() Converts Pandas objects to Python lists for Chart.js.




def average_price_by_room_type(df):

    grouped = df.groupby("room_type")
    price = grouped["price"].mean()

    price = price.round(2)
    price = price.sort_values(ascending=False)

    return {
        "labels": price.index.tolist(),
        "values": price.values.tolist()
    }

# Uses pd.cut() to group prices into custom ranges.
def price_distribution(df):
    bins = [0, 50, 100, 150, 200, 300, 500, 1000, float("inf")]
    labels = [
        "$0-50",
        "$50-100",
        "$100-150",
        "$150-200",
        "$200-300",
        "$300-500",
        "$500-1000",
        "$1000+"
    ]
    price_bins = pd.cut(
        df["price"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    counts = price_bins.value_counts().sort_index()

    return {
        "labels": counts.index.tolist(),
        "values": counts.values.tolist()
    }



def revenue_by_bedrooms(df):

    grouped = df.groupby("bedrooms")
    revenue = grouped["estimated_revenue_l365d"].mean()
    revenue = revenue.round(2)
    revenue = revenue.sort_index()
    revenue = revenue[(revenue.index <= 7) & (revenue.index >= 1)]

    labels = []

    for i in revenue.index:
        if i == 1:
            labels.append("1 Bedroom")
        else:
            labels.append(f"{int(i)} Bedrooms")

    return {
        "labels": labels,
        "values": revenue.values.tolist()
    }


def listings_by_room_type(df):
    counts=df["room_type"].value_counts()
    return{
        "labels": counts.index.tolist(),
        "values": counts.values.tolist()
    }

def top_5_revenue_listings(df):
    top = df.sort_values("estimated_revenue_l365d", ascending=False).head(5)



    labels = []

    for index, row in top.iterrows():
        labels.append(
            f"{row['room_type']} • {int(row['bedrooms'])} BR"
        )

    return {
        "labels": labels,
        "values": top["estimated_revenue_l365d"].round(2).tolist()
    }


#study diff between using and not using orient="records"
def heat_map(df):
    return df[["latitude","longitude","price"]].to_dict(orient="records")

def competitor_map(df):
    return df[
        [
            "latitude",
            "longitude",
            "price",
            "room_type",
            "bedrooms",
            "bathrooms",
            "accommodates"
        ]
    ].to_dict(orient="records")