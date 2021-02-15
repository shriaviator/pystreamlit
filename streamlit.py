import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import pickle
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from pydatetime import daycreator
import pickle
import re

alpha = pickle.load(open("save.p", "rb"))
# dropping columns for final assymbly
alpha = alpha.drop(['moddeptime', 'mod_arr_time', 'Freq',
                    'Modeffdate', 'moddisdate', 'actual_days'], axis=1)
alpha = pd.melt(alpha, id_vars=['Dept Arp', 'engg_arr', 'engg_dep', 'deptype', 'Arvl Arp', 'Flt Desg',
                                'Text Comment', 'Block Time'], value_vars=['D1', 'A1', 'D2', 'A2', 'D3', 'A3', 'D4',
                                                                           'A4', 'D5', 'A5', 'D6', 'A6', 'D7', 'A7', 'D8', 'A8', 'D9', 'A9', 'D10',
                                                                           'A10', 'D11', 'A11', 'D12', 'A12', 'D13', 'A13', 'D14', 'A14', 'D15',
                                                                           'A15', 'D16', 'A16', 'D17', 'A17', 'D18', 'A18', 'D19', 'A19', 'D20',
                                                                           'A20', 'D21', 'A21', 'D22', 'A22', 'D23', 'A23', 'D24', 'A24', 'D25',
                                                                           'A25', 'D26', 'A26', 'D27', 'A27', 'D28', 'A28', 'D29', 'A29', 'D30',
                                                                           'A30', 'D31', 'A31'])
my_list_ray = ['D1', 'A1', 'D2', 'A2', 'D3', 'A3', 'D4',
               'A4', 'D5', 'A5', 'D6', 'A6', 'D7', 'A7', 'D8', 'A8', 'D9', 'A9', 'D10',
               'A10', 'D11', 'A11', 'D12', 'A12', 'D13', 'A13', 'D14', 'A14', 'D15',
               'A15', 'D16', 'A16', 'D17', 'A17', 'D18', 'A18', 'D19', 'A19', 'D20',
               'A20', 'D21', 'A21', 'D22', 'A22', 'D23', 'A23', 'D24', 'A24', 'D25',
               'A25', 'D26', 'A26', 'D27', 'A27', 'D28', 'A28', 'D29', 'A29', 'D30',
               'A30', 'D31', 'A31']
filter_my_list_ray = list(filter(lambda x: "A" not in x, my_list_ray))
print(list(filter_my_list_ray))
dep_count_list = []


for india in filter_my_list_ray:
    test_df = alpha.loc[(alpha["Dept Arp"] == "DEL") &
                        (alpha["variable"] == india)]
    test_df = test_df[test_df.value != False].sort_values(by="value")
    dep_count_list.append(test_df["value"].count())

st.write("Here's our first attempt at using data to create a table:")
chart_data = pd.DataFrame({
    'Day': filter_my_list_ray,
    'Departure_Count': dep_count_list
})

st.line_chart(chart_data)
if st.checkbox('Show dataframe'):
    st.line_chart(chart_data)


option = st.selectbox(
    'please select a station?',
    chart_data['Day'])

'You selected: ', option

option = st.sidebar.selectbox(
    'Which number do you like best?',
    chart_data['Day'])

'You selected:', option
