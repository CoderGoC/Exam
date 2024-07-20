import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import streamlit as st


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


st.write("**Summary Statistics of the Data Frame:**")
st.write(data.describe())
st.markdown("---")


fig, ax = plt.subplots()
sns.histplot(data['Electric Range'], bins=30, kde=True, ax=ax)
ax.set_title('Electric Range Distribution', fontsize=16)
ax.set_xlabel('Electric Range', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)
st.pyplot(fig)


range_trend = data.groupby('Model Year')['Electric Range'].mean().reset_index()
fig, ax = plt.subplots()
ax.plot(range_trend['Model Year'], range_trend['Electric Range'], marker='o')
ax.set_title('Electric Range Trend Over Years', fontsize=16)
ax.set_xlabel('Model Year', fontsize=14)
ax.set_ylabel('Average Electric Range', fontsize=14)
ax.grid(True)
st.pyplot(fig)


fig, ax = plt.subplots()
sns.boxplot(x='Make', y='Electric Range', data=data, ax=ax)
ax.set_title('Electric Ranges by Vehicle Make', fontsize=16)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=12)
ax.set_xlabel('Make', fontsize=14)
ax.set_ylabel('Electric Range', fontsize=14)
ax.tick_params(labelsize=7)
st.pyplot(fig)


fig = px.scatter(data, x='Model Year', y='Electric Range', color='Make', title='Electric Range vs. Model Year')
st.plotly_chart(fig)



make_avg_range = data.groupby('Make')['Electric Range'].mean().reset_index()
fig, ax = plt.subplots()
sns.barplot(x='Make', y='Electric Range', data=make_avg_range, ax=ax)
ax.set_title('Average Electric Range by Vehicle Make', fontsize=16)
ax.set_xlabel('Make', fontsize=14)
ax.set_ylabel('Average Electric Range', fontsize=14)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=12)
ax.tick_params(labelsize=7)
st.pyplot(fig)



make_counts = data['Make'].value_counts().reset_index()
make_counts.columns = ['Make', 'Count']
fig = px.bar(make_counts, x='Make', y='Count', title='Total Number of Vehicles by Make', 
             labels={'Make': 'Make', 'Count': 'Total Count'})
fig.update_layout(xaxis={'categoryorder': 'total descending'}, xaxis_tickfont_size=12)
fig.update_xaxes(title_font=dict(size=16))
fig.update_yaxes(title_font=dict(size=16))
st.plotly_chart(fig)


st.subheader("Correlation Heatmap")
numeric_data = data.select_dtypes(include=[np.number])
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', ax=ax)
ax.set_title('Correlation Heatmap', fontsize=16)
st.pyplot(fig)


# st.subheader("FacetGrid Plots with Regression")


# g = sns.FacetGrid(data, col="Make", col_wrap=4, height=3.5)
# g.map(sns.regplot, "Base MSRP", "Electric Range", scatter_kws={"s": 10}, line_kws={"color": "r"})
# st.pyplot(g)



# g = sns.FacetGrid(data, col="Make", col_wrap=4, height=3.5)
# g.map(sns.regplot, "Model Year", "Base MSRP", scatter_kws={"s": 10}, line_kws={"color": "r"})
# st.pyplot(g)


# st.subheader("FacetGrid: Base MSRP by Vehicle Electric Range")
# g = sns.FacetGrid(data, col='Electric Range', col_wrap=4, height=3.5)
# g.map(sns.boxplot, 'Base MSRP')
# for ax in g.axes.flat:
#     for label in ax.get_xticklabels():
#         label.set_rotation(45)
# st.pyplot(g)


st.subheader("Advanced JointGrid: Model Year vs. Electric Range")
g = sns.JointGrid(data=data, x='Model Year', y='Electric Range', height=8)
g.plot(sns.regplot, sns.histplot)
st.pyplot(g)


st.subheader("Customized Jointplot: Model Year vs. Electric Range")
jp = sns.jointplot(data=data, x='Model Year', y='Electric Range', kind="reg", height=8, marginal_kws=dict(bins=30, fill=True))
jp.figure.suptitle('Model Year vs. Electric Range', fontsize=16)
jp.set_axis_labels('Model Year', 'Electric Range', fontsize=14)
st.pyplot(jp)



st.write("### Insights and Recommendations")
st.write("1. Most electric vehicles have a range between 20 and 300 miles.")
st.write("2. Tesla vehicles tend to have higher electric ranges compared to other makes.")