import streamlit as st
import pandas as pd
import requests


st.set_page_config(
    page_title="Average Weather 2025",
    layout="wide"
)

st.title(" Average Weather - 2025")
st.write("Temperatura mesatare mujore bazuar në të dhënat nga Weather API.")


latitude = 42.66
longitude = 21.16

city = "Prishtinë"


url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "start_date": "2025-01-01",
    "end_date": "2025-12-31",
    "daily": "temperature_2m_mean",
    "timezone": "auto"
}


@st.cache_data
def get_weather_data():

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    dates = data["daily"]["time"]
    temperatures = data["daily"]["temperature_2m_mean"]

    df = pd.DataFrame({
        "Date": dates,
        "Temperature": temperatures
    })

    df["Date"] = pd.to_datetime(df["Date"])

    return df



try:

    df = get_weather_data()

except Exception as error:

    st.error("Nuk u arritën të merren të dhënat nga API.")
    st.error(error)
    st.stop()




df = df.dropna(subset=["Temperature"])


df["Month"] = df["Date"].dt.month

monthly_average = (
    df.groupby("Month")["Temperature"]
    .mean()
    .reset_index()
)

month_names = {
    1: "Janar",
    2: "Shkurt",
    3: "Mars",
    4: "Prill",
    5: "Maj",
    6: "Qershor",
    7: "Korrik",
    8: "Gusht",
    9: "Shtator",
    10: "Tetor",
    11: "Nëntor",
    12: "Dhjetor"
}

monthly_average["Muaji"] = monthly_average["Month"].map(
    month_names
)

monthly_average["Average Temperature"] = (
    monthly_average["Temperature"]
    .round(2)
)



yearly_average = round(
    df["Temperature"].mean(),
    2
)




col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Lokacioni",
        city
    )

with col2:
    st.metric(
        "Viti",
        "2025"
    )

with col3:
    st.metric(
        "Average i vitit",
        f"{yearly_average} °C"
    )


st.subheader(" Average Temperature për çdo muaj")

result = monthly_average[
    ["Muaji", "Average Temperature"]
]

result = result.rename(
    columns={
        "Average Temperature": "Temperatura (°C)"
    }
)

st.dataframe(
    result,
    use_container_width=True,
    hide_index=True
)



st.subheader(" Temperatura mesatare mujore")

chart_data = monthly_average.set_index("Muaji")

st.line_chart(
    chart_data["Average Temperature"]
)


st.subheader(" Informacion")

st.write(
    f"""
    Projekti analizon temperaturat ditore gjatë vitit 2025
    për lokacionin {city}.

    Të dhënat merren automatikisht nga Weather API dhe
    pastaj Python dhe Pandas i grupojnë sipas muajve.

    Temperatura mesatare e vitit 2025 është:
    **{yearly_average} °C**
    """
)


with st.expander("Shiko të dhënat ditore"):

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
