import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.set_page_config(
    page_title="Multipage App",
    page_icon="✔️"
)

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


data = pd.read_csv("Electric_Vehicle_Population_Data.csv")


st.title("Electric Vehicle Population Data Report")
st.write(data.head())


st.title("Brief Definitions of Data Frame Columns")
st.write("""
    1. **VIN (1-10)**: The Vehicle Identification Number, truncated.
    2. **County**: The county where the vehicle is registered.
    3. **City**: The city where the vehicle is registered.
    4. **State**: The state where the vehicle is registered.
    5. **Postal Code**: The postal code where the vehicle is registered.
    6. **Model Year**: The year the vehicle model was released.
    7. **Make**: The manufacturer of the vehicle.
    8. **Model**: The specific model of the vehicle.
    9. **Electric Vehicle Type**: Type of electric vehicle (e.g., BEV - Battery Electric Vehicle, PHEV - Plug-in Hybrid Electric Vehicle).
    10. **CAFV Eligibility**: Eligibility for Clean Alternative Fuel Vehicle.
    11. **Electric Range**: The range of the vehicle on electric power alone.
    12. **Base MSRP**: Manufacturer's Suggested Retail Price.
    13. **Legislative District**: The legislative district where the vehicle is registered.
    14. **DOL Vehicle ID**: Department of Licensing vehicle ID.
    15. **Vehicle Location**: The geographic coordinates of the vehicle's registration location.
    16. **Electric Utility**: The utility provider for the vehicle's charging location.
    17. **2020 Census Tract**: Census tract for demographic and geographical data.
""")

st.title("Explore the Data Frame")

st.write("**Data Shape:**", data.shape)

st.write("**Unique Car Makes:**")
st.write(data["Make"].unique())

st.write("**Number of Cities:**", len(data["City"].unique()))
st.write("**Number of Counties:**", len(data["County"].unique()))
st.write("**Total Number of Car Makes:**", len(data["Make"].unique()))
st.write("**Total Number of Car Models:**", len(data["Model"].unique()))

st.write("**Average Model Year by Make:**")
st.write(data.groupby("Make")["Model Year"].mean().astype(int))

st.write("**Additional Descriptive Statistics:**")

numeric_columns = data.select_dtypes(include=[np.number]).columns

stats_df = pd.DataFrame(index=numeric_columns)
stats_df['Mean'] = data[numeric_columns].mean()
stats_df['Median'] = data[numeric_columns].median()
stats_df['Min'] = data[numeric_columns].min()
stats_df['Max'] = data[numeric_columns].max()
stats_df['Q1'] = data[numeric_columns].quantile(0.25)
stats_df['Q3'] = data[numeric_columns].quantile(0.75)
stats_df['IQR'] = stats_df['Q3'] - stats_df['Q1']

st.write(stats_df)


st.write("**Summary Statistics of the Data Frame:**")
st.write(data.describe())

st.title("Data Visualization")

st.sidebar.title("Filter Options")
selected_make = st.sidebar.multiselect("Select Car Makes", options=data["Make"].unique(), default=data["Make"].unique())
selected_type = st.sidebar.multiselect("Select Electric Vehicle Types", options=data["Electric Vehicle Type"].unique(), default=data["Electric Vehicle Type"].unique())

filtered_data = data[(data["Make"].isin(selected_make)) & (data["Electric Vehicle Type"].isin(selected_type))]

st.subheader("Distribution of Electric Vehicle Types")
fig, ax = plt.subplots()
sns.countplot(data=filtered_data, x='Electric Vehicle Type', palette='viridis', ax=ax)
ax.set_title('Distribution of Electric Vehicle Types')
ax.set_xlabel('Electric Vehicle Type')
ax.set_ylabel('Count')
st.pyplot(fig)

st.subheader("Electric Range vs Make")
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(data=filtered_data, x='Make', y='Electric Range', palette='viridis', ax=ax)
ax.set_title('Electric Range by Make')
ax.set_xlabel('Make')
ax.set_ylabel('Electric Range')
ax.tick_params(axis='x', rotation=90)
st.pyplot(fig)

# st.subheader("Model vs Electric Range")
# fig, ax = plt.subplots(figsize=(12, 6))
# sns.boxplot(data=filtered_data, x='Model', y='Electric Range', palette='viridis', ax=ax)
# ax.set_title('Electric Range by Model')
# ax.set_xlabel('Model')
# ax.set_ylabel('Electric Range')
# ax.tick_params(axis='x', rotation=90)
# st.pyplot(fig)



st.subheader("Model Year vs. Base MSRP")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x='Model Year', y='Base MSRP', hue='Electric Vehicle Type', palette='viridis', ax=ax)
ax.set_title('Model Year vs. Base MSRP')
ax.set_xlabel('Model Year')
ax.set_ylabel('Base MSRP')
st.pyplot(fig)






