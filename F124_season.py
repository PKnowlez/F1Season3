import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image

# Load the data
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
qualifiying = ['SuzukaQualifying','SilverstoneQualifying','AustraliaQualifying', 
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
color_list = ['darkorange','orange','blue','skyblue','red','#ff6060','hotpink','pink','darkblue','#8888c9','teal','#84c1c1']
driver_colors = {}  # Initialize an empty dictionary
for i, driver in enumerate(drivers.unique()):
    driver_colors[driver] = color_list[i % len(color_list)]

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
    xaxis_title="Race",
    yaxis_title="Total Points",
    title="Driver's Championship",
    hovermode="x unified"  # Enhanced hover mode for better readability
)

## ----- App Format ----- ##
logo = Image.open("TheAlternativeLogo.png")
st.image(logo)

tabs = st.tabs(["League News", "Standings", "Race Results", "Constructor Statistics", "Driver Statistics","Race Schedule"])

# League News
with tabs[0]:
    # Author and add news articles for each race with headlines and such
    
    st.subheader('Suzuka & Pre-Season Recap')
    st.markdown('''
                With a lovely pre-season in Miami complete where 8 of the league's 12 drivers and all 6 constructors took to the streets 
                around Hard Rock Statium, the lights went out in Suzuka to an aborted start. With a multiple car incident that sent the 
                whole grid into turmoil,the race director determined it was best to have a full restart. One of our top qualifiers, VCARB's 
                Patrick, fell back two positions at the start and near the end of the first lap attempted to make up those positions going 
                into the Hitachi Astemo Chicane. This manuever failed and ended with a slow down into the chicane allowing many of our drivers 
                to make up spots against the AI and other drivers. The remainder of the race saw only a few spins, beachings, and other minor 
                mishaps that affected a few of the final standings. Big winners from this race include VCARB's Brentuar as well as Aston Martin's 
                Del. Alpine's Joshua took home the win and the fastest lap with McLaren's reigning champion Nick coming in second and Del 
                rounding out the podium.
                ''' + '''
                With the results final, Alpine takes an early lead in the Constructor's Championship. Alpine's Joshua is also leading the
                Driver's Championship. Reigning champion Nick finds himself in second place in the Driver's Championship with his team,
                McLaren, also slotting into second overall in the Constructor's Championship. Ferrari, Aston Martin, VCARB, and Red Bull
                respectively make up the rest of the Constructor's Championship standings.
                ''')

# Standings
with tabs[1]:
    col1, col2 = st.columns(2)
    with col1:
        with st.popover("Full Constructor's Championship Standings"):
            totals = team_race_totals.T
            constructor_sorted = totals.sort_values('COTAPoints', ascending=False)
            constructor_sorted = constructor_sorted.reset_index() 
            constructor_totals = pd.DataFrame({
            'Team': constructor_sorted['Team'],
            'Points': constructor_sorted['COTAPoints'],
            })
            st.table(constructor_totals)
    with col2:
        with st.popover("Full Driver's Championship Standings"):
            totals = driver_race_totals.T
            driver_sorted = totals.sort_values('COTAPoints', ascending=False)
            driver_sorted = driver_sorted.reset_index() 
            driver_totals = pd.DataFrame({
            'Driver': driver_sorted['Driver'],
            'Points': driver_sorted['COTAPoints'],
            })
            st.table(driver_totals)
         
    # Display the Team Plot in Streamlit
    st.plotly_chart(fig1)
    
    #st.subheader("", divider='rainbow')
    st.divider()
    
    # Display the Driver Plot in Streamlit
    st.plotly_chart(fig2)

