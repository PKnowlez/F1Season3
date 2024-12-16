import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image
import Tab0, Tab1, Tab2, Tab3, Tab4, Tab5, Tab6

st.set_page_config(layout="wide") 

# Read in excel sheet
df = pd.read_excel('F124_season.xlsx', sheet_name='PythonReadyData')

race_points = ['SuzukaPoints','SilverstonePoints','AustraliaPoints', 
                'SpaPoints','SpainPoints','ChinaSprintPoints','ChinaPoints', 
                'BakuPoints','CanadaPoints','MonzaPoints','Abu DhabiPoints', 
                'AustriaSprintPoints','AustriaPoints','COTASprintPoints','COTAPoints']
race_place = ['SuzukaPlace','SilverstonePlace','AustraliaPlace', 
                'SpaPlace','SpainPlace','ChinaSprintPlace','ChinaPlace', 
                'BakuPlace','CanadaPlace','MonzaPlace','Abu DhabiPlace', 
                'AustriaSprintPlace','AustriaPlace','COTASprintPlace','COTAPlace']
fastest_lap = ['SuzukaFastestLap','SilverstoneFastestLap','AustraliaFastestLap', 
                'SpaFastestLap','SpainFastestLap','ChinaSprintFastestLap','ChinaFastestLap', 
                'BakuFastestLap','CanadaFastestLap','MonzaFastestLap','Abu DhabiFastestLap', 
                'AustriaSprintFastestLap','AustriaFastestLap','COTASprintFastestLap','COTAFastestLap']
qualifying = ['SuzukaQualifying','SilverstoneQualifying','AustraliaQualifying', 
                'SpaQualifying','SpainQualifying','ChinaSprintQualifying','ChinaQualifying', 
                'BakuQualifying','CanadaQualifying','MonzaQualifying','Abu DhabiQualifying', 
                'AustriaSprintQualifying','AustriaQualifying','COTASprintQualifying','COTAQualifying']
races = ['Suzuka','Silverstone','Australia', 
                'Spa','Spain','China (S)','China', 
                'Baku','Canada','Monza','Abu Dhabi', 
                'Austria (S)','Austria','COTA (S)','COTA']

drivers = df['Driver']
teams = df['Team']
starting = df['Starting']

df['Total'] = 0
for i in range(len(race_points)):
    df['Total'] = df['Total'] + df[race_points[i]]

team_race_totals = pd.DataFrame([]) 
for i in range(len(race_points)):
    if i == 0:
        team_race_totals[race_points[i]] = df.groupby('Team')[race_points[i]].sum()
    else:
        team_race_totals[race_points[i]] = df.groupby('Team')[race_points[i]].sum() \
                                                + team_race_totals[race_points[i-1]]

driver_race_totals = pd.DataFrame([])
for i in range(len(race_points)):
    if i == 0:
        driver_race_totals[race_points[i]] = df.groupby('Driver')[race_points[i]].sum()
    else:
        driver_race_totals[race_points[i]] = df.groupby('Driver')[race_points[i]].sum() \
                                                + driver_race_totals[race_points[i-1]]

total = df['Total']
team_totals = df.groupby('Team')['Total'].sum()
team_totals_sorted = team_totals.sort_values(ascending=False)

# Define team colors
team_colors = {
    'Alpine': 'hotpink', 
    'Aston Martin': 'teal',
    'Ferrari': 'red',
    'McLaren': 'darkorange',
    'Red Bull': 'darkblue',
    'VCARB': 'blue'
}

# Driver colors
color_list = ['darkorange','orange','blue','skyblue','red','#ff6060','pink','hotpink','darkblue','#8888c9','#84c1c1','teal']
driver_colors = {}  # Initialize an empty dictionary
for i, driver in enumerate(drivers.unique()):
    driver_colors[driver] = color_list[i % len(color_list)]

for i in range(len(race_place)):
    if df.loc[0,race_points[i]] == 0:
        index = i
        index_x = index-0.5
        break
    else:
        x = 0

# --- Team Plot ---

# Add a new column of zeros at the beginning
team_race_totals.insert(0, 'Start', 0)  
team_race_totals = team_race_totals.T

races.insert(0, 'Start') 

# Create Plotly figure
fig1 = go.Figure()

