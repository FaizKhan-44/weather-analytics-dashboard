# 🌤️ Weather Analytics Dashboard

A live weather dashboard built using Python and Streamlit. It fetches real-time weather metrics using the `wttr.in` REST API, cleans up the JSON payload using Pandas, and plots today's hourly temperature trends using Plotly.

I built this project to expand on my weather API concept and turn raw API data into an interactive visual dashboard.

---

## 🔗 Live App
[Check out the Live App Here](https://your-app-name.streamlit.app)

---

## 🚀 Features
* **Live Weather Metrics:** Displays current temperature, humidity, wind speed, and general weather conditions[cite: 1].
* **Hourly Trend Visuals:** Plots hourly temperature changes using Plotly charts.
* **Data Processing:** Cleans and formats raw API JSON data into structured Pandas DataFrames[cite: 1].
* **Raw Data View:** Includes an expandable view to inspect raw hourly dataset tables.

---

## 🛠️ Tech Stack
* **Python 3.11+**[cite: 1]
* **Streamlit** (Web UI)
* **Requests** (API fetching)[cite: 1]
* **Pandas** (Data cleaning & manipulation)[cite: 1]
* **Plotly** (Data visualization)

---

## 💻 How to Run Locally

1. Clone the repo:
```bash
git clone [https://github.com/FaizKhan-44/weather-analytics-dashboard.git](https://github.com/FaizKhan-44/weather-analytics-dashboard.git)
cd weather-analytics-dashboard

libraries required :
  pip install -r requirements.txt
command to run :
python -m streamlit run app.py