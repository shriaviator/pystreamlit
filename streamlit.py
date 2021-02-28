from altair.vegalite.v4.schema.channels import Tooltip
# from matplotlib.pyplot import text
import streamlit as st
import numpy as np
import pandas as pd
import time
from vega_datasets import data
import pickle
import datetime
import pickle
import re
import altair as alt
st.set_page_config(page_title=" Jebah", page_icon="favicon.ico", layout="wide")
streamlit_pickle = pickle.load(open("gsheet_pickle.p", "rb"))
test_pickle = pickle.load(open("minortest_pickle.p", "rb"))
alpha = test_pickle
day_sorted_list = streamlit_pickle[1]
dep_airport_list = streamlit_pickle[2]
dep_count_list = []


option = st.sidebar.selectbox(
    'Please select Airport?',
    dep_airport_list)
# - [ ]using html in streamlit , looks dreadful

tabs = ["Introduction", "MonthView", "Test_One", "Test_Two"]
page = st . sidebar . radio("SelectView", tabs)


for india in day_sorted_list:
    test_df = alpha.loc[(alpha["Dept Arp"] == option) &
                        (alpha["depDay"] == india) & (alpha["deptype"] == "Transit")]

    dep_count_list.append([india, "Transit", test_df["depDay"].count()])
    test_df = alpha.loc[(alpha["Dept Arp"] == option) &
                        (alpha["depDay"] == india) & (alpha["deptype"] == "baseDep")]

    dep_count_list.append([india, "baseDeparture", test_df["depDay"].count()])
    test_df = alpha.loc[(alpha["Dept Arp"] == option) &
                        (alpha["depDay"] == india) & (alpha["deptype"] == "baseArr")]

    dep_count_list.append([india, "baseArrival", test_df["depDay"].count()])


# for india in filter_my_list_ray:
#     if (option == "All_Stations"):
#         my_df = alpha.loc[
#             (alpha["variable"] == india)]

#         my_df = my_df[my_df.value != False].sort_values(by="value")
#         dep_count_list.append(my_df["value"].count())

#     else:
#         test_df = alpha.loc[(alpha["Dept Arp"] == option) &
#                             (alpha["variable"] == india)]
#         test_df = test_df[test_df.value != False].sort_values(by="value")
#         dep_count_list.append(test_df["value"].count())


chart_data = pd.DataFrame(dep_count_list, columns=[
                          'DepDay', 'DepType', "Dep_Count"])
# st.line_chart(chart_data)
my_chart = alt.Chart(chart_data).mark_bar(point=True).encode(
    x=alt.X('DepDay', sort=day_sorted_list, title='Days Of The Month'
            ),
    y=alt.Y('Dep_Count:Q', title='Count'),

    color='DepType:N',

    tooltip=[alt.Tooltip('Dep_Count'),
             alt.Tooltip("DepDay"),
             alt.Tooltip("DepType")],



).properties(
    title='Operation Details Per Day in Station'
)

text_chart = my_chart.mark_bar(
    align='left',
    baseline='top',

).encode(
    text='Dep_Count'
)
tesla = alt.layer(my_chart, text_chart).interactive()


if page == "Introduction":
    st . write("Application for monitoring the Flight Schedule details")
    st . subheader("What is it trying to solve ? ")
    st . markdown(""" 
    - Looking at operating schedule , schedule work and unscheduled work for a medium to large  station is still done manually ,The system still runs but is not optimized
    - Tv remote example {keyword interface }
    - We are just trying to provide a interface or tools for people to make decision instead of concentrating on making the tools  
    - Engineering operations planning is currently manually done in almost all airline and mro operations in India , The procedures are nedds to made available for the year 2021 """)
    st . sidebar . write(
        "General Introduction")

if page == "MonthView":
    title_style = """
    <div style="background-color:#001B94",padding:5px;">
    <h1 style ="color:white">Flight Schedule for Station 💉💉 </h1>
    </div>
    """
    st.markdown(title_style, unsafe_allow_html=True)
    'Airport selected:', option
    st.altair_chart(tesla, use_container_width=True)

if page == "Test_One":
    source = data.stocks()
    print()

    ref_chart = alt.Chart(source).mark_line().encode(
        x='date',
        y='price',
        color='symbol',
        strokeDash='symbol',
    )
    st.altair_chart(ref_chart, use_container_width=True)
