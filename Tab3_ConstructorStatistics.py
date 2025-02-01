import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

# Expands for each constructor: race results bar graph, best finish callout, total points callout,
# Total points bar graph for all constructors
# Add expands for each constructor with:
# - Number of fastest laps callout
# - Number of wins callout
# - Driver/Team Bios
def Tab3(team_df,team_races_points_only,index_x,drivers_points_df,colors_driver_team,colors_driver_df):
    # wins_df = new_df.copy()
    # wins_df = wins_df.mask(wins_df < "25", 0)
    # wins_df = wins_df.mask(wins_df > "24", 1)
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown('''**Stacked Constructor Points**''')
        fig_name000 = "Stacked Constructor Points"
        
        # Calculate total points per team
        team_total_points = drivers_points_df.groupby('Team')['Points'].sum().sort_values(ascending=True)

        # Create the plot
        globals()[fig_name000] = px.bar(drivers_points_df, 
                                        x='Points', 
                                        y='Team', 
                                        color='Driver', 
                                        orientation='h',
                                        barmode='stack',
                                        color_discrete_map=dict(zip(colors_driver_df['Driver'], colors_driver_df['Color'])))

        # Order the bars based on total team points
        globals()[fig_name000].update_yaxes(categoryorder='array', categoryarray=team_total_points.index)

        st.plotly_chart(globals()[fig_name000])
    
    with col4:
        st.markdown('''**Individual Constructor Statistics**''')
        # Loops through each constructor to create an expand with their information only
        for i in range(len(team_df['Team'])):
            with st.expander(team_df['Team'][i]):
                team_name = team_df['Team'][i]  # Get the team's name
                team_points = team_df.iloc[i, 1:].tolist()

                # Create the figure name using the constructor's name
                fig_name = f"{team_name} Points Per Race"
                
                # 15 unique colors
                colors = [
                    '#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', 
                    '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', 
                    '#800000'
                ]

                # Use globals() to dynamically create the variable
                globals()[fig_name] = px.bar(x=team_races_points_only, y=team_points, title=fig_name,
                                            color=team_races_points_only,
                                            color_discrete_sequence=colors)
                globals()[fig_name].update_xaxes(categoryorder='array', categoryarray=team_races_points_only)

                # Update x-axis title
                globals()[fig_name].update_xaxes(title_text="Race", categoryorder='array', categoryarray=team_races_points_only)

                # Update y-axis title
                globals()[fig_name].update_yaxes(title_text="Points")

                # Update layout
                globals()[fig_name].update_layout(xaxis_range=[-0.5,index_x], showlegend=False)

                # Calculates the highest placement a driver has achieved
                highest_score = max(team_points)
                index = team_points.index(highest_score)
                best_result = 'Best Result: ' + team_races_points_only[index] + ' (' + str(highest_score) + ' points)'
                button_key = 'TeamButton' + "_" + str(i)

                # Calculates the total points for a team
                button_key1 = button_key + "_" + str(i)
                total_pointsN = sum(team_points)
                total_points = 'Total Points: ' + str(total_pointsN)
                # Create full list of team total points
                team_total_points = []
                team_total_points.append(total_pointsN)

                # Creates the layout for each expand
                col1, col2 = st.columns(2)
                with col1:
                    st.button(total_points,key=button_key1)
                with col2:
                    st.button(best_result,key=button_key)
                st.plotly_chart(globals()[fig_name])

    return colors