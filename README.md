# MyPreprocessingDataSetExample
# Preprocessing titanic dataset

Data preprocessing is an crucial step in Machine Learning as the quality of data and the useful information that can be derived from it directly 
affects the ability of your model to learn so preprocessing is done with sequence of steps.

These are the steps for starting the project

1. Input the Dataset
      For testing out my application I used a very popular ML dataset - Titanic survival Dataset. 

2. Data Description
      In this step we can correctly show some basic statistical details (mean, standard deviation, percentiles, total number of values, maximum, minimum), 
      datatype of columns of the dataset using methods provided by pandas library.
      
3. Handling NULL Values
    The next step of data preprocessing is to handle missing data in the datasets. 
    If dataset contains some missing data, then it may create a huge problem for your machine learning model. 
    Hence it is necessary to handle missing values present in the dataset.
    The idea is to remove all the NULL values from the dataset.

4. Encoding Categorical Data
    Machine learning models completely works on mathematics and numbers, 
    but if our dataset have a categorical variable, it may create trouble while building the model. 
    So, it is necessary to encode these categorical variables into numbers.
    
5. Feature Scaling
    If feature scaling is not done, then a machine learning algorithm will weigh greater values, higher and 
    consider smaller values as the lower values, regardless of the unit of the values. 
    To avoid this, feature scaling is done.


6. Download the dataset
    The idea is to download the modified and preprocessed dataset in the correct file format, in my case it is CSV.