# Race Results
with tabs[2]:
    # Expands for each race
    # - Reports race results like post race screen
    with st.expander("Pre-Season: Miami"):
        st.subheader("Winner: Joshua")
        MiamiResults = pd.DataFrame({
            'Driver': ['Joshua','Nick**','Patrick','Erick','Yeti','Boz','Del','Gary'],
            'Place': ['1','2','3','4','16','17','18','19'],
        })
        # CSS to inject contained in a string
        hide_table_row_index = """
        <style>
        thead tr th:first-child {display:none}
        tbody th {display:none}
        </style>
        """
        # Inject CSS with Markdown
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.table(MiamiResults)
    for i in range(len(races)):
        if i == 0:
            x = 0
        else:
            with st.expander(races[i]):
                df_sorted = df.sort_values(race_place[i-1], ascending=True)
                winner = df_sorted['Driver'].iloc[0]
                constructor = df_sorted['Team'].iloc[0]
                st.subheader("Winner: " + winner + " - " + constructor)
                race_results_df = pd.DataFrame({
                'Driver': df_sorted['Driver'],
                'Team': df_sorted['Team'],
                'Place': df_sorted[race_place[i-1]],
                'Points': df_sorted[race_points[i-1]],
                #'Fastest Lap': df_sorted[races[i]+'FastestLap']
                })
                st.table(race_results_df)

# Constructor Statistics    
with tabs[3]:
    # Add expands for each constructor with:
    # - Bar graph showing result at each race (stacked if possible)
    # - Best finish of the season callout
    # - Number of fastest laps callout
    # - Number of wins callout
    # - Total points callout
    # - Driver/Team Bios
    st.image('https://i.imgflip.com/2mxizj.jpg?a480720')

# Driver Statistics
with tabs[4]:
    # Add expands for each driver with:
    # - Bar graph showing result at each race
    # - Highest finish of the season callout
    # - Number of fastest laps callout
    # - Number of wins callout
    # - Total points callout
    # - Qualification vs. finish statistic
    points_columns = [col for col in df.columns if col.endswith(('Points', 'SprintPoints'))] 

    # Explicitly define the desired race order
    races_points_only = [
        'Suzuka', 'Silverstone', 'Australia', 'Spa', 'Spain', 'ChinaSprint', 'China', 
        'Baku', 'Canada', 'Monza', 'Abu Dhabi', 'AustriaSprint', 'Austria', 'COTASprint', 'COTA'
    ]

    new_df = df.set_index('Driver')[points_columns]
    new_df = new_df.reset_index()

    for i in range(len(new_df['Driver'])):
        with st.expander(new_df['Driver'][i]):
            driver_name = new_df['Driver'][i]  # Get the driver's name
            driver_points = new_df.iloc[i, 1:].tolist()

            # Create the figure name using the driver's name
            fig_name = f"{driver_name} Points Per Race"

            # Use globals() to dynamically create the variable
            globals()[fig_name] = px.bar(x=races_points_only, y=driver_points, title=fig_name)
            globals()[fig_name].update_xaxes(categoryorder='array', categoryarray=races_points_only)

            # Update x-axis title
            globals()[fig_name].update_xaxes(title_text="Race", categoryorder='array', categoryarray=races_points_only)

            # Update y-axis title
            globals()[fig_name].update_yaxes(title_text="Points") 

            # Access the figure using the dynamic variable name
            st.plotly_chart(globals()[fig_name])  
            st.write('test')

# Race Schedule  
with tabs[5]:
    schedule = pd.DataFrame({
    'Race': ['Pre-Season: Miami', 'Suzuka','Silverstone','Australia','Spa','Spain','China', 
                'Baku','Canada','Monza','Abu Dhabi', 'Austria','COTA'],
    'Date': ['11/13/2024','11/20/2024','12/4/2024','12/18/2024','12/25/2024','1/1/2025','1/8/2025',
             '1/15/2025','1/22/2025','1/29/2025','2/5/2025','2/12/2025','2/26/2025'],
    'Status': ['Final', 'Final', 'Upcoming', 'Upcoming', 'Upcoming', 'Upcoming', 'Upcoming',
               'Upcoming', 'Upcoming', 'Upcoming', 'Upcoming', 'Upcoming', 'Upcoming']
    })

    # CSS to inject contained in a string
    hide_table_row_index = """
    <style>
    thead tr th:first-child {display:none}
    tbody th {display:none}
    </style>
    """
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    st.table(schedule)