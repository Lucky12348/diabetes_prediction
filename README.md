# **Women Diabetes Outcome Prediction Machine Learning Project**

**This project aims to build a machine learning model to predict the diabetic outcome for women based on a dataset of 15,000 women aged between 21 and 77. The goal is to develop machine learning, from exploratory data analysis to model deployment, and create a web application that can predict whether a woman is likely to have diabetes based on input features.**


## **About the dataset**
The dataset used in this project is derived from a study conducted at the Taipei Municipal Medical Center. It contains 8 features for each of the 15,000 women, including:

* **Pregnancies**: number of times pregnant;
* **PlasmaGlucose**: plasma glucose concentration after 2 hours in an oral glucose tolerance test;
* **DiastolicBloodPressure**: diastolic blood pressure (mm Hg);
* **TricepsThickness**: triceps skin fold thickness (mm);
* **SerumInsulin**: 2-hour serum insulin (mu U/ml);
* **BMI**: body mass index (weight in kg/(height in m)^2);
* **DiabetesPedigree**: a function that scores the probability of diabetes based on family history;
* **Age**: age in years.

The target variable is **Diabetic**, which indicates whether diabetes was diagnosed (1) or not (0).

## **How It Works**

1. The user inserts medical record data.
2. A Logistic Regression model, trained on the above-mentionned dataset assesses the risk of the user of being in the diabetic or non-diabetic risk group.

## **GIF demonstration**

![](https://i.postimg.cc/0yNS8SKT/diabetic.gif)   ![](https://i.postimg.cc/wTgfQwnD/non-diabetic.gif)


## Project Structure

```bash
diabetes_prediction
├── Data/
│   └── TAIPEI_diabetes.csv
│   └── pima_indian_dataset.csv
│
├── Notebooks/
│   └── data_analysis.ipynb
│
├── Reports/
│   └── women_diabetes_prediction_report.pdf
│
├── WebApp/
│   ├── app/
│   │   ├── api.py
│   │   ├── model_loader.py
│   │   ├── predictor.py
│   │   └── ui.py
│   └── main.py
│
├── README.md
└── requirements.txt
└── conda-requirements.txt

```
* **Data/**: contains the dataset used in the project.
* **Notebooks/**: contains a Jupyter notebook for exploratory data analysis, feature engineering, model training, and evaluation.
* **Reports/**: contains the final project report in PDF format.
* **WebApp/**: contains the code for the web application built using FastAPI and Streamlit.
* **README.md**: provides an overview of the project.
* **requirements.txt**: lists all the dependencies required to run the project.
* **conda-requirements.txt**: lists all the dependencies required to run the project using Conda distribution.


## Installation

To set up the project locally, you can choose between using **Conda** or a **virtual environment with pip**.

**Clone the repository**:
   ```bash
   git clone https://github.com/Lucky12348/diabetes_prediction.git
   cd diabetes_prediction
   ```
### Option 1: Using Conda


-  **Create and activate the environment**:
   ```bash
   conda create --name diabetes_env --file conda-requirements.txt
   conda activate diabetes_env
   ```

### Option 2: Using pip and virtualenv

1. **Create and activate a virtual environment**:

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

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Start the web project
```bash
cd WebApp
streamlit run main.py
```

## ⚠️ **Disclaimer**

**This application is developed as part of an academic machine learning project, aimed at showcasing proficiency in machine learning techniques. It is not intended to offer medical advice and should not be used as a basis for any medical decision-making.**
