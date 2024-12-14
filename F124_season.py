import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

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
    if df.loc[0,fastest_lap[i]] == 'Z':
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
    # Author and add news articles for each race with headlines and such
    australia1 = Image.open("./Images/Australia_Start.png")
    australia2 = Image.open("./Images/Australia_Collage.png")
    australia3 = Image.open("./Images/Australia_Side_Shot.png")
    st.subheader('Australia Recap: A Rumble Down Under')
    st.markdown('''
                tldr; Australia did not disappoint. Safety cars, front wings destroyed, questionable restarts, engines blown, drivers fuming, DNFs, a DNS, and a new race winner. 
                '''+'''
                With race hype at an all time high the drivers jumped into discord and silently sat waiting for the race to begin. Nerves were frayed, but when the lights went green in qualifying the drivers took to the streets of Albert Park without much trouble. The Red Bull pairing failed to make it out of Q1 and Alpine’s #2 driver Eddie totaled his car beyond repair, making it impossible for him to set a lap time during Q2. The final results of Q3 saw Alpine’s Joshua take home another pole position, with McLaren’s Nick, Aston Martin’s Del, and VCARB’s Patrick completing the first two rows. The Ferrari pairing occupied the third row and McLaren’s Travis and VCARB’s Brently rounded out the top eight on the fourth row of the grid. The rest of the field found themselves starting near the back, which to some strategists was the right move to ensure their drivers survived the first corner.
                ''')
    st.image(australia1)
    st.markdown('''
                When the five lights went out, the drivers quickly proceeded down the straight into Turn 1 where the top few drivers made it through fairly clean. However, Zane’s Ferrari was caught up in an incident on his way through Turn 2. This ended up proving to be a detrimental loss for Zane early in the race. Erick was able to make up a place into fourth passing Del and avoiding contact through the first few corners. 
                '''+'''
                As the race continued Alpine’s dominant driver Joshua took an early lead but was unable to break free from McLaren’s top contender Nick. As the front of the pack continued, Erick miraculously avoided contact with both Patrick and Nick in Turn 3 as he found himself in the gravel. This maneuver would have normally left him high and dry, but an early VSC and safety car allowed Erick to get right back into the groove. 
                ''')
    st.image(australia2)
    st.markdown('''
                Track limits were heavily enforced across the field as drivers tested the race director’s new regulations. Prior to the start of the race the league was informed that, due to sloppiness and abuse of the rules by Alpine’s Joshua at Silverstone, any corner cutting would be strictly recorded and penalties would be awarded for drivers who broke the rules three or more times throughout the race. For most these penalties were minor and did not end up changing the outcome of the race. However in the post race driver’s meeting there was a minor uproar that the regulations were too strict. Only time will tell if these regulations will remain or if the race director will renege their stance.
                '''+'''
                With just nine laps to go a late safety car bunched up the drivers and allowed some to take advantage of a less impactful pitstop. With Joshua still in first, Nick tailing him, and Erick following in third, the queue of cars cautiously took the final few corners of Lap 22 waiting for Joshua to throttle up. Waiting on bated breath, Nick and Erick pounced as Joshua launched only to find Joshua jump off the throttle for a short moment causing a multitude of front wings to be damaged. Regardless, no penalties were called and the drivers mustered what they could with their damaged vehicles. A tight battle ensued up front which ultimately saw McLaren’s Nick take home his first win of the season with Alpine’s Joshua right behind. 
                ''')
    st.image(australia3)
    st.markdown('''
                Rounding out the podium was Ferrari's Erick, who moved up from 5th to 3rd. Just behind him the two VCARB drivers had their best team finish of the season with Patrick finishing 4th, and driver of the day Brently moving up from 8th to 5th. Del was unable to fully recover from the early setbacks and ended in 11th with McLaren’s Travis just behind in 12th, and Alpine’s 7th place wunderkind Eddie falling all the way back to 13th. Rounding out our finishers today was Ferrari’s Zane in 15th. For Red Bull, this will be a qualifying and race to take notes from and improve upon as both drivers ended up unable to cross the finish line. Aston Martin again ran with just a single driver today as Gary was sadly watching the Knicks fall to the Hawks.
                '''+'''
                After all the engines were turned off and points totalled, battles for rank in both the World Driver’s and Constructor’s Championships have begun to heat up. McLaren begins to close the gap to Alpine and leap frogs Ferrari into second. In the Driver’s Championship, we saw both of the VCARB drivers overtake Ferrari’s Zane, but the leaders Joshua, Nick, and Erick remain the same. Next our drivers take to the Belgian forest in Spa where they will test their mettle against the highspeed Eau Rouge and longest track on the calendar.
                ''')
    st.markdown('''
                <p style="color:lightgray;">Thursday 12/11/2024 - Patrick Knowles with credit Erick & Nick</p>
                ''',
                unsafe_allow_html=True,)
    
    st.divider()
    australia_circuit = Image.open("./Images/Australia_Circuit.png")
    st.subheader('Race Week - Australia')
    st.markdown('''
                This week the drivers will be “defying gravity” while racing upside down in Melbourne. The real question is whether or not the league continues to let Alpine and Joshua cook? Or maybe more fittingly, will the league let Joshua put another shrimp on the barbie? Only the streets of Albert Park will be able to answer these questions.
                '''+'''
                Albert Park Circuit provides the first street circuit of the year, which without a doubt is set to create some sparks. With the first heavy braking Turn 1 of the calendar, the start of this race will likely turn into an abbreviated game of Survivor. From there the drivers will be challenged by tight walls coming out of Turn 2 and Turn 5 as they queue up into the highspeed Sector 2. Sector 3’s heavy braking zones will provide tantalizing opportunities for the drivers to throw dummies, lick it and send it, and hopefully keep all the carbon fiber on their cars
                ''')
    st.image(australia_circuit)
    st.markdown('''
                The league took a short pause from running down under last season. Which means the most recent winner here is current Ferrari driver and previous Mercedes driver Erick, who took home a commanding win with a lead of 18 seconds over McLaren’s Nick. Rounding out the podium was  retired Mercedes driver turned steward Marcus. If Silverstone’s race is any evidence of how close the drivers plan to race this week, we will certainly see an exciting race in the capital of Victoria. With nearly no room for run off, mistakes will be magnified, and incidents are sure to become heated.
                '''+'''
                <p style="color:lightgray;">Saturday 12/7/2024 - Patrick Knowles</p>
                ''',
                unsafe_allow_html=True,
                )

    st.divider()
    silverstone0 = Image.open("./Images/Silverstone_Start.png")
    silverstone1 = Image.open("./Images/Silverstone_Final_Turn.png")
    silverstone2 = Image.open("./Images/Silverstone_PK_Zane.png")
    st.subheader('Silverstone Recap: “007 You Only Win Twice”')
    st.image(silverstone0)
    st.markdown('''
                Another week, another race. The sun mercifully shone down on the British Isles and provided the perfect weather for an eventful race. Reigning WDC Nick, and Alpine’s top driver Joshua, battled it out for 26 laps straight. Joshua took the win after a little bit of questionable contact and a helpful dose of backmarker blocking. This is Alpine and Joshua’s second win of the season. Alpine also had some 007 magic from their second seat, Eddie, who had 0 intention of racing, 0 practice, and placed 7th. Coincidentally this was also his second time placing 7th this season. Let’s see if this pattern continues for the French outfit.
                ''')
    st.image(silverstone1)
    st.markdown('''
                The podium was rounded out by Ferrari ace, Erick, who raced a lonely set of laps around the hallowed airfield. Ferrari’s other driver Zane battled with VCARB’s Patrick in a tightly contested tango where the drivers had opposite tire strategies (softs to mediums and mediums to softs respectively). However, in the end, a bit of contact left Zane just out of reach on the final lap.
                ''')
    st.image(silverstone2)
    st.markdown('''
                Further down the field the two Red Bull drivers Yeti and Boz sparred for the entire race, ending in 6th and 11th after a late error by Boz. Which allowed VCARB’s Brently to make up a place after a muddled start, and end in 8th. Finally, rounding out our grid this week were the Aston Martins with Gary finishing in 19th and Del MIA for this week’s bout.
                '''+'''
                Alpine’s Joshua takes an early strong lead in the WDC with his back-to-back wins. His efforts, along with Jr.'s, have propelled the team into the lead for the WCC as well. As it stands today Alpine leads the way, followed by Ferrari and McLaren who are separated by mere points. The WDC currently stands with Joshua, Nick, and Zane in the top three with Erick just one point behind his Ferrari teammate in 4th. See you all down under where the league takes to the converted streets of Albert Park.
                ''')
    st.markdown('''
                <p style="color:lightgray;">Wednesday 12/4/2024 - Patrick Knowles with credit Eddie & Nick</p>
                ''',
                unsafe_allow_html=True,)

    st.divider()
    trophy = Image.open("./Images/Trophy.png")
    st.subheader('Race Week - Silverstone')
    st.markdown('''
                Rise and shine gamers, its race week! This week The Alternative will take to the famed and hallowed pavement of Silverstone. With a week off for the Thanksgiving holiday, the drivers should not be worried about meeting the minimum weight limit at the end of the race. With the season still young, all drivers are still hopeful they can make a meaningful impact on both championship races.
                '''+'''
                Additionally, the league’s president, Mr. Erick Tavera, is proud to unveil the crown jewel of this year’s competition, the champion’s trophy. Derived from F1’s cancelled COTA trophies, The Alternative’s World Driver’s Champion and Constructor’s Champions will receive a commemorative trophy marking their achievement from throughout the season. The Pirelli tire the champion stands upon has each of this season’s tracks encircling the perimeter of the tire. The races won by each driver or constructor will be highlighted in gold. Additionally, the bottom of the base will include the driver’s and constructor’s records and accomplishments from throughout the season.
                ''')
    st.image(trophy)
    st.markdown('''
                <p style="color:lightgray;">Sunday 12/1/2024 - Patrick Knowles</p>
                ''',
                unsafe_allow_html=True,)

    st.divider()
    st.subheader('Suzuka & Pre-Season Recap')
    st.markdown('''
                With a lovely pre-season in Miami complete where 8 of the league's 12 drivers and all 6 constructors took to the streets around Hard Rock Stadium, the lights went out in Suzuka to an aborted start. With a multiple car incident that sent the whole grid into turmoil,the race director determined it was best to have a full restart. One of our top qualifiers, VCARB's Patrick, fell back two positions at the start and near the end of the first lap attempted to make up those positions going into the Hitachi Astemo Chicane. This maneuver failed and ended with a slow down into the chicane allowing many of our drivers to make up spots against the AI and other drivers. The remainder of the race saw only a few spins, beachings, and other minor mishaps that affected a few of the final standings. Big winners from this race include VCARB's Brentuar as well as Aston Martin's Del. Alpine's Joshua took home the win and the fastest lap with McLaren's reigning champion Nick coming in second and Del rounding out the podium.
                ''' + '''
                With the results final, Alpine takes an early lead in the Constructors’ Championship. Alpine's Joshua is also leading the Driver's Championship. Reigning champion Nick finds himself in second place in the Driver's Championship with his team, McLaren, also slotting into second overall in the Constructors’ Championship. Ferrari, Aston Martin, VCARB, and Red Bull respectively make up the rest of the Constructors’ Championship standings.
                '''+'''
                <p style="color:lightgray;">Thursday 11/21/2024 - Patrick Knowles</p>
                ''',
                unsafe_allow_html=True,)

