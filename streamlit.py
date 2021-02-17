from altair.vegalite.v4.schema.channels import Tooltip
# from matplotlib.pyplot import text
import streamlit as st
import numpy as np
import pandas as pd
import time

import pickle
import datetime
import pickle
import re
import altair as alt
st.set_page_config(page_title=" Jebah", page_icon="favicon.ico", layout="wide")
streamlit_pickle = pickle.load(open("gsheet_pickle.p", "rb"))

alpha = streamlit_pickle[0]
filter_my_list_ray = streamlit_pickle[1]
dep_airport_list = streamlit_pickle[2]
dep_count_list = []


option = st.sidebar.selectbox(
    'Please select Airport?',
    dep_airport_list)
# - [ ]using html in streamlit , looks dreadful
title_style = """
<div style="background-color:#001B94",padding:5px;">
<h1 style ="color:white">Flight Details for Station 💉💉 </h1>
</div>
"""
st.markdown(title_style, unsafe_allow_html=True)


'Airport selected:', option

for india in filter_my_list_ray:
    if (option == "All_Stations"):
        my_df = alpha.loc[
            (alpha["variable"] == india)]

        my_df = my_df[my_df.value != False].sort_values(by="value")
        dep_count_list.append(my_df["value"].count())

    else:
        test_df = alpha.loc[(alpha["Dept Arp"] == option) &
                            (alpha["variable"] == india)]
        test_df = test_df[test_df.value != False].sort_values(by="value")
        dep_count_list.append(test_df["value"].count())


chart_data = pd.DataFrame({
    'Day of month': filter_my_list_ray,
    'Departure_Count': dep_count_list,
    "label": dep_count_list,
})
# st.line_chart(chart_data)
my_chart = alt.Chart(chart_data).mark_line(point=True).encode(
    x=alt.X('Day of month', sort=filter_my_list_ray,
            ),
    y='Departure_Count',
    tooltip=[alt.Tooltip('Departure_Count'),
             alt.Tooltip("Day of month")],



).properties(
    title='Departures Per Day in Station'
)

text_chart = my_chart.mark_text(
    align='left',
    baseline='top',

).encode(
    text='Departure_Count'
)
tesla = alt.layer(my_chart, text_chart).interactive()

st.altair_chart(tesla, use_container_width=True)
