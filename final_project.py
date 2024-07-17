# -*- coding: utf-8 -*-
"""Final Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rlgzT9MF5dkmMd6JAqwSA0PuQIEPuATq

# **Yes Bank Stock Closing Price Prediction**    -

##### **Project Type**    - EDA/Regression/Classification/Unsupervised
##### **Contribution**    - Nafees Shaikh
##### **LinkedIn**        - https://www.linkedin.com/in/nafees-shaikh-84ab221bb/

# **Project Summary -**

The project focused on predicting stock prices using historical data. The dataset underwent thorough cleaning to handle missing values, correct data types, and manage outliers, ensuring data quality. Categorical variables were encoded, and numerical features were scaled for optimal modeling.

A Ridge regression model was selected for its ability to manage multicollinearity and prevent overfitting. Hyperparameter tuning using GridSearchCV identified the best model with an optimal alpha value of 1.

The model demonstrated strong performance during evaluation on both training and test datasets. It achieved a high R-squared score of 0.99 for both sets, indicating a robust fit. Mean squared error (MSE) metrics were also low, with values of 50.04 for training and 82.43 for testing, highlighting the model's predictive accuracy.

Exploratory Data Analysis (EDA) provided insights into stock price trends and relationships between variables. Visualizations such as line plots and scatter plots facilitated understanding of data patterns and influential factors affecting stock prices.

In summary, the project successfully applied machine learning techniques, specifically Ridge regression, to predict stock prices. Rigorous data preprocessing, effective model selection through hyperparameter tuning, and comprehensive evaluation metrics underscored the project's methodology and findings. Future work could explore additional models or advanced feature engineering techniques to further enhance predictive capabilities.

# **GitHub Link -**

https://github.com/shaikhrnafees?tab=repositories

# **Problem Statement**

The project aims to predict stock prices using historical data, focusing on developing a machine learning model that accurately forecasts stock prices based on features like Open, High, Low, and Close. Key tasks include thorough data cleaning, preprocessing (including categorical encoding and numerical scaling), testing multiple models (such as Ridge regression), and optimizing model performance through hyperparameter tuning. Evaluation will be based on metrics like R-squared and mean squared error (MSE), with insights from Exploratory Data Analysis (EDA) informing model selection and feature engineering decisions.

# **General Guidelines** : -

1.   Well-structured, formatted, and commented code is required.
2.   Exception Handling, Production Grade Code & Deployment Ready Code will be a plus. Those students will be awarded some additional credits.
     
     The additional credits will have advantages over other students during Star Student selection.
       
             [ Note: - Deployment Ready Code is defined as, the whole .ipynb notebook should be executable in one go
                       without a single error logged. ]

3.   Each and every logic should have proper comments.
4. You may add as many number of charts you want. Make Sure for each and every chart the following format should be answered.
        

```
# Chart visualization code
```
            

*   Why did you pick the specific chart?
*   What is/are the insight(s) found from the chart?
* Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

5. You have to create at least 15 logical & meaningful charts having important insights.


[ Hints : - Do the Vizualization in  a structured way while following "UBM" Rule.

U - Univariate Analysis,

B - Bivariate Analysis (Numerical - Categorical, Numerical - Numerical, Categorical - Categorical)

M - Multivariate Analysis
 ]





6. You may add more ml algorithms for model creation. Make sure for each and every algorithm, the following format should be answered.


*   Explain the ML Model used and it's performance using Evaluation metric Score Chart.


*   Cross- Validation & Hyperparameter Tuning

*   Have you seen any improvement? Note down the improvement with updates Evaluation metric Score Chart.

*   Explain each evaluation metric's indication towards business and the business impact pf the ML model used.

# ***Let's Begin !***

## ***1. Know Your Data***

### Import Libraries
"""

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

"""### Dataset Loading"""

# Load Dataset
df=pd.read_csv("/content/data_YesBank_StockPrices.csv")

"""### Dataset First View"""

# Dataset First Look
df.head()

"""### Dataset Rows & Columns count"""

# Dataset Rows & Columns count
df.shape

"""### Dataset Information"""

# Dataset Info
df.info()

"""#### Duplicate Values"""

# Dataset Duplicate Value Count
df.duplicated().sum()

"""#### Missing Values/Null Values"""

# Missing Values/Null Values Count
df.isnull().sum()