# Standings
with tabs[1]:
    totals = team_race_totals.T
    constructor_sorted = totals.sort_values('COTAPoints', ascending=False)
    constructor_sorted = constructor_sorted.reset_index() 
    constructor_totals = pd.DataFrame({
    'Team': constructor_sorted['Team'],
    'Points': constructor_sorted['COTAPoints'],
    })

    totals = driver_race_totals.T
    driver_sorted = totals.sort_values('COTAPoints', ascending=False)
    driver_sorted = driver_sorted.reset_index() 
    driver_totals = pd.DataFrame({
    'Driver': driver_sorted['Driver'],
    'Points': driver_sorted['COTAPoints'],
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

            # Use globals() to dynamically create the variable
            globals()[fig_name] = px.bar(x=team_races_points_only, y=team_points, title=fig_name)
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

            # 15 unique colors
            colors = [
                '#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', 
                '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', 
                '#800000'
            ]

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

    # --------------------- #
    # Create the figure name
    fig_name4 = "Average Positions Gained or Lost Per Race"

    avg_changed_df = pd.DataFrame({
        'Driver': new_df['Driver'].copy(),
        'Average Changed': average_changed
        })
    avg_changed_df = avg_changed_df.sort_values(by='Average Changed', ascending=False)

    # Create a list of colors based on the values in average_changed
    colors = ['green' if val >= 0 else 'red' for val in avg_changed_df['Average Changed']]
    
    # Use globals() to dynamically create the variable with the color list
    globals()[fig_name4] = px.bar(x=avg_changed_df['Driver'], y=avg_changed_df['Average Changed'], 
                                title=fig_name4, color=colors,
                                color_discrete_map="identity")

    # Update x-axis title
    globals()[fig_name4].update_xaxes(title_text="Driver")

    # Update y-axis title
    globals()[fig_name4].update_yaxes(title_text="Positions Changed")

    # --------------------- #
    # Create the figure name
    fig_name5 = "Points Per Driver"

    drivers_points_df = pd.DataFrame({
        'Driver': new_df['Driver'].copy(),
        'Points': drivers_total_points
        })
    drivers_points_df = drivers_points_df.sort_values(by='Points', ascending=False)

    # 15 unique colors
    colors = [
        '#FFD700', '#C0C0C0', '#CD7F32', '#0068c9', '#0068c9', '#0068c9', '#0068c9', 
        '#0068c9', '#0068c9', '#0068c9', '#0068c9', '#0068c9'
    ]
    
    # Use globals() to dynamically create the variable with the color list
    globals()[fig_name5] = px.bar(x=drivers_points_df['Driver'], y=drivers_points_df['Points'], 
                                title=fig_name5, color=colors,
                                color_discrete_map="identity")

    # Update x-axis title
    globals()[fig_name5].update_xaxes(title_text="Driver")

    # Update y-axis title
    globals()[fig_name5].update_yaxes(title_text="Points")

    # --------------------- #
    # Create the figure name
    fig_name6 = "Average Qualifying Position"

    avg_qualifying_df = pd.DataFrame({
        'Driver': new_df['Driver'].copy(),
        'Qualifying': average_qualifying
        })
    avg_qualifying_df = avg_qualifying_df.sort_values(by='Qualifying', ascending=True)

    # 15 unique colors
    colors = [
        '#FFD700', '#C0C0C0', '#CD7F32', '#0068c9', '#0068c9', '#0068c9', '#0068c9', 
        '#0068c9', '#0068c9', '#0068c9', '#0068c9', '#0068c9'
    ]
    
    # Use globals() to dynamically create the variable with the color list
    globals()[fig_name6] = px.bar(x=avg_qualifying_df['Driver'], y=avg_qualifying_df['Qualifying'], 
                                title=fig_name6, color=colors,
                                color_discrete_map="identity")

    # Update x-axis title
    globals()[fig_name6].update_xaxes(title_text="Driver")

    # Update y-axis title
    globals()[fig_name6].update_yaxes(title_text="Qualifying Place")

    # --------------------- #
    # Create the figure name
    fig_name7 = "Average Place"

    avg_place_df = pd.DataFrame({
        'Driver': new_df['Driver'].copy(),
        'Place': average_place
        })
    avg_place_df = avg_place_df.sort_values(by='Place', ascending=True)

    # 15 unique colors
    colors = [
        '#FFD700', '#C0C0C0', '#CD7F32', '#0068c9', '#0068c9', '#0068c9', '#0068c9', 
        '#0068c9', '#0068c9', '#0068c9', '#0068c9', '#0068c9'
    ]
    
    # Use globals() to dynamically create the variable with the color list
    globals()[fig_name7] = px.bar(x=avg_place_df['Driver'], y=avg_place_df['Place'], 
                                title=fig_name7, color=colors,
                                color_discrete_map="identity")

    # Update x-axis title
    globals()[fig_name7].update_xaxes(title_text="Driver")

    # Update y-axis title
    globals()[fig_name7].update_yaxes(title_text="Place")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        button_text = "Points Leader: " + drivers_points_df.loc[drivers_points_df['Points'].idxmax(), 'Driver']
        st.button(button_text,key='Points Leader')
    with col2:
        button_text = "Positions Gained Leader: " + avg_changed_df.loc[avg_changed_df['Average Changed'].idxmax(), 'Driver']
        st.button(button_text,key='Positions Gained Leader')
    with col3:
        button_text = "Qualifying Leader: " + avg_qualifying_df.loc[avg_qualifying_df['Qualifying'].idxmin(), 'Driver']
        st.button(button_text,key='Qualifying Leader')
    with col4:
        button_text = "Place Leader: " + avg_place_df.loc[avg_place_df['Place'].idxmin(), 'Driver']
        st.button(button_text,key='Place Leader')
    col5, col6 = st.columns(2)
    with col5:
        st.plotly_chart(globals()[fig_name5])
        st.plotly_chart(globals()[fig_name6])
    with col6:
        st.plotly_chart(globals()[fig_name4])
        st.plotly_chart(globals()[fig_name7])

# Race Schedule  
with tabs[6]:
    schedule = pd.DataFrame({
    'Race': ['Pre-Season: Miami', 'Suzuka','Silverstone','Australia','Spa','Spain','China & Sprint', 
                'Baku','Canada','Monza','Abu Dhabi', 'Austria & Sprint','COTA & Sprint'],
    'Date': ['11/13/2024','11/20/2024','12/4/2024','12/11/2024','12/18/2024','1/1/2025','1/8/2025','1/15/2025',
             '1/22/2025','1/23/2025','1/29/2025','2/5/2025','2/12/2025'],
    'Status': ['Final', 'Final', 'Final', 'Final', 'Upcoming', 'Tentative', 'Tentative',
               'Tentative', 'Tentative', 'Tentative', 'Tentative', 'Tentative', 'Tentative']
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