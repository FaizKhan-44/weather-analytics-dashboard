import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Weather Analytics Dashboard", page_icon="🌤️", layout="wide")

st.title("Real-Time Weather & Analytics Dashboard")
st.caption("Built by Faiz Khan | Streamlit & wttr.in API")

city = st.text_input("Enter City Name:", value="Bangalore").strip()

if st.button("Fetch Weather Data"):
    endpoint = f"https://wttr.in/{city}?format=j1"
    
    with st.spinner("Fetching data..."):
        try:
            res = requests.get(endpoint, timeout=8)
            
            if res.status_code == 200:
                payload = res.json()
                current = payload['current_condition'][0]
                
                # Metric display
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Temperature", f"{current['temp_C']} °C")
                c2.metric("Humidity", f"{current['humidity']} %")
                c3.metric("Condition", current['weatherDesc'][0]['value'])
                c4.metric("Wind Speed", f"{current['windspeedKmph']} km/h")

                st.divider()
                st.subheader("Today's Hourly Temperature Trend")
                
                hourly = payload['weather'][0]['hourly']
                df = pd.DataFrame(hourly)
                
                # Clean time stamps and types
                df['time'] = df['time'].apply(lambda t: f"{int(t)//100:02d}:00")
                df['tempC'] = pd.to_numeric(df['tempC'])
                df['humidity'] = pd.to_numeric(df['humidity'])
                df['condition'] = df['weatherDesc'].apply(lambda d: d[0]['value'] if isinstance(d, list) else d)

                # Visuals
                fig = px.line(
                    df, 
                    x='time', 
                    y='tempC', 
                    title=f"Hourly Temperature Forecast: {city.title()}",
                    labels={'time': 'Time', 'tempC': 'Temperature (°C)'},
                    markers=True
                )
                st.plotly_chart(fig, use_container_width=True)
                
                with st.expander("View Cleaned Dataset"):
                    st.dataframe(df[['time', 'tempC', 'humidity', 'condition']], use_container_width=True)

            else:
                st.error("Failed to retrieve weather data. Please verify the city name.")

        except requests.exceptions.RequestException:
            st.error("Connection timed out. Please check your internet or try again later.")
