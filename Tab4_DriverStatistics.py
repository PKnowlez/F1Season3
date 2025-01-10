import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
import numpy as np
from PIL import Image

# Expands for each driver: Race results bar graph, highest finish, number of wins, 
#   number of podiums, total points, fastest laps total, average qualifying,
#   average place, qualifying vs finsih graph, qualyfing vs finish average
def Tab4(colors,index_x,new_df,new_df_FL,new_df_Q,new_df_Place,races_points_only):
    # Variables for loop
    total_points = []
    average_changed = []
    average_qualifying = []
    average_place = []

    # Loops through each driver to create an expand with their information only
    for i in range(len(new_df['Driver'])):
        with st.expander(new_df['Driver'][i]):
            driver_name = new_df['Driver'][i]  # Get the driver's name
            driver_points = new_df.iloc[i, 1:].tolist()

            # Create the figure name using the driver's name
            fig_name = f"{driver_name} Points Per Race"

            # Use globals() to dynamically create the variable
            globals()[fig_name] = px.bar(x=races_points_only, y=driver_points, 
                                        title=fig_name, color=races_points_only,
                                        color_discrete_sequence=colors) 

            globals()[fig_name].update_xaxes(categoryorder='array', categoryarray=races_points_only)

            # Update x-axis title
            globals()[fig_name].update_xaxes(title_text="Race", categoryorder='array', categoryarray=races_points_only)

            # Update y-axis title
            globals()[fig_name].update_yaxes(title_text="Points")

            # Update layout
            globals()[fig_name].update_layout(xaxis_range=[-0.5,index_x], showlegend=False)

            # Calculates the highest placement a driver has achieved
            highest_score = max(driver_points)
            index = driver_points.index(highest_score)
            if highest_score >= 25:
                place = '1st'
            elif highest_score >= 18:
                place = '2nd'
            elif highest_score >= 15:
                place = '3rd'
            elif highest_score >= 12:
                place = '4th'
            elif highest_score >= 10:
                place = '5th'
            elif highest_score >= 8:
                place = '6th'
            elif highest_score >= 6:
                place = '7th'
            elif highest_score >= 4:
                place = '8th'
            elif highest_score >= 2:
                place = '9th'
            else:
                place = '10th or lower'
            best_finish = 'Best Finish: ' + place + ' at ' + races_points_only[index] + ' (' + str(highest_score) + ' points)'
            button_key = 'Button' + "_" + str(i)

            # Calculates the number of wins a driver has
            specific_value = 25
            count = 0
            for value in driver_points:
                if value >= specific_value:
                    count += 1
            button_key2 = button_key + "_" + str(i)
            countW = 'Wins: ' + str(count)

            # Calculates the number of podiums a driver has
            specific_value = 15
            count = 0
            for value in driver_points:
                if value >= specific_value:
                    count += 1
            # sprint_cols = [col for col in new_df.columns if col.endswith('SprintPoints')]
            # sprint_indexes = [new_df.columns.get_loc(col) for col in sprint_cols]
            # for i, points in enumerate(driver_points):
            #     if i in sprint_indexes and points >= 6:
            #         count += 1
            button_key3 = button_key2 + "_" + str(i)
            countP = 'Podiums: ' + str(count)

            # Calculates the total points for a driver
            button_key4 = button_key3 + "_" + str(i)
            total_pointsN = sum(driver_points)
            total_points = 'Total Points: ' + str(total_pointsN)

            # Creates placement graph
            placements = [0,0,0,0,0,0,0,0,0,0]
            places = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th+']
            for value in driver_points:
                if value >= 25:
                    placements[0] += 1
                elif value >= 18:
                    placements[1] += 1
                elif value >= 15:
                    placements[2] += 1
                elif value >= 12:
                    placements[3] += 1
                elif value >= 10:
                    placements[4] += 1
                elif value >= 8:
                    placements[5] += 1
                elif value >= 6:
                    placements[6] += 1
                elif value >= 4:
                    placements[7] += 1
                elif value >= 2:
                    placements[8] += 1
                elif value >= 0.5:
                    placements[9] += 1
            # Create the figure name using the driver's name
            fig_name2 = f"{driver_name} Placements Summary"

            # Use globals() to dynamically create the variable
            globals()[fig_name2] = px.bar(x=places, y=placements, title=fig_name2)
            globals()[fig_name2].update_xaxes(categoryorder='array', categoryarray=races_points_only)

            # Update x-axis title
            globals()[fig_name2].update_xaxes(title_text="Placement", categoryorder='array', categoryarray=races_points_only)

            # Update y-axis title
            globals()[fig_name2].update_yaxes(title_text="Count") 

            # Calculates the number of fastest laps a driver has earned
            driver_fastest_laps = new_df_FL.iloc[i, 1:].tolist()
            count_fastest_laps = 0
            for value in driver_fastest_laps:
                if value == 'Y':
                    count_fastest_laps += 1
                elif value == 'y':
                    count_fastest_laps += 1
            
            # Sets the value to be displayed for Driver Fastest Lap
            button_key5 = button_key4 + "_" + str(i)
            fastest_lap_count = 'Fastest Laps: ' + str(count_fastest_laps)

            # Calculates the difference in qualifying and race placement per driver
            index_a = int(index_x+0.5)
            driver_qualifying = new_df_Q.iloc[i, 1:index_a + 1].tolist()
            driver_place = new_df_Place.iloc[i, 1:index_a + 1].tolist()

            # Convert to numeric, replacing non-numeric with NaN
            driver_qualifying = pd.to_numeric(driver_qualifying, errors='coerce')
            driver_place = pd.to_numeric(driver_place, errors='coerce')

            # Fill NaN with a specific value (e.g., 0)
            driver_qualifying = np.nan_to_num(driver_qualifying, nan=0)
            driver_place = np.nan_to_num(driver_place, nan=0)
            qualifying_place = [x - y for x, y in zip(driver_qualifying, driver_place)]

            # Create the figure name using the driver's name
            fig_name3 = f"{driver_name} Positions Gained or Lost Per Race"

            # Create a list of colors based on the values in qualifying_place
            colorsRG = ['green' if val >= 0 else 'red' for val in qualifying_place]

            # Use globals() to dynamically create the variable with the color list
            globals()[fig_name3] = px.bar(x=races_points_only[:index_a], y=qualifying_place, 
                                        title=fig_name3, color=colorsRG,
                                        color_discrete_map="identity")

            globals()[fig_name3].update_xaxes(categoryorder='array', categoryarray=races_points_only)

            # Update x-axis title
            globals()[fig_name3].update_xaxes(title_text="Race", categoryorder='array', categoryarray=races_points_only)

            # Update y-axis title
            globals()[fig_name3].update_yaxes(title_text="Positions Changed")

            # Update layout
            globals()[fig_name3].update_layout(xaxis_range=[-0.5,index_x]) 

            # Calculate Average Qualifying Position
            driver_qualifying_average = []
            driver_qualifying_average = [item for item in driver_qualifying if not math.isnan(item)]
            driver_qualifying_averageN = sum(driver_qualifying_average) / len(driver_qualifying_average)
            driver_qualifying_average = 'Average Qualifying: ' + str(round(driver_qualifying_averageN,1))
            button_key6 = button_key5 + "_" + str(i)
            # Create full average qualifying list
            average_qualifying.append(driver_qualifying_averageN)

            # Calculate Average Finishing Position
            driver_place_average = []
            driver_place_average = [item for item in driver_place if not math.isnan(item)]
            driver_place_averageN = sum(driver_place_average) / len(driver_place_average)
            driver_place_average = 'Average Place: ' + str(round(driver_place_averageN,1))
            button_key7 = button_key6 + "_" + str(i)
            # Create full average finishing list
            average_place.append(driver_place_averageN)

            # Calculates Average Positions Gained/Lost
            driver_changedN = driver_qualifying_averageN - driver_place_averageN
            driver_changed = 'Average Position Change: ' + str(round(driver_changedN,1))
            button_key8 = button_key7 + "_" + str(i)
            # Create full average positions gained/lost list
            average_changed.append(driver_changedN)

            # Calculates the number of fastest laps a driver has earned
            pole_positions_count = 0
            for value in driver_qualifying:
                if value == 1:
                    pole_positions_count = pole_positions_count + 1

            # Sets the value to be displayed for number of pole positions
            button_key9 = button_key8 + "_" + str(i)
            pole_positions = 'Pole Positions: ' + str(pole_positions_count)

            # Creates the layout for each expand
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.button(total_points,key=button_key4)
            with col2:
                st.button(countW,key=button_key2)
            with col3:
                st.button(countP,key=button_key3)
            with col4:
                st.button(fastest_lap_count,key=button_key5)
            col5, col6, col7, col8 = st.columns(4)
            with col5:
                st.button(driver_qualifying_average,key=button_key6)
            with col6:
                st.button(driver_place_average,key=button_key7)
            with col7:
                st.button(driver_changed,key=button_key8)
            with col8:
                st.button(pole_positions,key=button_key9)
            col9,colN = st.columns(2)
            with col9:
                st.button(best_finish,key=button_key)
            col10, col11, col12 = st.columns(3)
            with col10:
                st.plotly_chart(globals()[fig_name])
            with col11:
                st.plotly_chart(globals()[fig_name2])
            with col12:
                st.plotly_chart(globals()[fig_name3])
    
    return new_df,average_changed,average_qualifying,average_place