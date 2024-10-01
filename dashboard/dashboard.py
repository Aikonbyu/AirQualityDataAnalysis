import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_df = pd.read_csv("./dashboard/cleaned_data.csv")
air_quality_year = data_df.groupby("year").agg({"PM2.5": "mean", "PM10": "mean", "SO2": "mean", "NO2": "mean", "CO": "mean", "O3": "mean"})

air_quality_month = data_df.groupby("month").agg({"PM2.5": "mean", "PM10": "mean", "SO2": "mean", "NO2": "mean", "CO": "mean", "O3": "mean"})
air_quality_month.index = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

air_quality_station = data_df.groupby("station").agg({"PM2.5": "mean", "PM10": "mean", "SO2": "mean", "NO2": "mean", "CO": "mean", "O3": "mean"})
air_quality_station_mean = air_quality_station.drop(columns=["O3"]).mean(axis=1)
air_quality_station_mean_df = air_quality_station_mean.to_frame(name="Mean Concentration")



st.title('Air Quality Data Visualization')
st.subheader("Worse Air Quality by Time and Polutant")
col1, col2 = st.columns(2)

time_coices = 'Year'
polutant_choices = 'All'

with col1:
    time_coices = st.selectbox('Select by time', ['Year', 'Month'])

with col2:
    polutant_choices = st.selectbox('Select by polutant', ['All', 'PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3'])

if time_coices == 'Year':
    if polutant_choices == 'All':
        all_air_quality_year = air_quality_year.drop(columns=["O3"])
        all_air_quality_year.index = all_air_quality_year.index.astype(str)
        all_air_quality_year_mean = all_air_quality_year.mean(axis=1).sort_values(ascending=False)
        all_air_quality_year_mean_df = all_air_quality_year_mean.to_frame(name="Mean Concentration")
        plt.figure(figsize=(10, 6))
        sns.barplot(x="Mean Concentration", y=all_air_quality_year_mean_df.index, data=all_air_quality_year_mean_df, color="skyblue")
        plt.title("Worse Air Quality by Year (Polutant Mean Concentration)")
        plt.xlabel("Polutant Concentration (µg/m³)")
        plt.ylabel("Year")
        st.pyplot(plt)

    elif polutant_choices == 'PM2.5':
        PM25_year = air_quality_year.drop(columns=["PM10", "SO2", "NO2", "CO", "O3"]).reset_index()
        PM25_year.sort_values(by="PM2.5", ascending=False, inplace=True)
        PM25_year.reset_index(drop=True, inplace=True)
        PM25_year["year"] = PM25_year["year"].astype(str)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="PM2.5", y="year", data=PM25_year, color="skyblue")
        plt.title("Worse Air Quality by Year (PM2.5)")
        plt.xlabel("PM2.5 Concentration (µg/m³)")
        plt.ylabel("Year")
        st.pyplot(plt)

    elif polutant_choices == 'PM10':
        PM10_year = air_quality_year.drop(columns=["PM2.5", "SO2", "NO2", "CO", "O3"]).reset_index()
        PM10_year.sort_values(by="PM10", ascending=False, inplace=True)
        PM10_year.reset_index(drop=True, inplace=True)
        PM10_year["year"] = PM10_year["year"].astype(str)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="PM10", y="year", data=PM10_year, color="skyblue")
        plt.title("Worse Air Quality by Year (PM10)")
        plt.xlabel("PM10 Concentration (µg/m³)")
        plt.ylabel("Year")
        st.pyplot(plt)

    elif polutant_choices == 'SO2':
        SO2_year = air_quality_year.drop(columns=["PM2.5", "PM10", "NO2", "CO", "O3"]).reset_index()
        SO2_year.sort_values(by="SO2", ascending=False, inplace=True)
        SO2_year.reset_index(drop=True, inplace=True)
        SO2_year["year"] = SO2_year["year"].astype(str)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="SO2", y="year", data=SO2_year, color="skyblue")
        plt.title("Worse Air Quality by Year (SO2)")
        plt.xlabel("SO2 Concentration (µg/m³)")
        plt.ylabel("Year")
        st.pyplot(plt)

    elif polutant_choices == 'NO2':
        NO2_year = air_quality_year.drop(columns=["PM2.5", "PM10", "SO2", "CO", "O3"]).reset_index()
        NO2_year.sort_values(by="NO2", ascending=False, inplace=True)
        NO2_year.reset_index(drop=True, inplace=True)
        NO2_year["year"] = NO2_year["year"].astype(str)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="NO2", y="year", data=NO2_year, color="skyblue")
        plt.title("Worse Air Quality by Year (NO2)")
        plt.xlabel("NO2 Concentration (µg/m³)")
        plt.ylabel("Year")
        st.pyplot(plt)

    elif polutant_choices == 'CO':
        CO_year = air_quality_year.drop(columns=["PM2.5", "PM10", "SO2", "NO2", "O3"]).reset_index()
        CO_year.sort_values(by="CO", ascending=False, inplace=True)
        CO_year.reset_index(drop=True, inplace=True)
        CO_year["year"] = CO_year["year"].astype(str)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="CO", y="year", data=CO_year, color="skyblue")
        plt.title("Worse Air Quality by Year (CO)")
        plt.xlabel("CO Concentration (µg/m³)")
        plt.ylabel("Year")
        st.pyplot(plt)

    elif polutant_choices == 'O3':
        O3_year = air_quality_year.drop(columns=["PM2.5", "PM10", "SO2", "NO2", "CO"]).reset_index()
        O3_year.sort_values(by="O3", ascending=True, inplace=True)
        O3_year.reset_index(drop=True, inplace=True)
        O3_year["year"] = O3_year["year"].astype(str)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="O3", y="year", data=O3_year, color="skyblue")
        plt.title("Worse Air Quality by Year (O3)")
        plt.xlabel("O3 Concentration (µg/m³)")
        plt.ylabel("Year")
        st.pyplot(plt)

