import streamlit as st
import time
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(
    page_title="EV Base MSRP Prediction Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

data = pd.read_csv("Electric_Vehicle_Population_Data.csv")


st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://i2.wp.com/files.123freevectors.com/wp-content/original/154027-abstract-blue-and-white-background-design.jpg?w=500&q=95");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def replace_zeros_with_mean(df, column_name):
    non_zero_mean = df[df[column_name] != 0][column_name].mean()
    df[column_name] = df[column_name].replace(0, non_zero_mean)
    return df

data = replace_zeros_with_mean(data, 'Base MSRP')

st.title('EV Base MSRP Prediction Dashboard')

my_data = data.copy()
my_data['Base MSRP'] = my_data['Base MSRP'].fillna(0)

make = st.selectbox('Select the Make:', my_data['Make'].unique())
year = st.slider('Select the Year:', min_value=int(my_data['Model Year'].min()), max_value=int(my_data['Model Year'].max()) + 10, value=int(my_data['Model Year'].max()))

features = ['Model Year', 'Electric Range']
X = my_data[features]
y = my_data['Base MSRP']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
st.write(f"Mean Squared Error: {mse:.2f}")
st.write(f"R^2 Score: {r2:.4f}")

def stream_data():
    text = f"Predicting Base MSRP for {make} in the year {year}...\n"
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

    re = my_data[(my_data['Make'] == make) & (my_data['Base MSRP'] != 0)]['Base MSRP']
    if not re.empty:
        re_dat = my_data[my_data['Make'] == make].sort_values(by='Model Year')
        re_dat['Previous Year Value'] = re_dat['Base MSRP'].shift(1)
        re_dat = re_dat.tail(5)

        re_dat['Growth Rate (%)'] = ((re_dat['Base MSRP'] - re_dat['Previous Year Value']) / re_dat['Previous Year Value']) * 100
        re_dat = re_dat.dropna(subset=['Growth Rate (%)'])

        text = '\nRecent 5-Year Growth Rate\n'
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.02)
        st.write(re_dat[['Model Year', 'Base MSRP', 'Growth Rate (%)']])

        if re.count() < 5:
            text = "\nThe information is a bit sparse; this might reduce accuracy!\n"
            for word in text.split(" "):
                yield word + " "
                time.sleep(0.02)

        make_data = my_data[my_data['Make'] == make].iloc[0]
        input_data = {
            'Model Year': year,
            'Electric Range': make_data['Electric Range'],
        }

        input_df = pd.DataFrame([input_data])
        predicted_value = model.predict(input_df[features])[0]

        actual_value = make_data['Base MSRP']
        error_percentage = abs(predicted_value - actual_value) / actual_value

        text = f"\nPredicted Base MSRP for {make} in {year}: ${predicted_value:,.2f}\n"
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.02)
        text = f"\nAccuracy: {100 - error_percentage:.2f}%\n"
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.02)
        text = f"\nActual Base MSRP: ${actual_value:,.2f}\n"
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.02)
    else:
        time.sleep(1)
        text = f'\nSorry, the information about {make} is very limited. Please choose another make!'
        for word in text.split(" "):
            yield word + " "
            time.sleep(0.02)

if st.button("Stream data"):
    st.write_stream(stream_data)

st.subheader("Mean Squared Error (MSE)")
st.markdown("""
    `Mean Squared Error (MSE)` measures the average of the squares of the errors 📖 that is, the average squared difference between the estimated values `(predictions)` and the actual values `(observations)`.
""")

st.subheader("R² Score")
st.markdown("""
    `The R² Score` (or coefficient of determination) represents the proportion of the variance in the dependent variable that is predictable from the independent variables. It is a measure of how well the model explains the variability of the data.
    
    `The R² value` ranges from `0 to 1`, where `1 indicates that the model explains all the variability of the response data around its mean`, and 0 indicates that the model explains none of the variability. The value you provided, `0.0015, is very close to 0, which means the model explains very little of the variability in the target variable (Base MSRP)`. This suggests that the model is not a good fit for the data and may not be providing meaningful predictions.
""")

st.subheader("Summary")
st.markdown("""
    `High MSE` 📖 Indicates large average squared errors, which can be problematic if your model predictions are not close to actual values.
    `Low R² Score` 📖 Indicates that the model is not capturing the underlying patterns in the data and has poor explanatory power.
    
    In practice, `a high MSE and low R²` score usually suggest that the model might `need improvement`, `possibly by including additional features`, trying different `algorithms`, or `transforming the data`.
""")
