from altair.vegalite.v4.schema.channels import Tooltip
# from matplotlib.pyplot import text
import streamlit as st
import numpy as np
import pandas as pd
import time
# from vega_datasets import data
import pickle
import datetime
import pickle
import re
import altair as alt
# import ptvsd
# ptvsd.enable_attach(address=('localhost', 5678))
# Only include this line if you always wan't to attach the debugger
# ptvsd.wait_for_attach()
st.set_page_config(page_title=" Jebah", page_icon="favicon.ico", layout="wide")
# streamlit_pickle = pickle.load(open("gsheet_pickle.p", "rb"))
# test_pickle = pickle.load(open("minortest_pickle.p", "rb"))
alpha = pickle.load(open("apr_21.p", "rb"))
day_sorted_list = np.sort(alpha["aocs_dep"].dt.date.unique()).tolist()
dep_airport_list = np.sort(alpha["Dept_Arp"].unique())

# - [ ]using html in streamlit , looks dreadful
tabs = ["Introduction", "Month-View", "Day-View", "Test_Two"]
page = st . sidebar . radio("SelectView", tabs)


if page == "Introduction":
    st . write("Application for monitoring the Flight Schedule details")
    st . subheader("What is it trying to solve ? ")
    st . markdown("""
    - Looking at operating schedule , schedule work and unscheduled work for a medium to large  station is still done manually ,The system still runs but is not optimized
    - **Analogy** -> If one were asked to assemble a Television before watching  , and contrast with the real world where we just use a remote and start watching Telivision.
    - We are just trying to provide a interface or tools for people to make decision instead of concentrating on making the tools
    - Engineering operations planning is currently manually done in almost all airline and mro operations  , The procedures are nedds to made available for the year 2021 """)
    st . sidebar . write(
        "General Introduction")
# breakpoint()


