import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import datetime

df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])

df_grouped = df.groupby("date")["sales"].sum().reset_index()

fig = px.line(
    df_grouped,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)

fig.add_vline(
    x=datetime.datetime(2021, 1, 15).timestamp() * 1000,
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase",
    annotation_position="top right"
)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Pink Morsel Sales Visualiser",
        style={"textAlign": "center", "color": "#d63384", "fontFamily": "Arial"}
    ),
    html.H3(
        "Were sales higher before or after the Pink Morsel price increase on 15 Jan 2021?",
        style={"textAlign": "center", "color": "#666", "fontFamily": "Arial"}
    ),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)