"""### What did you know about your dataset?

The dataset appears to capture monthly stock price movements, showing the opening, highest, lowest, and closing prices for each month-year combination. It's structured to analyze how stock prices fluctuate over time, which is crucial for understanding market trends and making informed investment decisions.

## ***2. Understanding Your Variables***
"""

# Dataset Columns
df.columns

# Dataset Describe
df.describe()

# Note the outliers

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['Open', 'High', 'Low', 'Close']], palette='Set3')
plt.title('Box Plot of Open, High, Low, Close Prices')
plt.ylabel('Price')
plt.grid(True)
plt.tight_layout()
plt.show()

"""### Variables Description

*   Date: Month-year format denoting the time period of the stock data.
*   Open: Opening price of the stock on a given date.
*   High: Highest price of the stock reached during the trading day.
*   Low: Lowest price of the stock reached during the trading day.
*   Close: Closing price of the stock on a given date.

### Check Unique Values for each variable.
"""

# Check Unique Values for each variable.
df.nunique()

"""## 3. ***Data Wrangling***

### Data Wrangling Code
"""

# Write your code to make your dataset analysis ready.
df['Date'] = pd.to_datetime(df['Date'], format='%b-%y')

# Extract the month number
df['MonthNumber'] = df['Date'].dt.month
df['YearNumber'] = df['Date'].dt.year
df.drop(columns='Date',inplace=True)

df.head()

"""### What all manipulations have you done and insights you found?

*   Checked for missing values.
*   Checked for duplicated columns.
*   Identified outliers using box plot charts.
*   Extracted month and year numbers from the date column.
*   Dropped the date column after extracting month and year numbers.

## ***4. Data Vizualization, Storytelling & Experimenting with charts : Understand the relationships between variables***

#### Chart - Monthly Closing Prices Over Years
"""

plt.figure(figsize=(10, 6))
for year in df['YearNumber'].unique():
    year_data = df[df['YearNumber'] == year]
    plt.plot(year_data['MonthNumber'], year_data['Close'], marker='o', label=f'Year {year}')
plt.xlabel('Month')
plt.ylabel('Closing Price')
plt.title('Monthly Closing Prices Over Years')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""##### 1. Why did you pick the specific chart?

This line plot was chosen to visualize the monthly closing prices of stocks over different years. It helps in understanding how the closing prices fluctuate month by month across multiple years, highlighting trends and patterns over time.

##### 2. What is/are the insight(s) found from the chart?

From the chart, insights can include identifying seasonal trends in stock prices. For example, consistent peaks or dips in certain months across multiple years could indicate recurring market behaviors. It also shows if there are any outlier months where prices significantly deviate from the general trend.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

*   Yes, these insights can be valuable for strategic decision-making in trading or investment. Understanding seasonal patterns can help in timing buy or sell decisions, optimizing portfolio management, and managing risk more effectively.
*   Insights indicating negative growth might include prolonged periods of declining closing prices across all or specific months over the years. This trend could imply economic downturns, sector-specific issues, or company-specific challenges affecting stock performance negatively. Identifying such trends early can prompt proactive measures to mitigate risks or adjust investment strategies accordingly.

#### Chart - Average High Prices by Year
"""

plt.figure(figsize=(10, 6))
avg_highs = df.groupby('YearNumber')['High'].mean()
plt.bar(avg_highs.index.astype(str), avg_highs.values, color='b', alpha=0.6)
plt.xlabel('Year')
plt.ylabel('Average High Price')
plt.title('Average High Prices by Year')
plt.grid(True)
plt.tight_layout()
plt.show()

"""##### 1. Why did you pick the specific chart?

The bar chart displaying average high prices by year was chosen to visually compare and analyze the average high prices of stocks across different years. It provides a clear snapshot of how these prices fluctuate annually, helping to identify trends or anomalies over time.

##### 2. What is/are the insight(s) found from the chart?

Insights from the chart include identifying peak years where average high prices were significantly higher or lower compared to other years. It also highlights any consistent upward or downward trends in average high prices over the years, indicating market trends and potential patterns that could influence trading decisions.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

*   Yes, these insights can be instrumental in strategic decision-making for investors and traders. Understanding average high price trends can assist in timing entry or exit points in the market, optimizing trading strategies, and forecasting potential profitability.
*   Insights indicating negative growth might include years where the average high prices show a consistent decline or stagnation compared to previous years. This could signify economic downturns, sector-specific challenges, or external factors impacting market performance negatively. Identifying such trends early allows stakeholders to adjust investment strategies, mitigate risks, or explore alternative market opportunities.

