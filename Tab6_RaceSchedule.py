import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import math
from PIL import Image

def Tab6():
    schedule = pd.DataFrame({
    'Race': ['Pre-Season: Miami',
             'Suzuka',
             'Silverstone',
             'Australia',
             'Spa',
             'Spain',
             'China & Sprint',
             'Baku',
             'Canada',
             'Monza',
             'Abu Dhabi',
             'Austria & Sprint',
             'COTA & Sprint'],
    'Date': ['11/13/2024',
             '11/20/2024',
             '12/4/2024',
             '12/11/2024',
             '1/1/2025',
             '1/2/2025',
             '1/8/2025',
             '1/15/2025',
             '1/22/2025',
             '1/23/2025',
             '1/29/2025',
             '2/5/2025',
             '2/12/2025'],
    'Status': ['Final',
               'Final',
               'Final',
               'Final',
               'Upcoming',
               'Tentative',
               'Tentative',
               'Tentative',
               'Tentative',
               'Tentative',
               'Tentative',
               'Tentative',
               'Tentative']
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

    # Print Table
    st.table(schedule)