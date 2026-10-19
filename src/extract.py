import pandas as pd
import json

def extract_data(df):

    with open(df, 'r', encoding='utf-8') as f:
        data = json.load(f)

    df_final = pd.json_normalize(
        data,
        record_path="items",
        meta=[
            "order_id",
            "timestamp",
            ["customer", "customer_id"],
            ["customer", "country"],
            ["payment", "method"],
            ["payment", "status"]

        ],
        errors="ignore"
    )
    return df_final
