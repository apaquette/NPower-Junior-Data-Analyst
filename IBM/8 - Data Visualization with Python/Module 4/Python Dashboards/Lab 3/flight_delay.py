import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output

file = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv'

airline_data =  pd.read_csv(file,
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

app = dash.Dash(__name__)

# Dashboard Title
html_dashboard_title = html.H1('Flight Delay Time Statistics Dashboard',
                style={'align-text': 'center', 'color': '#503D36', 'font-size': 35})

html_year_input = html.Div([
'Input Year: ',
dcc.Input(  id='input-year',
            value='2010',
            type='number',
            style={'height':35, 'font-size': 30}
        )
],
style={'font-size': 30})

carrier_plot = dcc.Graph(id='carrier-plot')
weather_plot = dcc.Graph(id='weather-plot')

html_segment_one = html.Div([
    html.Div(carrier_plot),
    html.Div(weather_plot)
], style={'display': 'flex'})

nas_plot = dcc.Graph(id='nas-plot')
security_plot = dcc.Graph(id='security-plot')

html_segment_two = html.Div([
    html.Div(nas_plot),
    html.Div(security_plot)
], style={'display': 'flex'})

late_plot = dcc.Graph(id='late-plot')

html_segment_three = html.Div(late_plot, style={'width':'65%'})

app.layout = html.Div(children=[
    html_dashboard_title,
    html_year_input,
    html.Br(), html.Br(),
    html_segment_one,
    html_segment_two,
    html_segment_three
])

""" Compute_info function description

This function takes in airline data and selected year as an input and performs computation for creating charts and plots.

Arguments:
    data: Input airline data.
    entered_year: Input year for which computation needs to be performed.
    
Returns:
    Computed average dataframes for carrier delay, weather delay, NAS delay, security delay, and late aircraft delay.

"""
def compute_info(data, entered_year):
    # Select data
    df =  data[data['Year']==int(entered_year)]
    # Compute delay averages
    avg_car = df.groupby(['Month','Reporting_Airline'])['CarrierDelay'].mean().reset_index()
    avg_weather = df.groupby(['Month','Reporting_Airline'])['WeatherDelay'].mean().reset_index()
    avg_NAS = df.groupby(['Month','Reporting_Airline'])['NASDelay'].mean().reset_index()
    avg_sec = df.groupby(['Month','Reporting_Airline'])['SecurityDelay'].mean().reset_index()
    avg_late = df.groupby(['Month','Reporting_Airline'])['LateAircraftDelay'].mean().reset_index()
    return avg_car, avg_weather, avg_NAS, avg_sec, avg_late

def get_airline_fig(avg: pd.DataFrame, y: str, title: str):
    return px.line(avg, x='Month', y=y, color='Reporting_Airline', title=title)

@app.callback(
    [
        Output(component_id='carrier-plot', component_property='figure'),
        Output(component_id='weather-plot', component_property='figure'),
        Output(component_id='nas-plot', component_property='figure'),
        Output(component_id='security-plot', component_property='figure'),
        Output(component_id='late-plot', component_property='figure'),
    ],
    Input(component_id='input-year', component_property='value')
)
def get_graph(year):
    avg_car, avg_weather, avg_NAS, avg_sec, avg_late = compute_info(airline_data, year)
    carrier_fig = get_airline_fig(avg_car, 'CarrierDelay', 'Average carrrier delay time (minutes) by airline')
    weather_fig = get_airline_fig(avg_weather, 'WeatherDelay', 'Average weather delay time (minutes) by airline')
    nas_fig = get_airline_fig(avg_NAS, 'NASDelay', 'Average NAS delay time (minutes) by airline')
    security_fig = get_airline_fig(avg_sec, 'SecurityDelay', 'Average security delay time (minutes) by airline')
    late_fig = get_airline_fig(avg_late, 'LateAircraftDelay', 'Average late aircraft delay time (minutes) by airline')

    return [carrier_fig, weather_fig, nas_fig, security_fig, late_fig]

if __name__ == '__main__':
    app.run()
