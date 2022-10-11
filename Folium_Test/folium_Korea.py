"""
Created on Fri Aug 31 16:42:02 2018

@author: kccha
"""

# Import libraries
import pandas as pd
import folium
import webbrowser
 
# Load the shape of the zone (US states)
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
# You have to download this file and set the directory where you saved it
state_geo = 'TL_SCCO_SIG_WGS84.json'
 
# Load the unemployment value of each state
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
state_unemployment = 'Total_People_2018.csv'
state_data = pd.read_csv(state_unemployment, encoding = 'euc-kr')
 
# Initialize the map:
m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)
 
# Add the color for the chloropleth:

m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=state_data,
 columns=['Code', 'Population'],
 key_on='feature.properties.SIG_CD',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='Population Rate (%)'
)

folium.LayerControl().add_to(m)
 
# Save to html
m.save('folium_kr.html')
webbrowser.open_new("folium_kr.html")






