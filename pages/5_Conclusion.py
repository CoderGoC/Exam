import streamlit as st

st.set_page_config(
    page_title="Conclusion",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title('Conclusion')

st.markdown("""
### Overview

In this project, we embarked on a comprehensive journey to develop a predictive model for estimating the base MSRP of electric vehicles based on their model year and electric range. Here’s a summary of the key steps and findings:

#### 1. **Data Collection**
We began by collecting a dataset on electric vehicle populations, which included various attributes such as `Make`, `Model Year`, `Electric Range`, and `Base MSRP`. This data served as the foundation for our analysis and modeling.

#### 2. **Data Cleaning**
To ensure the accuracy and reliability of our predictions, we performed several data cleaning tasks:
- **Handling Missing Values**: We replaced zeros in the `Base MSRP` column with the mean of non-zero values. This step was crucial to avoid skewing our analysis with zero values that might not be meaningful.
- **Feature Selection**: We focused on relevant features such as `Model Year` and `Electric Range`, which we hypothesized would have a significant impact on the `Base MSRP`.

#### 3. **Exploratory Data Analysis (EDA)**
EDA was conducted to gain insights into the data and to understand the relationships between different variables:
- **Visualization**: Various visualizations were used to explore the distribution of `Base MSRP` across different `Makes` and `Model Years`, and to analyze the relationship between `Electric Range` and `Base MSRP`.
- **Growth Rate Analysis**: We calculated the recent 5-year growth rate of `Base MSRP` for each make, providing insights into how vehicle pricing trends have evolved.

#### 4. **Prediction Model**
A linear regression model was developed to predict the `Base MSRP` based on `Model Year` and `Electric Range`:
- **Model Training**: We trained the model using historical data, splitting it into training and testing sets to evaluate its performance.
- **Model Evaluation**: The model was evaluated using Mean Squared Error (MSE) and R² Score. The MSE indicated the average squared difference between predicted and actual values, while the R² Score showed the proportion of variance explained by the model.

Despite the challenges faced, including high MSE and low R² Score, these results provided valuable insights into the limitations of the current model. The low R² Score suggests that the model may not fully capture the complexity of the data, indicating potential areas for improvement.

#### **Future Directions**
To enhance the predictive accuracy, further steps could include:
- **Feature Engineering**: Incorporating additional features or refining existing ones could improve model performance.
- **Algorithm Exploration**: Experimenting with different regression algorithms or machine learning techniques might yield better results.
- **Data Enrichment**: Acquiring more comprehensive data or incorporating external sources could provide a richer context for predictions.

Overall, this project highlights the importance of thorough data preparation and analysis in building effective predictive models. While the current model offers a foundational understanding, ongoing refinement and exploration are essential for achieving more accurate and reliable predictions.
""")
