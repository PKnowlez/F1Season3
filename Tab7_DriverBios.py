import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

def Tab7(team_df,drivers_points_df):
    
    # comment
    def read_text_file(file_path):
        with open(file_path, 'r') as f:
            text = f.read()
        return text
    
    for i in range(len(team_df['Team'])):
        with st.expander(team_df['Team'][i]):
            team_name = team_df['Team'][i]  # Get the team's name
            
            # Get drivers for the current team
            drivers_in_team = drivers_points_df[drivers_points_df['Team'] == team_name]['Driver'].unique()

            # Creates the layout for each expand
            col5, col6 = st.columns(2)
            with col5:
                # Display the first driver (if available)
                if len(drivers_in_team) > 0:
                    st.write(f"**Driver Bio: {drivers_in_team[0]}**") 
                    driver_image = Image.open(f"./Bios/{drivers_in_team[0]}.jpg")
                    st.image(driver_image)
                    file_content = read_text_file(f"./Bios/{drivers_in_team[0]}.txt")
                    st.markdown(file_content)
            with col6:
                # Display the second driver (if available)
                if len(drivers_in_team) > 1:
                    st.write(f"**Driver Bio: {drivers_in_team[1]}**")
                    driver_image = Image.open(f"./Bios/{drivers_in_team[1]}.jpg")
                    st.image(driver_image)
                    file_content = read_text_file(f"./Bios/{drivers_in_team[1]}.txt")
                    st.markdown(file_content)

    return