# Page : Month - View
if page == "Month-View":
    option = st.sidebar.selectbox(
        'Please select Airport?',
        dep_airport_list, key="Month-View")
    selectedMonth = st.sidebar.selectbox("SelectMonth", pd.date_range(
        start='1/1/2021', freq="MS", periods=12).strftime("%b-%y").tolist())
    title_style = """
    <div style="background-color:#001B94",padding:5px;">
    <h1 style ="color:white">Flight Schedule for Station 📈📈 </h1>
    </div>
    """
    st.markdown(title_style, unsafe_allow_html=True)
    'Airport selected:', option
    "Selected-Month :", selectedMonth
    # generating a month days as a list
    day_sorted_list = pd.date_range(start=(pd.to_datetime(selectedMonth, format="%b-%y")),
                                    freq="D", periods=(pd.to_datetime(selectedMonth, format="%b-%y").daysinmonth)).tolist()
    dep_count_list = []
    baseDep_dep_count_list = []
    baseArr_dep_count_list = []
    for india in day_sorted_list:
        test_df = alpha.loc[(alpha["Dept_Arp"] == option) &
                            (alpha["engg_dep"].dt.day == india.day) & (alpha["deptype"] == "Transit") & (alpha["engg_dep"].dt.month == datetime.datetime.strptime(selectedMonth, "%b-%y").month)]

        dep_count_list.append(
            [india.day, "Transit", test_df["engg_dep"].count()])
        # for base departure
        test_df = alpha.loc[(alpha["Dept_Arp"] == option) &
                            (alpha["engg_dep"].dt.day == india.day) & (alpha["deptype"] == "baseDep") & (alpha["engg_dep"].dt.month == datetime.datetime.strptime(selectedMonth, "%b-%y").month)]

        baseDep_dep_count_list.append(
            [india.day, "baseDeparture", test_df["engg_dep"].count()])
        # for base arrival
        test_df = alpha.loc[(alpha["Dept_Arp"] == option) &
                            (alpha["engg_arr"].dt.day == india.day) & (alpha["deptype"] == "baseArr") & (alpha["engg_arr"].dt.month == datetime.datetime.strptime(selectedMonth, "%b-%y").month)]

        baseArr_dep_count_list.append(
            [india.day, "baseArrival", test_df["engg_arr"].count()])
        # make dataframe for each type of data reqwuired
        # transit dataframe
    chart_data = pd.DataFrame(dep_count_list, columns=[
        'DepDay', 'DepType', "Dep_Count"])
    # base departure dataframe
    baseDep_chart_data = pd.DataFrame(baseDep_dep_count_list, columns=[
        'DepDay', 'DepType', "Dep_Count"])
    # base Arrival dataframe
    baseArr_chart_data = pd.DataFrame(baseArr_dep_count_list, columns=[
        'DepDay', 'DepType', "Dep_Count"])
    # st.write(chart_data)
    # st.line_chart(chart_data)
    numbered_day_sorted_list = [x.day for x in day_sorted_list]
    my_chart = alt.Chart(chart_data).mark_line(point=True).encode(
        x=alt.X('DepDay', sort=numbered_day_sorted_list, title='Days Of The Month'
                ),
        y=alt.Y('Dep_Count:Q', title='Count'),

        color='DepType:N',

        tooltip=[alt.Tooltip('Dep_Count'),
                 alt.Tooltip("DepDay"),
                 alt.Tooltip("DepType")],

    ).properties(
        title='Operation Details Per Day in Station'
    )

    text_chart = my_chart.mark_text(
        align='left',
        baseline='top',

    ).encode(
        text='Dep_Count'
    )
    tesla = alt.layer(my_chart, text_chart).interactive()

    st.altair_chart(tesla, use_container_width=True)
    # baseDeparture Chart
    baseDep_my_chart = alt.Chart(baseDep_chart_data).mark_line(point=True).encode(
        x=alt.X('DepDay', sort=numbered_day_sorted_list, title='Days Of The Month'
                ),
        y=alt.Y('Dep_Count:Q', title='Count'),

        color='DepType:N',

        tooltip=[alt.Tooltip('Dep_Count'),
                 alt.Tooltip("DepDay"),
                 alt.Tooltip("DepType")],

    ).properties(
        title='Operation Details Per Day in Station'
    )

    baseDep_text_chart = baseDep_my_chart.mark_text(
        align='left',
        baseline='top',

    ).encode(
        text='Dep_Count'
    )
    baseDep_tesla = alt.layer(
        baseDep_my_chart, baseDep_text_chart).interactive()

    st.altair_chart(baseDep_tesla, use_container_width=True)
    # baseDeparture Chart
    baseArr_my_chart = alt.Chart(baseArr_chart_data).mark_line(point=True).encode(
        x=alt.X('DepDay', sort=numbered_day_sorted_list, title='Days Of The Month'
                ),
        y=alt.Y('Dep_Count:Q', title='Count'),

        color='DepType:N',

        tooltip=[alt.Tooltip('Dep_Count'),
                 alt.Tooltip("DepDay"),
                 alt.Tooltip("DepType")],

    ).properties(
        title='Operation Details Per Day in Station'
    )

    baseArr_text_chart = baseArr_my_chart.mark_text(
        align='left',
        baseline='top',

    ).encode(
        text='Dep_Count'
    )
    baseArr_tesla = alt.layer(
        baseArr_my_chart, baseArr_text_chart).interactive()

    st.altair_chart(baseArr_tesla, use_container_width=True)
    # st.write(baseArr_chart_data)

# Page : Day -View
if page == "Day-View":
    option = st.sidebar.selectbox(
        'Please select Airport?',
        dep_airport_list, key="Day-View")
    selectedStartDate = st.sidebar.date_input(
        "Select-Start-Date", datetime.date(2021, 1, 31), key="startDate")
    selectedstartTime = st.sidebar.time_input(
        'select-start-time', datetime.time(8, 45), key="startTime")
    # made sure the end date is the same day or the next day
    selectedEndDate = st.sidebar.date_input(
        "SelectEndDate", min_value=selectedStartDate, max_value=(selectedStartDate+datetime.timedelta(days=1)))

    selectedEndTime = st.sidebar.time_input(
        'select-start-time', datetime.time(8, 45), key="endTime")
    # end date shold be same or next day as start date
    if (selectedStartDate != selectedEndDate) and (selectedEndDate != selectedStartDate+datetime.timedelta(days=1)):
        st.sidebar.error(
            "Error:End Date should be same as Start day or (Start Day +1)")
    # end date time should be greater than start date time
    if datetime.datetime.combine(selectedEndDate, selectedEndTime) <= datetime.datetime.combine(selectedStartDate, selectedstartTime):
        st.error("Error: End Date Time should be greater  than Start Date Time")
    "Start-Date", selectedStartDate
    "Start-Time", selectedstartTime
    "End-Date", selectedEndDate
    "End-Time", selectedEndTime
