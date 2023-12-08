import streamlit as st
import pickle
#dir = path.Path(_file_).abspath()
#sys.append.path(dir.parent.parent)
#path_to_model = './Users/rajusubba/london-bike-shares-main/gb_model.pkl'
model = pickle.load(open('gb_model.pkl', 'rb'))
st.title("Prediction of bike")
st.markdown("Here we are using temperature as the input to predict the day's revenue")
st.subheader("Real Temperature in in C")
t1 = st.number_input('', 0,46)

st.subheader("Feels like Temperature in C")
t2 = st.number_input('', 0,45)

st.subheader("Humidity in Percentage")
hum = st.number_input('', 0,90)

st.subheader("wind speed in Km/h")
wind_speed = st.number_input('', 0,100)

st.subheader("Enter the weather code")
long_string =  """Weather Code and the corresponding number:
    1 = Clear ; mostly clear but have some values with haze/fog/patches of fog/ fog in vicinity
    2 = scattered clouds / few clouds
    3 = Broken clouds
    4 = Cloudy
    7 = Rain/ light Rain shower/ Light rain
    10 = rain with thunderstorm
    26 = snowfall
    94 = Freezing Fog"""
st.subheader(long_string)
weather_code = st.number_input('', 0,94)

st.subheader("Enter the is holiday, 0 for not and 1 for holiday")
is_holiday = st.number_input('', 0,1)

st.subheader("Enter the if it is is weekend, o for not and 1 for weekend")
is_weekend = st.number_input('', 0,2)
season = """Enter the season/category field meteorological seasons:
            0-spring
    1-summer
    2-fall
    3-winter"""
st.subheader(season)
season = st.number_input('', 0,4)

st.subheader("Predicted")
#user_data = {t1,t2,hum,wind_speed, weather_code, is_holiday, is_weekend, season}

#user_data = pd.DataFrame(user_data, index = [0])
#count = model.predict(user_data)

st.code(float(model.predict([[t1,t2,hum,wind_speed, weather_code, is_holiday, is_weekend, season]])))
