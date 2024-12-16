import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image
import Tab0_LeagueNews, Tab1_Standings, Tab2_RaceResults, Tab3_ConstructorStatistics, Tab4_DriverStatistics, \
    Tab5_DriverComparison, Tab6_RaceSchedule, Calculations

# Calculations
team_race_totals,driver_race_totals,df,races,team_colors,fig1,fig2,race_place,race_points,index_x, \
new_df,new_df_FL,new_df_Q,new_df_Place,races_points_only,drivers_total_points,driver_colors \
    = Calculations.Calculations()

## ----- App Format ----- ##
st.set_page_config(layout="wide") 

# Header
logo = Image.open("./Images/TheAlternativeLogo.png")
st.image(logo)

# Declare Tabs
tabs = st.tabs([
    "League News",
    "Standings",
    "Race Results",
    "Constructor Statistics",
    "Driver Statistics",
    "Driver Comparisons",
    "Race Schedule"
    ])

# League News
with tabs[0]:
    Tab0_LeagueNews.Tab0()

# Standings
with tabs[1]:
    team_df,team_races_points_only,drivers_points_df,colors_driver_team \
        = Tab1_Standings.Tab1(team_race_totals,driver_race_totals,df,races,team_colors,fig1,fig2,new_df,
                              drivers_total_points,driver_colors)

# Race Results
with tabs[2]:
    Tab2_RaceResults.Tab2(races,df,race_place,race_points)

# Constructor Statistics    
with tabs[3]:
    colors = Tab3_ConstructorStatistics.Tab3(team_df,team_races_points_only,index_x,
                                             drivers_points_df,colors_driver_team)

# Driver Statistics
with tabs[4]:
    new_df,average_changed,average_qualifying,average_place \
        = Tab4_DriverStatistics.Tab4(colors,index_x,new_df,new_df_FL,new_df_Q,new_df_Place,races_points_only)

# Driver Comparisons
with tabs[5]:
    Tab5_DriverComparison.Tab5(new_df,average_changed,drivers_total_points,average_qualifying,average_place)

# Race Schedule  
with tabs[6]:
    Tab6_RaceSchedule.Tab6()