elif time_coices == 'Month':
    if polutant_choices == "All":
        all_air_quality_month = air_quality_month.drop(columns=["O3"])
        all_air_quality_month.index = all_air_quality_month.index.astype(str)
        all_air_quality_month_mean = all_air_quality_month.mean(axis=1).sort_values(ascending=False)
        all_air_quality_month_mean_df = all_air_quality_month_mean.to_frame(name="Mean Concentration")
        plt.figure(figsize=(10, 6))
        sns.barplot(x="Mean Concentration", y=all_air_quality_month_mean_df.index, data=all_air_quality_month_mean_df, color="skyblue")
        plt.title("Worse Air Quality by Month (Polutant Mean Concentration)")
        plt.xlabel("Polutant Concentration (µg/m³)")
        plt.ylabel("Month")
        st.pyplot(plt)
    elif polutant_choices == 'PM2.5':
        PM25_month = air_quality_month.drop(columns=["PM10", "SO2", "NO2", "CO", "O3"])
        PM25_month.sort_values(by="PM2.5", ascending=False, inplace=True)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="PM2.5", y=PM25_month.index, data=PM25_month, color="skyblue")
        plt.title("Worse Air Quality by Month (PM2.5)")
        plt.xlabel("PM2.5 Concentration (µg/m³)")
        plt.ylabel("Month")
        st.pyplot(plt)
    elif polutant_choices == "PM10":
        PM10_month = air_quality_month.drop(columns=["PM2.5", "SO2", "NO2", "CO", "O3"])
        PM10_month.sort_values(by="PM10", ascending=False, inplace=True)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="PM10", y=PM10_month.index, data=PM10_month, color="skyblue")
        plt.title("Worse Air Quality by Month (PM10)")
        plt.xlabel("PM10 Concentration (µg/m³)")
        plt.ylabel("Month")
        st.pyplot(plt)
    elif polutant_choices == "SO2":
        SO2_month = air_quality_month.drop(columns=["PM2.5", "PM10", "NO2", "CO", "O3"])
        SO2_month.sort_values(by="SO2", ascending=False, inplace=True)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="SO2", y=SO2_month.index, data=SO2_month, color="skyblue")
        plt.title("Worse Air Quality by Month (SO2)")
        plt.xlabel("SO2 Concentration (µg/m³)")
        plt.ylabel("Month")
        st.pyplot(plt)
    elif polutant_choices == "NO2":
        NO2_month = air_quality_month.drop(columns=["PM2.5", "PM10", "SO2", "CO", "O3"])
        NO2_month.sort_values(by="NO2", ascending=False, inplace=True)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="NO2", y=NO2_month.index, data=NO2_month, color="skyblue")
        plt.title("Worse Air Quality by Month (NO2)")
        plt.xlabel("NO2 Concentration (µg/m³)")
        plt.ylabel("Month")
        st.pyplot(plt)
    elif polutant_choices == "CO":
        CO_month = air_quality_month.drop(columns=["PM2.5", "PM10", "SO2", "NO2", "O3"])
        CO_month.sort_values(by="CO", ascending=False, inplace=True)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="CO", y=CO_month.index, data=CO_month, color="skyblue")
        plt.title("Worse Air Quality by Month (CO)")
        plt.xlabel("CO Concentration (µg/m³)")
        plt.ylabel("Month")
        st.pyplot(plt)
    elif polutant_choices == "O3":
        O3_month = air_quality_month.drop(columns=["PM2.5", "PM10", "SO2", "NO2", "CO"])
        O3_month.sort_values(by="O3", ascending=True, inplace=True)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="O3", y=O3_month.index, data=O3_month, color="skyblue")
        plt.title("Worse Air Quality by Month (O3)")
        plt.xlabel("O3 Concentration (µg/m³)")
        plt.ylabel("Month")
        st.pyplot(plt)

st.subheader("Air Quality by Station")
choice = st.radio("Best/Worse Air Quality", ("Best", "Worse"))

if choice == "Best":
    best_air_quality_station = air_quality_station_mean_df.sort_values(by="Mean Concentration", ascending=True)
    best_air_quality_station.reset_index(inplace=True)
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Mean Concentration", y="station", data=best_air_quality_station, color="skyblue")
    plt.title("Best Air Quality by Station")
    plt.xlabel("Mean Concentration")
    plt.ylabel("Station")
    st.pyplot(plt)
elif choice == "Worse":
    worst_air_quality_station = air_quality_station_mean_df.sort_values(by="Mean Concentration", ascending=False)
    worst_air_quality_station.reset_index(inplace=True)
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Mean Concentration", y="station", data=worst_air_quality_station, color="skyblue")
    plt.title("Worst Air Quality by Station")
    plt.xlabel("Mean Concentration")
    plt.ylabel("Station")
    st.pyplot(plt)