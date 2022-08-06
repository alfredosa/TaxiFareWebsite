import streamlit as st
import requests
import urllib
import datetime
'''
# Predicting a Taxi fare in NY!
'''
url = 'https://taxifare.lewagon.ai/predict'
st.markdown('''
Welcome to the page, we are happy to predict a fare for you.
''')

'''

1. To be able to make a prediction we need the following details from you:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Fill the details bellow to get a prediction:
'''
with st.form("taxifareform"):
    date = st.date_input("Date"),
    time = st.time_input('Time', datetime.time(8, 45)),
    picklat = st.text_input("Pickup Latitud",'40.783282')
    picklong = st.text_input("Pickup Longitud",'-73.950655')
    droplat = st.text_input("Dropoff Latitud",'40.769802')
    droplong = st.text_input("Dropoff Longitud",'-73.984365')
    slider_val = st.slider("How many people?",min_value=1,max_value=8)
    ### BUTTON
    submitted = st.form_submit_button("Get Taxi Fare")
    if submitted:
        params = {
        "pickup_datetime": date[0].strftime("%Y-%m-%d") + " " + time[0].strftime("%H:%M:%S"),
        "pickup_longitude": picklong,
        "pickup_latitude": picklat,
        "dropoff_longitude": droplong,
        "dropoff_latitude": droplat,
        "passenger_count": slider_val
        }
        urlparams = url +"?"+ urllib.parse.urlencode(params)
        prediction = requests.get(url,params=params).json()
        st.write("# Taxi fare is: ", "%.2f" % round(prediction['fare'], 2))

st.write("Thank you for using this service :)")
