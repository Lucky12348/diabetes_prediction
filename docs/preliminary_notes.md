## **Diabetes Medical Information Summary**

1. Diabetes mellitus, a chronic metabolic disorder, is **characterized by the body's impaired ability to utilize blood sugar (glucose) effectively.** The American Diabetes Association categorizes diabetes into two primary types:

    * ***Type 1 diabetes:***
        * form often manifests in childhood;
        * body's immune system mistakenly attacks and destroys insulin-producing beta cells in the pancreas, **leading to a deficiency in insulin production**.
    
    * ***Type 2 Diabetes:***
        * typically diagnosed in adulthood;
        * arises due to either **insufficient insulin secretion or the development of insulin resistance** within the body's cells;
        * risk factors include: **a positive family history, obesity, and physical inactivity**.

    * **less common forms of diabetes can occur** due to genetic defects, pancreatic dysfunction, or exposure to medications or chemicals.

<br>

2. ***Gestational diabetes mellitus (GDM):***
    * **a temporary type of diabetes that can develop during pregnancy**;
    * typically resolves after childbirth,but **it increases the mother's risk of developing type 2 diabetes** later in life

<br>

4. ***Maternal inheritance of diabetes and its impact on offspring:***
    * GDM is unlikely to directly cause diabetes in the baby;
    * If the mother has pre-existing type 2 diabetes, the child has an **elevated risk of developing type 2 diabetes later in life due to genetic predisposition**;
    * **Mothers with type 1 diabetes have a slightly increased risk of their child having type 1 diabetes at birth**.


## **Dataset Origins**

#### A study [Chou et al., J.Pers.Med. 2023] of 15000 women aged between 20 and 80 selected as the subjects in the Taipei Municipal medical center. These women were patients who had gone to the medical center during 2018–2020 and 2021–2022 with or without the diagnosis of diabetes.


## **Key Dataset Features**

1. **Independent features:**
    * Pregnancies - number of times pregnant;
    * PlasmaGlucose - plasma glucose concentration after 2 hours in an oral glucose tolerance test;
    * DiastolicBloodPressure - diastolic blood pressure (mm Hg);
    * TricepsThickness - triceps skin fold thickness (mm);
    * SerumInsulin - 2-hour serum insulin (mu U/ml);
    * BMI - body mass index (weight in kg/(height in m)^2);
    * DiabetesPedigree - a function that scores the probability of diabetes based on family history;
    * Age - age in years.

<br>

2. **Dependent feature:**
    * Diabetic:
        * 1 = diabetes diagnosed;
        * 0 = no diabetes diagnosed.

## Additional resources:
* [WHO Diabetes webpage](https://www.who.int/news-room/fact-sheets/detail/diabetes)
* [PIMA Indian dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
* Original study for the project dataset: Chou CY, Hsu DY, Chou CH. Predicting the Onset of Diabetes with Machine Learning Methods. J Pers Med. 2023 Feb 24;13(3):406. doi:10.3390/jpm13030406. PMID: 36983587; PMCID: PMC10057336.