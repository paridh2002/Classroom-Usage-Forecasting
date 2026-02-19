import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

from data_processor import load_data
from forecast_model import train_forecast

df = load_data()
forecast = train_forecast(df)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Classroom Usage Forecast"),

    dcc.Graph(
        id="usage-chart",
        figure=px.line(df, x="date", y="usage", title="Usage History")
    ),

    dcc.Graph(
        id="forecast-chart",
        figure=px.line(forecast, x="date", y="usage", title="30-Day Forecast")
    )
])

if __name__ == "__main__":
    app.run(debug=True)
