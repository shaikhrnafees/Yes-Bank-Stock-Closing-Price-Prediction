# Yes Bank Stock Closing Price Prediction

![Yes Bank Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Yes_Bank_SVG_Logo.svg/2560px-Yes_Bank_SVG_Logo.svg.png)

This project focuses on predicting stock prices using historical data of Yes Bank. The methodology involves thorough data cleaning, modeling, and evaluation to ensure accurate and reliable predictions.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Data Preprocessing](#data-preprocessing)
   - [Data Cleaning](#data-cleaning)
   - [Categorical Encoding](#categorical-encoding)
   - [Feature Scaling](#feature-scaling)
3. [Model Selection](#model-selection)
4. [Model Evaluation](#model-evaluation)
5. [Conclusion](#conclusion)
6. [Future Work](#future-work)
7. [References](#references)

## Project Overview
The project focuses on predicting the closing stock prices of Yes Bank using historical data. It employs machine learning techniques to derive insights and make accurate predictions.

## Data Preprocessing

### Data Cleaning
Data cleaning is a crucial step in the data preprocessing pipeline. It involves the following sub-steps:

1. **Handling Missing Values:**
   - Identified missing values within the dataset.
   - Used appropriate methods to fill or remove these values, depending on their impact on the dataset. For instance, rows with excessive missing data might be dropped, while smaller gaps can be filled using techniques such as forward fill or interpolation.

2. **Correcting Data Types:**
   - Ensured that each column in the dataset had the correct data type (e.g., converting date columns to `datetime` type, numerical columns to `float` or `int`).
   - This step is essential for accurate calculations and analyses later on.

3. **Managing Outliers:**
   - Analyzed the data for outliers using methods like the Interquartile Range (IQR) or Z-scores.
   - Outliers were addressed either by removing them or transforming them if they were deemed to significantly skew the results.

4. **Removing Duplicates:**
   - Checked for duplicate entries within the dataset and removed them to maintain the integrity of the analysis.

<p align="center">
  <img src="https://camo.githubusercontent.com/0627dec620568c918ffe0b8856f2144bee19c975c34f8f05e9f99292cc03dfbf/68747470733a2f2f6173736574732d676c6f62616c2e776562736974652d66696c65732e636f6d2f3563313931303063326235303037336536656536396461312f3630643335393637613835336131623134383531373033625f416c6c253230746865253230646174612532302831292e676966" alt="Data Cleaning GIF" />
</p>

### Categorical Encoding
- Categorical variables were identified and encoded using techniques such as one-hot encoding or label encoding. This step ensures that categorical data can be effectively utilized in the machine learning model.

### Feature Scaling
- Numerical features were scaled using techniques like Min-Max Scaling or Standardization. This process is crucial for algorithms like Ridge regression that are sensitive to the scale of input features.

## Model Selection
- **Algorithm Used:** A Ridge regression model was selected due to its ability to manage multicollinearity and prevent overfitting.
- **Hyperparameter Tuning:** Utilized GridSearchCV to identify the best model, resulting in an optimal alpha value of 1.

<p align="center">
  <img src="https://i.gifer.com/OyGx.gif" alt="Model Selection GIF" />
</p>

## Model Evaluation
- The model demonstrated strong performance during evaluation on both training and test datasets.
- Achieved a high R-squared score of **0.99** for both sets, indicating a robust fit.
- Mean Squared Error (MSE) metrics were low, with values of **50.04** for training and **82.43** for testing, highlighting the model's predictive accuracy.

## Conclusion
This project successfully applied machine learning techniques, specifically Ridge regression, to predict stock prices of Yes Bank using historical data. The meticulous data preprocessing ensured that the dataset was clean, relevant, and appropriately formatted, which is crucial for building effective predictive models.

The Ridge regression model outperformed expectations, achieving a high R-squared score of **0.99**, which indicates that the model explains 99% of the variance in the stock prices. Such a high level of accuracy is indicative of the effectiveness of the chosen features and the model itself.

Additionally, the project highlighted the importance of thorough exploratory data analysis (EDA) and model evaluation metrics, such as Mean Squared Error (MSE), in understanding model performance and refining predictive capabilities. This not only provides a robust methodology for predicting stock prices but also serves as a foundation for applying similar techniques to other financial datasets.

In conclusion, this project not only demonstrates the practical application of machine learning in finance but also emphasizes the need for continuous improvement and adaptation in model development to achieve even greater predictive accuracy in future endeavors.

## Future Work
Future work could explore additional models or advanced feature engineering techniques to further enhance predictive capabilities. Considerations for using more complex algorithms, like LSTM or other deep learning approaches, could also be beneficial in capturing the temporal aspects of stock price movements.

## References
- [Data Source](https://github.com/shaikhrnafees/Yes-Bank-Stock-Closing-Price-Prediction/blob/main/data_YesBank_StockPrices.csv)
- [Python Colab File](https://github.com/shaikhrnafees/Yes-Bank-Stock-Closing-Price-Prediction/blob/main/final_project.py)