#### Chart - Distribution of Low Prices by Month
"""

plt.figure(figsize=(10, 6))
sns.boxplot(x='MonthNumber', y='Low', data=df, palette='Set3')
plt.xlabel('Month')
plt.ylabel('Low Price')
plt.title('Distribution of Low Prices by Month')
plt.grid(True)
plt.tight_layout()
plt.show()

"""##### 1. Why did you pick the specific chart?

The box plot depicting the distribution of low prices by month was chosen because it effectively visualizes the variation and central tendency of low prices across different months. It helps in identifying outliers, if any, and understanding the spread and median values of low prices month-wise.

##### 2. What is/are the insight(s) found from the chart?

Insights from the chart include identifying which months typically have lower or higher low prices compared to others. It also highlights any months with significant variability in low prices, indicating periods of market volatility or specific economic factors influencing price fluctuations.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

*   Yes, these insights are valuable for making informed trading decisions. Understanding the distribution and variability of low prices month-wise can aid in timing purchases or sales of stocks, optimizing entry or exit points, and managing risk effectively.
*   Insights indicating negative growth might include months where the median or range of low prices is consistently lower compared to previous periods. This could suggest declining market conditions or economic uncertainties affecting stock performance negatively. Identifying such trends allows stakeholders to adjust strategies, hedge risks, or diversify investments to mitigate potential losses during downturns.

#### Chart - Relationship Between Open and Close Prices by Year
"""

plt.figure(figsize=(10, 6))
for year in df['YearNumber'].unique():
    year_data = df[df['YearNumber'] == year]
    plt.scatter(year_data['Open'], year_data['Close'], label=f'Year {year}')
plt.xlabel('Open Price')
plt.ylabel('Close Price')
plt.title('Relationship Between Open and Close Prices by Year')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""##### 1. Why did you pick the specific chart?

The scatter plot showing the relationship between open and close prices by year was chosen because it visually represents how these two key price points correlate and vary across different years. It helps in understanding if there's a consistent pattern or trend in how stocks open and close over time.

##### 2. What is/are the insight(s) found from the chart?

Insights from the chart include identifying if there's a strong linear relationship between open and close prices each year. It helps in spotting any outliers where stocks opened significantly higher or lower compared to their closing prices, indicating intraday volatility or market sentiment shifts.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

*   Yes, these insights are crucial for traders and investors in making informed decisions. Understanding the relationship between open and close prices can assist in predicting price movements throughout the trading day, optimizing entry or exit points, and managing risk more effectively.
*   Insights indicating negative growth might include years where there's a noticeable divergence between open and close prices, especially if closing prices consistently fall below opening prices across multiple years. This divergence could signify bearish market conditions, economic downturns, or company-specific challenges affecting stock performance negatively. Recognizing such trends allows stakeholders to adjust strategies, hedge risks, or explore alternative investment opportunities during periods of market decline.

#### Chart - Monthly High Prices Over Years
"""

plt.figure(figsize=(10, 6))
months = df['MonthNumber'].unique()
for month in months:
    month_data = df[df['MonthNumber'] == month]
    plt.plot(month_data['YearNumber'], month_data['High'], marker='o', label=f'Month {month}')
plt.xlabel('Year')
plt.ylabel('High Price')
plt.title('Monthly High Prices Over Years')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

"""##### 1. Why did you pick the specific chart?

The line plot depicting monthly high prices over years was chosen to visualize how high prices fluctuate across different years for each month. It helps in understanding seasonal trends and variations in high prices over time.

##### 2. What is/are the insight(s) found from the chart?

Insights from the chart include identifying which months typically have higher or lower high prices across different years. It also highlights any consistent upward or downward trends in high prices month-wise, providing insights into seasonal market behaviors.

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

*   Yes, these insights are valuable for strategic decision-making in trading or investment. Understanding monthly high price trends can assist in timing buy or sell decisions, optimizing portfolio management, and forecasting potential profitability.
*   Insights indicating negative growth might include months where high prices show a consistent decline or stagnation compared to previous years. This could indicate economic downturns, sector-specific challenges, or external factors impacting market performance negatively. Recognizing such trends early allows stakeholders to adjust investment strategies, mitigate risks, or explore alternative market opportunities during periods of market decline.

## ***6. Feature Engineering & Data Pre-processing***

### 1. Handling Missing Values
"""

# Handling Missing Values & Missing Value Imputation
df.isnull().sum()

