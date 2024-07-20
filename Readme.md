# Data Science Project

This repository contains the data science Exam project created by CoderGoC. Here are exercises, codes and results for solving various data science problems.

In this project, we embarked on a comprehensive journey to develop a predictive model for estimating the base MSRP of electric vehicles based on their model year and electric range. Here’s a summary of the key steps and findings:

# 1. **Data Collection**
We began by collecting a dataset on electric vehicle populations, which included various attributes such as `Make`, `Model Year`, `Electric Range`, and `Base MSRP`. This data served as the foundation for our analysis and modeling.

# 2. **Data Cleaning**
To ensure the accuracy and reliability of our predictions, we performed several data cleaning tasks:
- **Handling Missing Values**: We replaced zeros in the `Base MSRP` column with the mean of non-zero values. This step was crucial to avoid skewing our analysis with zero values that might not be meaningful.
- **Feature Selection**: We focused on relevant features such as `Model Year` and `Electric Range`, which we hypothesized would have a significant impact on the `Base MSRP`.

# 3. **Exploratory Data Analysis (EDA)**
EDA was conducted to gain insights into the data and to understand the relationships between different variables:
- **Visualization**: Various visualizations were used to explore the distribution of `Base MSRP` across different `Makes` and `Model Years`, and to analyze the relationship between `Electric Range` and `Base MSRP`.
- **Growth Rate Analysis**: We calculated the recent 5-year growth rate of `Base MSRP` for each make, providing insights into how vehicle pricing trends have evolved.

# 4. **Prediction Model**
A linear regression model was developed to predict the `Base MSRP` based on `Model Year` and `Electric Range`:
- **Model Training**: We trained the model using historical data, splitting it into training and testing sets to evaluate its performance.
- **Model Evaluation**: The model was evaluated using Mean Squared Error (MSE) and R² Score. The MSE indicated the average squared difference between predicted and actual values, while the R² Score showed the proportion of variance explained by the model.

Despite the challenges faced, including high MSE and low R² Score, these results provided valuable insights into the limitations of the current model. The low R² Score suggests that the model may not fully capture the complexity of the data, indicating potential areas for improvement.



## Project aim

- The aim of this project is to analyze a document that provides detailed information and statistics about the number and distribution of electric vehicles (EVs) within Washington, D.C.
This repository has the following goals:
- Learning and strengthening the basics of data science
- Learning to use various data science tools and libraries
- Gain practical experience in statistical analysis and data visualization
- Development of skills in data processing and modeling


## Used technologies

The following technologies and libraries were used in this project:
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Python py file
- os


## How to use

1. Clone the repository:
   ```bash
   git clone https://github.com/CoderGoC/Exam.git
   ```
2. Create a virtual environment and install the required libraries:
   ```bash
   cd Data-science-home-work
   python -m venv venv
   ```
   ```bash
   source venv/bin/activate  # Linux/Mac
   ```
   ```bash
   .\venv\Scripts\activate  # Windows
   ```
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Python py file:
   ```bash
   Streamlit run Home.py
   ```

## Contribute

If you would like to contribute to the project, please follow these steps:
1. Fork the repository
2. Open a new branch (`git checkout -b feature/YourFeature`)
3. Commit the changes (`git commit -m 'Add some feature'')
4. Push the branch (`git push origin feature/YourFeature`)
5. Create a pull request

## Litsenziya

This project is distributed under the MIT license. See the [LICENSE](LICENSE) file for details.



Thank you for your interest in the project!
