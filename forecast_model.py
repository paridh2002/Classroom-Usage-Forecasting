import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def train_forecast(df):
    # Work on a copy so original df is not modified
    df_copy = df.copy()
    df_copy.set_index("date", inplace=True)

    model = ExponentialSmoothing(
        df_copy["usage"],
        seasonal="add",
        seasonal_periods=7
    )

    fit = model.fit()
    forecast_values = fit.forecast(30)

    forecast_df = forecast_values.reset_index()
    forecast_df.columns = ["date", "usage"]

    return forecast_df