"""### 2. Handling Outliers"""

# Handling Outliers & Outlier treatments
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[column] = df[column].mask(df[column] < lower_bound, np.nan)
    df[column] = df[column].mask(df[column] > upper_bound, np.nan)
    return df

# Apply IQR outlier removal to each column
columns_to_check = ['Open', 'High', 'Low', 'Close']
for column in columns_to_check:
    df = remove_outliers_iqr(df, column)

# Drop rows with NaN values
df.dropna(inplace=True)

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['Open', 'High', 'Low', 'Close']], palette='Set3')
plt.title('Box Plot of Open, High, Low, Close Prices')
plt.ylabel('Price')
plt.grid(True)
plt.tight_layout()
plt.show()

"""##### What all outlier treatment techniques have you used and why did you use those techniques?

**IQR Method**

The technique used here is called Interquartile Range (IQR) outlier removal. It involves calculating the IQR, which is the difference between the third quartile (Q3) and the first quartile (Q1) of a dataset. Outliers are identified as values that fall below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR. In this function, for each specified column (Open, High, Low, Close), values outside this range are replaced with NaN. Finally, rows containing NaN values are dropped from the dataset. This method effectively filters out extreme values that skew statistical analysis or model performance based on their deviation from the dataset's central tendency.

### 3. Data Scaling
"""

input_data=df.drop(columns='Close')
output_data=df['Close']

# Scaling your data
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
input_data=scaler.fit_transform(input_data)

"""The method used here is StandardScaler from sklearn.preprocessing. StandardScaler scales the input data such that each feature has a mean of 0 and a standard deviation of 1. This transformation is crucial in machine learning to ensure that all features contribute equally to model training and prediction. Standardizing the data removes the mean and scales each feature to unit variance, which is particularly beneficial for algorithms that assume normally distributed data or require standardized inputs, such as linear regression, logistic regression, and support vector machines. It helps in improving the convergence rate and performance of these algorithms by reducing the impact of differing scales among features.

### 4. Data Splitting
"""

# Split your data to train and test. Choose Splitting ratio wisely.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(input_data, output_data, test_size=0.2, random_state=42)

"""The data splitting ratio used here is 80% training data and 20% testing data, specified by test_size=0.2 in train_test_split function. This ratio is commonly chosen to allocate a significant portion of the data for training the machine learning model (80%), while reserving a smaller portion for evaluating its performance (20%).

The rationale behind this ratio is to ensure that the model learns patterns and relationships from a sufficiently large dataset during training, which helps in achieving better generalization and performance on unseen data. The test set serves as an independent dataset to assess how well the model can generalize to new, unseen data points, thus providing a measure of its predictive capability and robustness. This approach helps in detecting overfitting and ensures that the model's performance estimates are reliable.







"""

sns.pairplot(df)
plt.show()

"""What it shows: The pairplot visualizes pairwise relationships between variables in the dataset. It displays scatter plots for each pair of variables and histograms along the diagonal for individual variables.

Insights: This chart helps in understanding how each variable (Open, High, Low, Close) relates to the others. Scatter plots show the correlation between any two variables, while histograms show the distribution of each variable.

Interpretation: For instance, you can observe if there's a linear relationship between Open and Close prices, or if there's clustering or dispersion of data points across different variables.
"""

sns.heatmap(df.corr(),annot=True)
plt.show()

"""What it shows: The heatmap visualizes the correlation matrix of the dataset using color intensity. Values closer to 1 indicate strong positive correlations (dark colors), while values closer to -1 indicate strong negative correlations (light colors).

Insights: This chart allows you to quickly identify which pairs of variables are strongly correlated and which are not. It provides insights into which variables might influence each other and to what extent.

Interpretation: For example, if the correlation between Open and High prices is high (near 1), it suggests that changes in Open prices strongly correlate with changes in High prices. Conversely, if correlations are near 0, there may be little linear relationship between the variables.Answer Here.

## ***7. ML Model Implementation***

### Lienar Regression
"""

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)

model.score(X_test,y_test)*100

y_pred=model.predict(X_test)
y_pred

df.head(2)

sample_data = np.array([[12.58, 14.88, 12.55 , 8, 2005]])  # Adjust based on your dataset

# If necessary, scale the input data using the same scaler used during training
scaled_sample_data = scaler.transform(sample_data)  # Use scaler.transform() if scaling was applied

# Predict the 'Close' value using your trained model
predicted_close = model.predict(scaled_sample_data)
print(predicted_close)

