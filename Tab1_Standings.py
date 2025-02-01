import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

def Tab1(team_race_totals,driver_race_totals,df,races,team_colors,fig1,fig2,new_df,drivers_total_points,
         driver_colors):
    totals = team_race_totals.T
    constructor_sorted = totals.sort_values('COTAPoints', ascending=False)
    constructor_sorted = constructor_sorted.reset_index() 
    constructor_totals = pd.DataFrame({
    'Team': constructor_sorted['Team'],
    'Points': [f"{points:.1f}" for points in constructor_sorted['COTAPoints']],
    })

    totals = driver_race_totals.T
    driver_sorted = totals.sort_values('COTAPoints', ascending=False)
    driver_sorted = driver_sorted.reset_index() 
    driver_totals = pd.DataFrame({
    'Driver': driver_sorted['Driver'],
    'Points': [f"{points:.1f}" for points in driver_sorted['COTAPoints']],
    })

    # Creates a list of all the points columns in the excel sheet
    team_points_columns = [col for col in df.columns if col.endswith(('Points', 'SprintPoints'))] 

    # Creates the order of the races to be graphed along the x-axis
    team_races_points_only = races.copy()
    del team_races_points_only[0]

    # Create team_df
    team_df = df.groupby('Team')[team_points_columns].sum()
    team_df = team_df.reset_index()
    
    # --------------------- #
    # Create the figure name
    fig_name0 = "Constructor Points"

    # Create a list of colors corresponding to the teams in constructor_totals['Team']
    colors = [team_colors.get(team) for team in constructor_totals['Team']]
    
    # Use globals() to dynamically create the variable with the color list
    globals()[fig_name0] = px.bar(
        x=constructor_totals['Team'], 
        y=constructor_totals['Points'], 
        title=fig_name0,
        color=colors,
        color_discrete_map="identity"
    )

    # Update x-axis title
    globals()[fig_name0].update_xaxes(title_text="Constructor")

    # Update y-axis title
    globals()[fig_name0].update_yaxes(title_text="Points")

    # --------------------- #
    # Create the figure name
    fig_name00 = "Driver Points"

    drivers_points_df = pd.DataFrame({
        'Driver': new_df['Driver'].copy(),
        'Team': df['Team'].copy(),
        'Points': drivers_total_points
    })

    # Key change: Group by driver and sum points
    drivers_points_2df = drivers_points_df.groupby('Driver')['Points'].sum().reset_index()

    drivers_points_3df = drivers_points_2df.sort_values(by='Points', ascending=False)

    # Create a list of colors corresponding to the drivers
    colors_driver_team = []
    colors_driver_list = []
    for driver in drivers_points_3df['Driver']:
        color = driver_colors.get(driver)
        colors_driver_team.append(color)
        colors_driver_list.append(driver)
    colors_driver_df = pd.DataFrame(list(zip(colors_driver_list, colors_driver_team)), columns=['Driver', 'Color'])

    globals()[fig_name00] = px.bar(
        x=drivers_points_3df['Driver'],
        y=drivers_points_3df['Points'],
        title=fig_name00,
        color=colors_driver_team, 
        color_discrete_map="identity" 
    )

    # Update x-axis title
    globals()[fig_name00].update_xaxes(title_text="Driver")

    # Update y-axis title
    globals()[fig_name00].update_yaxes(title_text="Points")

    # ----------------------- #
    # Layout for tab
    col1, col2 = st.columns(2)
    with col1:
        with st.popover("Full Constructor's Championship Standings"):
            st.table(constructor_totals)
    with col2:
        with st.popover("Full Driver's Championship Standings"):
            st.table(driver_totals)
    col3, col4 = st.columns(2)
    with col3:
        # Display the Team Plot in Streamlit
        st.plotly_chart(fig1)
        # Display the Team Bar plot
        st.plotly_chart(globals()[fig_name0])
    with col4:
        # Display the Driver Plot in Streamlit
        st.plotly_chart(fig2)
        # Display the Driver Bar plot
        st.plotly_chart(globals()[fig_name00])

    return team_df,team_races_points_only,drivers_points_df,colors_driver_team,colors_driver_df