#imports
import json
import pandas as pd
import plotly.express as px

## Load data
with open('Location History\Location History.json') as f:
    data = json.load(f)
df = pd.DataFrame.from_dict(data['locations'])
df2= df[['timestampMs','longitudeE7','latitudeE7']].copy()

## Data Enrichment for series colors
df2['datetime'] = pd.to_datetime(df2['timestampMs'].astype('int64'),utc=True,unit = 'ms')
df2["date"] = df2["datetime"].dt.date
df2["lat"]=df2['latitudeE7']/10000000
df2["long"]=df2['longitudeE7']/10000000
df2['year'] = df2['datetime'].dt.year
df2['month'] = df2['datetime'].dt.month
df2['month_name'] =df2['datetime'].dt.month_name()
df2['month_year'] =df2['month_name'].astype(str) + '_' + df2['year'].astype(str)

## Prep and plot the figure
fig = px.line_mapbox(df2, lat='lat', lon='long',color = 'month_year',zoom=2, height=800)

fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat = 41,title = 'My Locastion History from Google!<br>(Hover for location)',
    margin={"r":20,"t":20,"l":20,"b":20})

fig.show()

