import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import datetime

# Load data
df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([

    # Header
    html.H1(
        "🍬 Pink Morsel Sales Visualiser",
        style={
            "textAlign": "center",
            "color": "white",
            "backgroundColor": "#d63384",
            "padding": "20px",
            "margin": "0",
            "fontFamily": "Arial",
            "letterSpacing": "2px"
        }
    ),

    html.H3(
        "Were sales higher before or after the price increase on 15 Jan 2021?",
        style={
            "textAlign": "center",
            "color": "#d63384",
            "fontFamily": "Arial",
            "marginTop": "15px"
        }
    ),

    # Radio Button
    html.Div([
        html.Label(
            "Filter by Region:",
            style={
                "fontFamily": "Arial",
                "fontWeight": "bold",
                "color": "#d63384",
                "fontSize": "16px",
                "marginRight": "10px"
            }
        ),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": " All",   "value": "all"},
                {"label": " North", "value": "north"},
                {"label": " South", "value": "south"},
                {"label": " East",  "value": "east"},
                {"label": " West",  "value": "west"},
            ],
            value="all",
            inline=True,
            style={"fontFamily": "Arial", "fontSize": "15px"},
            labelStyle={"marginRight": "20px", "cursor": "pointer"}
        )
    ], style={
        "textAlign": "center",
        "padding": "15px",
        "backgroundColor": "#ffe6f0",
        "borderRadius": "10px",
        "margin": "20px auto",
        "width": "70%",
        "boxShadow": "2px 2px 8px rgba(0,0,0,0.1)"
    }),

    # Line Chart
    dcc.Graph(id="sales-chart"),

], style={"backgroundColor": "#fff5f9", "minHeight": "100vh", "paddingBottom": "30px"})


# Callback to update chart based on region
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered = df.groupby("date")["sales"].sum().reset_index()
    else:
        filtered = df[df["region"] == selected_region].groupby("date")["sales"].sum().reset_index()

    fig = px.line(
        filtered,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales — Region: {selected_region.capitalize()}",
        labels={"date": "Date", "sales": "Total Sales ($)"},
        color_discrete_sequence=["#d63384"]
    )

    fig.add_vline(
        x=datetime.datetime(2021, 1, 15).timestamp() * 1000,
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase (Jan 15, 2021)",
        annotation_position="top right"
    )

    fig.update_layout(
        plot_bgcolor="#fff5f9",
        paper_bgcolor="#fff5f9",
        font={"family": "Arial", "color": "#333"},
        title_font={"size": 20, "color": "#d63384"},
        hovermode="x unified"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)