from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
import os
import logging

path_ecommerce = os.path.join("data", "raw", "orders_payload.json")
path_data_clean = os.path.join("data", "processed", "ecommerce_final.csv")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Inicio de pipeline...")

    logging.info("Proceso de extraccion...")
    df_extract = extract_data(path_ecommerce)

    logging.info("Proceso de transformacion...")
    df_transform = transform_data(df_extract)

    logging.info("Proceso de carga...")
    print(df_transform)
    load_data(df_transform, path_data_clean)

if __name__ == "__main__":
    main()


