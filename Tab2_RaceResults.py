import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

# Expands for each race: Reports race results like post race screen
def Tab2(races,df,race_place,race_points):
    with st.expander("Pre-Season: Miami"):
        st.subheader("Winner: Joshua")
        MiamiResults = pd.DataFrame({
            'Place': ['1','2','3','4','16','17','18','19'],
            'Driver': ['Joshua','Nick','Patrick','Erick','Yeti','Boz','Del','Gary'],
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
    with st.expander("Postseason: Monaco"):
        st.subheader("Winner: Brently")
        MiamiResults = pd.DataFrame({
            'Place': ['1','10','17','DNF','DNF','DNF'],
            'Driver': ['Brently','Joshua','Boz','Nick','Del','Eddie'],
            'Qualifying': ['3','15','19','2','1','18']
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