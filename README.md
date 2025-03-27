# Predicting Diabetes Outcome for Women
> **Disclaimer**: This is a student project and is intended for educational purposes only. It should not be used for actual medical diagnosis or to predict diabetes outcomes in real-world scenarios.
## Project Overview

This project aims to build a machine learning model to predict the diabetic outcome for women based on a dataset of 15,000 women aged between 20 and 80. The goal is to develop machine learning, from exploratory data analysis to model deployment, and create a web application that can predict whether a woman is likely to have diabetes based on input features.

## Dataset

The [dataset]() used in this project is derived from a study conducted at the Taipei Municipal Medical Center. It contains 8 features for each of the 15,000 women, including:

- **Pregnancies**: Number of times pregnant
- **PlasmaGlucose**: Plasma glucose concentration after 2 hours in an oral glucose tolerance test
- **DiastolicBloodPressure**: Diastolic blood pressure (mm Hg)
- **TricepsThickness**: Triceps skin fold thickness (mm)
- **SerumInsulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **DiabetesPedigree**: A function that scores the probability of diabetes based on family history
- **Age**: Age in years

The target variable is **Diabetic**, which indicates whether diabetes was diagnosed (1) or not (0).

## Project Structure

The project is structured as follows:

- **Notebooks/**: Contains Jupyter notebooks for exploratory data analysis, feature engineering, model training, and evaluation.
- **WebApp/**: Contains the code for the web application built using FastAPI and Streamlit.
- **Reports/**: Contains the final project report in PDF format.
- **Data/**: Contains the dataset used in the project.
- **README.md**: This file, providing an overview of the project.
- **requirements.txt**: Lists all the Python dependencies required to run the project.

## Web application short demo video

![](https://media.tenor.com/ZPHHiCRxrlsAAAAj/happy-happy-happy-cat.gif)


## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Lucky12348/diabetes_prediction.git
   ```
2. **Create and activate a virtual environment**:

   **Linux**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

   **Windows**:
   ```bash
   python -m venv env
   .\env\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Start the web project
```bash
cd WebApp
streamlit run main.py
```