import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Page Setup
st.set_page_config(page_title="Weather Analytics Dashboard", page_icon="🌤️", layout="wide")

st.title("🌤️ Real-Time Weather & Analytics Dashboard")
st.write("Built by Faiz Khan | Powered by Python & REST APIs")

# User Input for City Selection
city = st.text_input("Enter City Name:", "Bangalore")

if st.button("Fetch Weather Data"):
    # API Call (Using wttr.in JSON format)
    url = f"https://wttr.in/{city}?format=j1"
    
    with st.spinner("Fetching data from API..."):
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract Current Weather Details
            current_condition = data['current_condition'][0]
            temp_c = current_condition['temp_C']
            humidity = current_condition['humidity']
            weather_desc = current_condition['weatherDesc'][0]['value']
            wind_speed = current_condition['windspeedKmph']

            # Display Key Metrics in Cards
            col1, col2, col3, col4 = st.columns(4)
            col1.metric(label="Temperature", value=f"{temp_c} °C")
            col2.metric(label="Humidity", value=f"{humidity} %")
            col3.metric(label="Condition", value=weather_desc)
            col4.metric(label="Wind Speed", value=f"{wind_speed} km/h")

            # Extract Hourly Forecast for Chart Visualizations
            st.divider()
            st.subheader("📊 Today's Hourly Temperature Trend")
            
            hourly_data = data['weather'][0]['hourly']
            
            # Convert JSON data into a Structured Pandas DataFrame (Data Analysis)
            df = pd.DataFrame(hourly_data)
            df['time'] = df['time'].apply(lambda x: f"{int(x)//100:02d}:00") # Format time string
            df['tempC'] = df['tempC'].astype(int)
            df['humidity'] = df['humidity'].astype(int)

            # Interactive Plotly Chart
            fig = px.line(df, x='time', y='tempC', title=f"Hourly Temperature Forecast for {city.title()}",
                          labels={'time': 'Time of Day', 'tempC': 'Temperature (°C)'},
                          markers=True)
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Show Raw Data Table
            with st.expander("View Raw Processed Dataset"):
                st.dataframe(df[['time', 'tempC', 'humidity', 'weatherDesc']])

        else:
            st.error("Could not fetch data. Check the city name and try again.")