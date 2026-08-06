import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title='Weather App',page_icon='🌦️')
st.title('🌦️Weather APP')
st.write('Enter the city name and click on the button to get weather app')
city = st.text_input('Enter the city name')
API_KEY= os.getenv('API_KEY')
API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
if st.button('fetch weather data'):
    response = requests.get(API_URL)
    if(response.status_code==200):
        st.success('weather data fetched successfully!')
        data = response.json()
        
        # Extract the values
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather =data['weather'][0]['main']
        name =data['name']
        country =data['sys']['country']
        st.subheader(f'{name},{country}')

        #create 4 columns
        col1,col2 =st.columns(2)
        col3,col4 =st.columns(2)

        #Display the values in UI........
        col1.metric('Temperature',f'🌡️{temperature}°C')
        col2.metric('humidity',f'💦{humidity}%')
        col3.metric('wind_speed',f'🌪️{wind_speed}m/s')
        col4.metric('weather',f'☔{weather}')
    else:
        st.error('city name')
