import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
import os





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




def replace_zeros_with_mean(df, column_name):
    non_zero_mean = df[df[column_name] != 0][column_name].mean()
    df[column_name] = df[column_name].replace(0, non_zero_mean)
    return df


data = replace_zeros_with_mean(data, 'Electric Range')
data = replace_zeros_with_mean(data, 'Base MSRP')



st.title("Electric Vehicle Population Data Report")
st.write(data.head())



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
st.markdown("---")

st.write("**Summary Statistics of the Data Frame:**")
st.write(data.describe())
st.markdown("---")


st.title("Data Scaling Methods")


st.image(
    "Scaling methods.jpg", 
    caption="Data scaling methods", 
    use_column_width=True
)


st.subheader("Standardization")
st.markdown("---")
st.image(
    "Standardisation.jpg", 
    caption="Standardization Method", 
    use_column_width=True
)

scaler = StandardScaler()
data_standardized = data.copy()
data_standardized[numeric_columns] = scaler.fit_transform(data[numeric_columns])

st.write(data_standardized.describe())
st.markdown("---")

st.title("Effects of Standardization Method on Skewed Data")
st.markdown("---")

def plot_distribution(data, title):
    fig, axes = plt.subplots(1, len(numeric_columns), figsize=(20, 5))
    fig.suptitle(title, fontsize=16)
    for i, column in enumerate(numeric_columns):
        sns.histplot(data[column], kde=True, ax=axes[i])
        axes[i].set_title(column)
    st.pyplot(fig)

st.markdown("---")

plot_distribution(data, "Original Data Distribution")
plot_distribution(data_standardized, "Standardized Data Distribution")

st.markdown("---")
st.image(
    "Standardisation summary.jpg", 
    caption="Standardisation Method summary", 
    use_column_width=True
)




st.subheader("Min-Max Scaling")
st.markdown("---")
st.image(
    "MinMax.jpg", 
    caption="Min-Max Scaling Method", 
    use_column_width=True
)

scaler = MinMaxScaler()
data_minmax = data.copy()
data_minmax[numeric_columns] = scaler.fit_transform(data[numeric_columns])

st.write(data_minmax.describe())
st.markdown("---")

st.title("Effects of Min-Max Scaling Method on Skewed Data")
st.markdown("---")

plot_distribution(data, "Original Data Distribution")
plot_distribution(data_minmax, "Min-Max Scaled Data Distribution")

st.image(
    "MinMax summary.jpg", 
    caption="Min-Max Scaling Method Summary", 
    use_column_width=True
)




st.subheader("Mean Normalization")
st.markdown("---")
st.image(
    "Mean Normal.jpg", 
    caption="Mean Normalization", 
    use_column_width=True
)

data_mean_normalized = data.copy()
for column in numeric_columns:
    data_mean_normalized[column] = (data_mean_normalized[column] - data_mean_normalized[column].mean()) / (data_mean_normalized[column].max() - data_mean_normalized[column].min())

st.write(data_mean_normalized.describe())
st.markdown("---")

st.title("Effects of Mean Normalization Method on Skewed Data")
st.markdown("---")

plot_distribution(data, "Original Data Distribution")
plot_distribution(data_mean_normalized, "Mean Normalized Data Distribution")

st.image(
    "Mean Normal summary.jpg", 
    caption="Mean Normalization Summary", 
    use_column_width=True
)



st.subheader("Robust Scaling")
st.markdown("---")
st.image(
    "Robust.jpg", 
    caption="Robust Scaling", 
    use_column_width=True
)

scaler = RobustScaler()
data_robust = data.copy()
data_robust[numeric_columns] = scaler.fit_transform(data[numeric_columns])

st.write(data_robust.describe())
st.markdown("---")

st.title("Effects of Robust Scaling Method on Skewed Data")
st.markdown("---")

plot_distribution(data, "Original Data Distribution")
plot_distribution(data_robust, "Robust Scaled Data Distribution")

st.image(
    "Robust summary.jpg", 
    caption="Robust Scaling Summary", 
    use_column_width=True
)



st.title("Effects of Scaling on Skewed Data")
st.markdown("---")

plot_distribution(data, "Original Data Distribution")
plot_distribution(data_standardized, "Standardized Data Distribution")
plot_distribution(data_minmax, "Min-Max Scaled Data Distribution")
plot_distribution(data_mean_normalized, "Mean Normalized Data Distribution")
plot_distribution(data_robust, "Robust Scaled Data Distribution")
