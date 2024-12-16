import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image
import Tab0, Tab1, Tab2, Tab3, Tab4, Tab5, Tab6, Calculations

team_race_totals,driver_race_totals,df,races,team_colors,fig1,fig2,race_place,race_points,index_x \
    = Calculations.Calculations()

## ----- App Format ----- ##
st.set_page_config(layout="wide") 

# Header
logo = Image.open("./Images/TheAlternativeLogo.png")
st.image(logo)

#Tabs
tabs = st.tabs(["League News", "Standings", "Race Results", "Constructor Statistics", "Driver Statistics","Driver Comparisons","Race Schedule"])

# League News
with tabs[0]:
    Tab0.Tab0()

# Standings
with tabs[1]:
    team_df, team_races_points_only \
        = Tab1.Tab1(team_race_totals,driver_race_totals,df,races,team_colors,fig1,fig2)

# Race Results
with tabs[2]:
    # Expands for each race: Reports race results like post race screen
    Tab2.Tab2(races,df,race_place,race_points)

# Constructor Statistics    
with tabs[3]:
    # Expands for each constructor: race results bar graph, best finish callout, total points callout,
    # Total points bar graph for all constructors
    # Add expands for each constructor with:
    # - Number of fastest laps callout
    # - Number of wins callout
    # - Driver/Team Bios
    colors = Tab3.Tab3(team_df,team_races_points_only,index_x)

# Driver Statistics
with tabs[4]:
    # Expands for each driver: Race results bar graph, highest finish, number of wins, 
    #   number of podiums, total points, fastest laps total, average qualifying,
    #   average place, qualifying vs finsih graph, qualyfing vs finish average
    new_df,average_changed,drivers_total_points,average_qualifying,average_place \
        = Tab4.Tab4(df,races,colors,index_x)

# Driver Comparisons
with tabs[5]:
    # Y variables average_changed, average_place, average_qualifying, drivers_total_points
    # X variable is new_df['Driver']
    Tab5.Tab5(new_df,average_changed,drivers_total_points,average_qualifying,average_place)

# Race Schedule  
with tabs[6]:
    Tab6.Tab6()