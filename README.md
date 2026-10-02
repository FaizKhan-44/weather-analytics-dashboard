# Weather Analytics Dashboard

A live weather dashboard built using Python and Streamlit. It fetches real-time weather metrics using the `wttr.in` REST API, cleans up the JSON payload using Pandas, and plots today's hourly temperature trends using Plotly.

I built this project to expand on my weather API concept and turn raw API data into an interactive visual dashboard.

---

## 🔗 Live App
[Check out the Live App Here](https://faiz-weather-analytics.streamlit.app/)

---

## Features
* **Live Weather Metrics:** Displays current temperature, humidity, wind speed, and general weather conditions.
* **Hourly Trend Visuals:** Plots hourly temperature changes using Plotly charts.
* **Data Processing:** Cleans and formats raw API JSON data into structured Pandas DataFrames.
* **Raw Data View:** Includes an expandable view to inspect raw hourly dataset tables.
---

## Tech Stack
* **Python 3.11+**
* **Streamlit** (Web UI)
* **Requests** (API fetching)
* **Pandas** (Data cleaning & manipulation)
* **Plotly** (Data visualization)

---

## How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/FaizKhan-44/weather-analytics-dashboard.git
cd weather-analytics-dashboard

pip install -r requirements.txt
python -m streamlit run app.py
```