for team in team_race_totals.columns:
    fig1.add_trace(go.Scatter(x=races,
                             y=team_race_totals[team], 
                             mode='lines+markers',
                             name=team, 
                             line=dict(color=team_colors.get(team))))

fig1.update_layout(
    xaxis_range=[0,index],
    xaxis_title="Race",
    yaxis_title="Total Points",
    title="Constructor's Championship",
    hovermode="x unified"  # Enhanced hover mode for better readability
)

# --- Driver Plot ---

# Add a new column of zeros at the beginning
driver_race_totals.insert(0, 'Start', 0)  
driver_race_totals = driver_race_totals.T 

# Create Plotly figure
fig2 = go.Figure()

for driver in driver_race_totals.columns:
    fig2.add_trace(go.Scatter(x=races,
                             y=driver_race_totals[driver], 
                             mode='lines+markers',
                             name=driver,
                             line=dict(color=driver_colors.get(driver))))

fig2.update_layout(
    xaxis_range=[0,index],
    xaxis_title="Race",
    yaxis_title="Total Points",
    title="Driver's Championship",
    hovermode="x unified"  # Enhanced hover mode for better readability
)

## ----- App Format ----- ##
logo = Image.open("./Images/TheAlternativeLogo.png")
st.image(logo)

tabs = st.tabs(["League News", "Standings", "Race Results", "Constructor Statistics", "Driver Statistics","Driver Comparisons","Race Schedule"])

# League News
with tabs[0]:
    Tab0.Tab0()

# Standings
with tabs[1]:
    team_df, team_races_points_only = Tab1.Tab1(
        team_race_totals,
        driver_race_totals,
        df,races,
        team_colors,
        fig1,
        fig2
        )

# Race Results
with tabs[2]:
    # Expands for each race: Reports race results like post race screen
    with st.expander("Pre-Season: Miami"):
        st.subheader("Winner: Joshua")
        MiamiResults = pd.DataFrame({
            'Place': ['1','2','3','4','16','17','18','19'],
            'Driver': ['Joshua','Nick**','Patrick','Erick','Yeti','Boz','Del','Gary'],
        })
        # Removes the index column from the markdown st.table
        hide_table_row_index = """
        <style>
        thead tr th:first-child {display:none}
        tbody th {display:none}
        </style>
        """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(MiamiResults)
    for i in range(len(races)):
        if i == 0:
            x = 0
        else:
            if not pd.isnull(df.loc[1,race_place[i-1]]):
                with st.expander(races[i]):
                    df_sorted = df.sort_values(race_place[i-1], ascending=True)
                    winner = df_sorted['Driver'].iloc[0]
                    constructor = df_sorted['Team'].iloc[0]
                    st.subheader("Winner: " + winner + " - " + constructor)
                    
                    # Construct the correct column name
                    qualifying_col = races[i] + 'Qualifying' 
                    if '(S)' in races[i]:  # Adjust for Sprint races
                        qualifying_col = races[i].replace(' (S)', '') + 'SprintQualifying'

                    fastestlap_col = races[i] + 'FastestLap'
                    if '(S)' in races[i]:
                        fastestlap_col = races[i].replace(' (S)','') + 'SprintFastestLap'

                    race_results_df = pd.DataFrame({
                    'Place': df_sorted[race_place[i-1]],
                    'Driver': df_sorted['Driver'],
                    'Team': df_sorted['Team'],
                    'Qualifying': df_sorted[qualifying_col],
                    'Points': df_sorted[race_points[i-1]],
                    'Fastest Lap': df_sorted[fastestlap_col]
                    })

                    race_results_df['Place'] = race_results_df['Place'].replace({
                        21: 'DNF', 
                        22: 'DNS'
                    })

                    race_results_df['Qualifying'] = race_results_df['Qualifying'].replace({
                        21: 'DNF', 
                        22: 'DNS'
                    })

                    st.table(race_results_df)
            else:
                x = 0

# Constructor Statistics    
with tabs[3]:
    # Expands for each constructor: race results bar graph, best finish callout, total points callout,
    # Total points bar graph for all constructors
    # Add expands for each constructor with:
    # - Number of fastest laps callout
    # - Number of wins callout
    # - Driver/Team Bios

    # Loops through each driver to create an expand with their information only
    for i in range(len(team_df['Team'])):
        with st.expander(team_df['Team'][i]):
            team_name = team_df['Team'][i]  # Get the team's name
            team_points = team_df.iloc[i, 1:].tolist()

            # Create the figure name using the driver's name
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
            globals()[fig_name].update_layout(xaxis_range=[-0.5,index_x])

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

