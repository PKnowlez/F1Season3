import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

def Tab5(new_df,average_changed,drivers_total_points,average_qualifying,average_place,):
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

    # Unique colors
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

    return 