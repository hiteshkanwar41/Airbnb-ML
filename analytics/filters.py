import pandas as pd

def filter_city(df, city):
    result = df[df["city"] == city]
    return result


def filter_neighbourhood(df, neighbourhood):
    return df[df["neighbourhood_cleansed"] == neighbourhood]


def filter_room_type(df, room_type):
    return df[df["room_type"] == room_type]



def apply_filters(df, request_args):

    filtered_df = df.copy()


    if "neighbourhood" in request_args and request_args["neighbourhood"]!="":
        filtered_df = filter_neighbourhood(
            filtered_df,
            request_args["neighbourhood"]
        )

    return filtered_df