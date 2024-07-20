import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="✔️"
)

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://akm-img-a-in.tosshub.com/indiatoday/images/story/201612/washh-647_121216093026.jpg?VersionId=DrAnBYDn44UyETgrQV.2K9W9kzVt2Wr6&size=690:388");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Let's get started with the agenda for the project")

st.markdown("---")
st.markdown("---")

st.sidebar.success("Select a page above")

st.title("Electric Vehicles Analysis in Washington, D.C.")

st.markdown(
    """
    <h2 style='color: #FFFF00;'>📥 Data Collection</h2>
    Detailed information on the sources and methods used to collect the data.</p>

    <h2 style='color: #FFFF00;'>🧹 Data Cleaning</h2>
    Steps taken to clean and preprocess the data for analysis.</p>

    <h2 style='color: #FFFF00;'>🔍 Exploratory Data Analysis (EDA)</h2>
    Visual and statistical analysis to uncover insights and trends.</p>

    <h2 style='color: #FFFF00;'>📈 Prediction</h2>
    Modeling techniques used to predict future trends in electric vehicle distribution.</p>

    <h2 style='color: #FFFF00;'>📋 Conclusion</h2>
    Summarizing key findings and potential implications.</p>

    <h2 style='color: #FFFF00;'>🎯 Project Aim</h2>
    <p style='color: #FFFF00;'>The aim of this project is to analyze a document that provides detailed information and statistics about the number and distribution of electric vehicles (EVs) within Washington, D.C.</p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown("---")

st.image(
    "https://images.news18.com/ibnlive/uploads/2022/09/ev-cars-16626568834x3.jpg?impolicy=website&width=640&height=480", 
    caption="Electric Vehicles in Washington, D.C.", 
    use_column_width=True
)

if st.button('Learn More'):
    st.write("Navigate to the detailed analysis section.")