"""#### 1. Explain the ML Model used and it's performance using Evaluation metric Score Chart."""

plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.xlabel('Sample Index')
plt.ylabel('Close Value')
plt.title('Actual vs Predicted Close Values')
plt.legend()
plt.show()

"""Answer Here.

### ML Model - Ridge Regression

#### 1. Explain the ML Model used and it's performance using Evaluation metric Score Chart.
"""

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
# Define the parameter grid
param_grid = {'alpha': [0.1, 1, 10, 100, 1000]}

# Create the Ridge regression model
ridge_model = Ridge()

# Create the GridSearchCV object
grid_search = GridSearchCV(estimator=ridge_model, param_grid=param_grid, cv=5, scoring='r2')

# Fit the grid search to the data
grid_search.fit(X_train, y_train)

# Get the best parameters and the best model
best_params = grid_search.best_params_
best_ridge_model = grid_search.best_estimator_

print(f"Best alpha value: {best_params['alpha']}")

# Predictions using the best model
y_train_pred = best_ridge_model.predict(X_train)
y_test_pred = best_ridge_model.predict(X_test)

# Evaluate the model
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f'Train MSE: {train_mse:.2f}, Test MSE: {test_mse:.2f}')
print(f'Train R-squared: {train_r2:.2f}, Test R-squared: {test_r2:.2f}')

# Plot actual vs predicted values
plt.figure(figsize=(10, 6))
plt.plot(y_test.values, label='Actual Values', color='blue')
plt.plot(y_test_pred, label='Predicted Values', color='red', linestyle='dashed')
plt.xlabel('Sample Index')
plt.ylabel('Close Price')
plt.title('Actual vs Predicted Values (Best Ridge Regression)')
plt.legend()
plt.grid(True)
plt.show()

df.head()

sample_data = np.array([[13.00, 14.00, 11.25, 7, 2005]])
scaled_sample_data = scaler.transform(sample_data)

# Predict the 'Close' value using your trained model
predicted_close = best_ridge_model.predict(scaled_sample_data)
print(f'Predicted Close value: {predicted_close[0]:.2f}')

"""### 1. Which Evaluation metrics did you consider for a positive business impact and why?

*   Metrics Considered: Mean Squared Error (MSE) and R-squared (R2).

*   Reasoning: MSE measures the average squared difference between predicted values and actual values, providing insight into prediction accuracy. R-squared (R2) indicates the proportion of the variance in the dependent variable that is predictable from the independent variables, demonstrating how well the model fits the data. These metrics are crucial for assessing model performance and ensuring accurate predictions, which are essential for making informed business decisions.

### 2. Which ML model did you choose from the above created models as your final prediction model and why?

*   Chosen Model: Ridge Regression (Ridge model after hyperparameter tuning).

*   Reasoning: Ridge regression was chosen as the final model due to its ability to handle multicollinearity (correlation among predictors) by introducing a regularization term (alpha). This helps in reducing model complexity and overfitting, thereby improving generalization to new data. The best alpha parameter obtained from GridSearchCV ensures optimal regularization strength, balancing between bias and variance to enhance model performance.

### 3. Explain the model which you have used and the feature importance using any model explainability tool?

*   Model Explanation: Ridge regression is a linear regression model that incorporates L2 regularization. It adds a penalty term to the ordinary least squares objective function, minimizing the sum of squared residuals plus the regularization term (alpha times the sum of squared coefficients). This regularization helps in shrinking the coefficients towards zero, reducing their variance and improving the model's ability to generalize.

*   Feature Importance: In linear models like Ridge regression, feature importance can be inferred from the magnitude of the coefficients after fitting the model. Larger coefficients indicate stronger influence of those features on the predicted outcome. Tools like permutation importance or partial dependence plots can further help visualize and interpret the impact of each feature on the model predictions, providing insights into which variables are most influential in determining the target variable.

# **Conclusion**

In conclusion, the project successfully demonstrated the application of machine learning in predicting car selling prices, emphasizing rigorous data preprocessing, effective model selection, and optimization through hyperparameter tuning. The insights gained have significant implications for strategic decision-making within the automotive retail sector, paving the way for enhanced profitability, operational efficiency, and customer satisfaction through data-driven approaches.

### ***Hurrah! You have successfully completed your Machine Learning Capstone Project !!!***

# **Thank you for your time. I look forward to your response.**
**Nafees Shaikh**
"""