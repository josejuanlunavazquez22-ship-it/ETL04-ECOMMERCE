import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    # 1. Filtrar por estado de pago, descartar pedidos no COMPLETED
    df = df[df["payment.status"].astype(str).str.upper() == "COMPLETED"].copy()

    # 2. Sanitización de precios sucios (asegurando el tipo str primero)
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace("USD", "", regex=False)
        .str.strip()
    )

    # 3. Castear los datos a tipos numéricos y temporales
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0)
    df["discount"] = pd.to_numeric(df["discount"], errors="coerce").fillna(0.0)

    # Filtrar registros que hayan quedado con precio nulo o inválido
    df = df[df["price"].notnull() & (df["price"] > 0)].copy()

    # 4. Cálculo de subtotal bruto
    df["subtotal_gross"] = df["price"] * df["quantity"]

    # 5. Cálculo de total neto
    df["total_net"] = df["subtotal_gross"] * (1 - df["discount"])

    # 6. Renombrar y seleccionar columnas finales
    df_final = df.rename(
        columns={
            "customer.customer_id": "customer_id",
            "customer.country": "country",
            "payment.method": "payment_method",
            "payment.status": "status",
        }
    )

    df_final = df_final[
        [
            "order_id",
            "country",
            "payment_method",
            "product_id",
            "price",
            "quantity",
            "discount",
            "subtotal_gross",
            "total_net",
        ]
    ].copy()

    return df_final