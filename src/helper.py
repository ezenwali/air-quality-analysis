import pandas as pd

NO2_rate_cement = 1117  # tons/year
pm25_rate_cement = 10.46  # tons/year

pm25_rate_plywood = 23.47  # tons/year
NO2_rate_plywood = 71.91  # tons/year


def convert_to_24_hour(time_str):
    """_summary_
    Converts a time string to a 24 hour format
    """
    try:
        # Try converting the time as a 12-hour format
        return pd.to_datetime(time_str, format="%I:%M %p").strftime("%H:%M")
    except:
        # If it fails, try converting the time as a 24-hour format
        return pd.to_datetime(time_str, format="%H:%M").strftime("%H:%M")


def convert_percent_to_weight(total_weight, per):

    return per / 100 * total_weight


def get_emission_rate():

    Facility = ["Richmond Plywood Factory", "Richmond Cement Plant"]
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    pm25_percent_yearly_plywood = [
        8.90,
        8.30,
        8.30,
        8.40,
        8.10,
        8.80,
        7.00,
        9.50,
        7.60,
        7.60,
        9.50,
        8.00,
    ]
    # monthly percentage

    pm25_percent_yearly_cement = [
        8.33,
        8.33,
        8.34,
        8.33,
        8.33,
        8.34,
        8.33,
        8.33,
        8.34,
        8.33,
        8.33,
        8.34,
    ]  # monthly percentage

    NO2_percent_year_plywood = [
        8.90,
        8.30,
        8.30,
        8.40,
        8.10,
        8.80,
        7.00,
        9.50,
        7.60,
        7.60,
        9.50,
        8.00,
    ]  # monthly percentage

    NO2_percent_yearly_cement = [
        8.33,
        8.33,
        8.34,
        8.33,
        8.33,
        8.34,
        8.33,
        8.33,
        8.34,
        8.33,
        8.33,
        8.34,
    ]  # monthly percentage

    # Calculate PM2.5 and NO2 emissions for each month
    pm25_tons_per_year_plywood = [
        convert_percent_to_weight(pm25_rate_plywood, per)
        for per in pm25_percent_yearly_plywood
    ]
    pm25_tons_per_year_cement = [
        convert_percent_to_weight(pm25_rate_cement, per)
        for per in pm25_percent_yearly_cement
    ]

    NO2_tons_per_year_plywood = [
        convert_percent_to_weight(NO2_rate_plywood, per)
        for per in NO2_percent_year_plywood
    ]
    NO2_tons_per_year_cement = [
        convert_percent_to_weight(NO2_rate_cement, per)
        for per in NO2_percent_yearly_cement
    ]

    # Create Data
    return {
        "facility": [fac for fac in Facility for _ in months],
        "month": months * len(Facility),
        "pm2.5_ton_per_month": pm25_tons_per_year_plywood + pm25_tons_per_year_cement,
        "NO2_ton_per_month": NO2_tons_per_year_plywood + NO2_tons_per_year_cement,
    }