# Driver Statistics
with tabs[4]:
    # Expands for each driver: Race results bar graph, highest finish, number of wins, 
    #   number of podiums, total points, fastest laps total, average qualifying,
    #   average place, qualifying vs finsih graph, qualyfing vs finish average

    # Creates a list of all the points columns in the excel sheet
    points_columns = [col for col in df.columns if col.endswith(('Points', 'SprintPoints'))]
    fastest_lap_columns = [col for col in df.columns if col.endswith(('FastestLap'))]
    qualifying_columns = [col for col in df.columns if col.endswith(('Qualifying'))]
    place_columns = [col for col in df.columns if col.endswith(('Place'))]

    # Creates the order of the races to be graphed along the x-axis
    races_points_only = races.copy()
    del races_points_only[0]

    # Creates a new dataframe with only the drivers and points columns
    new_df = df.set_index('Driver')[points_columns]
    new_df = new_df.reset_index()

    # Creates a new dataframe with only the drivers and fastest laps columns
    new_df_FL = df.set_index('Driver')[fastest_lap_columns]
    new_df_FL = new_df_FL.reset_index()

    # Creates a new dataframe with only the drivers and qualifying columns
    new_df_Q = df.set_index('Driver')[qualifying_columns]
    new_df_Q = new_df_Q.reset_index()

    # Creates a new dataframe with only the drivers and placement columns
    new_df_Place = df.set_index('Driver')[place_columns]
    new_df_Place = new_df_Place.reset_index()

    # Variables for loop
    drivers_total_points = []
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
            globals()[fig_name].update_layout(xaxis_range=[-0.5,index_x], showlegend=False)  # Hide the legend

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
            button_key3 = button_key2 + "_" + str(i)
            countP = 'Podiums: ' + str(count)

            # Calculates the total points for a driver
            button_key4 = button_key3 + "_" + str(i)
            total_pointsN = sum(driver_points)
            total_points = 'Total Points: ' + str(total_pointsN)
            # Create driver total points list
            drivers_total_points.append(total_pointsN)

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
                elif value >= 1:
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
                    count_fastest_laps =+ 1
                elif value == 'y':
                    count_fastest_laps =+ 1
            
            # Sets the value to be displayed for Driver Fastest Lap
            button_key5 = button_key4 + "_" + str(i)
            fastest_lap_count = 'Fastest Laps: ' + str(count_fastest_laps)

            # Calculates the difference in qualifying and race placement per driver
            driver_qualifying = new_df_Q.iloc[i, 1:].tolist()
            driver_place = new_df_Place.iloc[i,1:].tolist()
            qualifying_place = [x - y for x, y in zip(driver_qualifying, driver_place)]

            # Create the figure name using the driver's name
            fig_name3 = f"{driver_name} Positions Gained or Lost Per Race"

            # Create a list of colors based on the values in qualifying_place
            colors = ['green' if val >= 0 else 'red' for val in qualifying_place]

            # Use globals() to dynamically create the variable with the color list
            globals()[fig_name3] = px.bar(x=races_points_only, y=qualifying_place, 
                                        title=fig_name3, color=colors,
                                        color_discrete_map="identity")  # Use the provided colors

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
            driver_changed = 'Average Position Change: ' + str(round(driver_changedN))
            button_key8 = button_key7 + "_" + str(i)
            # Create full average positions gained/lost list
            average_changed.append(driver_changedN)

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
                st.button(best_finish,key=button_key)
            col9, col10, col11 = st.columns(3)
            with col9:
                st.plotly_chart(globals()[fig_name])
            with col10:
                st.plotly_chart(globals()[fig_name2])
            with col11:
                st.plotly_chart(globals()[fig_name3])

# Driver Comparisons
with tabs[5]:
    # Y variables average_changed, average_place, average_qualifying, drivers_total_points
    # X variable is new_df['Driver']
    Tab5.Tab5()

# Race Schedule  
with tabs[6]:
    Tab6.Tab6()