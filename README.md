

🚢 Titanic Survival Analysis: Exploratory Data Analysis (EDA)
Project Overview
This project focuses on conducting Exploratory Data Analysis (EDA) on the historical Titanic dataset. The goal is to identify and visualize key statistical relationships and patterns that determined a passenger's chance of survival. This deep dive into the data is a crucial prerequisite for building an accurate machine learning prediction model.

⚙️ Data Preparation and Cleaning
The raw data was processed to handle missing values and convert categorical features into a numerical format suitable for analysis and modeling.

1. Feature Removal
The following columns were dropped as they were deemed non-predictive or redundant:

Cabin: Removed due to excessive missing data.

PassengerId, Name, Ticket: Removed as they are unique identifiers that provide no predictive value for survival.

2. Missing Value Imputation
Age: Missing values were filled using the median of the column to maintain the shape of the age distribution.

Embarked: Missing values were filled using the mode (most frequent value) as it is a categorical/text column.

3. Feature Engineering
Sex: Converted to a numerical binary format (male: 0, female: 1).

Embarked: Converted into separate binary (dummy) columns using One-Hot Encoding.

📊 Key Insights from Visualization
The analysis revealed strong, multi-faceted relationships between survival and social factors, confirming the "Women and Children First" ethos.

1. Gender (Sex) & Class (Pclass) Were Dominant Factors
Gender Bias: More women survived than men, showing that gender played the single most important role in survival.

Socio-Economic Status: 1st class passengers had the highest chance of survival, followed by 2nd, with 3rd class having the lowest.

Combined Effect: The most profound finding is that women in 1st and 2nd class survived the most, while men in 3rd class survived the least. This highlights the interaction between social class and gender.

2. Wealth & Age Correlations
Fare/Wealth: Survivors generally paid higher fares, indicating that wealthier passengers had better access to lifeboats and survival.

Age: Younger children had a slightly higher chance of survival compared to older passengers, aligning with historical priorities.

Heatmap Correlation: The heatmap confirms that Fare and Pclass are strongly related (richer passengers purchased higher class tickets), and these two features have the highest positive and negative correlation with Survived, respectively.

✅ Conclusion and Next Steps
Summary of Findings:
Survival was overwhelmingly determined by a passenger's social status: Gender + Class + Wealth.
