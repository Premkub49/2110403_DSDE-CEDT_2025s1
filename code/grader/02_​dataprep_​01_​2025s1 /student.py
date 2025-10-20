import pandas as pd
from sklearn.model_selection import train_test_split

"""
    ASSIGNMENT 2 (STUDENT VERSION):
    Using pandas to explore Titanic data from Kaggle (titanic_to_student.csv) and answer the questions.
    (Note that the following functions already take the Titanic dataset as a DataFrame, so you don’t need to use read_csv.)

"""


def Q1(df):
    """
        Problem 1:
            How many rows are there in the "titanic_to_student.csv"?
    """
    # TODO: Code here
    
    return df.shape[0]


def Q2(df):
    '''
        Problem 2:
            2.1 Drop variables with missing > 50%
            2.2 Check all columns except 'Age' and 'Fare' for flat values, drop the columns where flat value > 70%
            From 2.1 and 2.2, how many columns do we have left?
            Note: 
            -Ensure missing values are considered in your calculation. If you use normalize in .value_counts(), please include dropna=False.
    '''
    # TODO: Code here
    # 2.1
    df = df.dropna(thresh=len(df) / 2, axis=1)
    # 2.2
    for col in df.columns:
        if col in ['Age', 'Fare']:
            continue
        most_flat = df[col].value_counts(normalize=True, dropna=False).max()
        if most_flat > 0.7:
            df = df.drop(col, axis=1)
    return df.shape[1]


def Q3(df):
    '''
       Problem 3:
            Remove all rows with missing targets (the variable "Survived")
            How many rows do we have left?
    '''
    # TODO: Code here
    df = df.dropna(subset='Survived')
    return df.shape[0]


def Q4(df):
    '''
       Problem 4:
            Handle outliers
            For the variable “Fare”, replace outlier values with the boundary values
            If value < (Q1 - 1.5IQR), replace with (Q1 - 1.5IQR)
            If value > (Q3 + 1.5IQR), replace with (Q3 + 1.5IQR)
            What is the mean of “Fare” after replacing the outliers (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here
    Q1_Fare = df["Fare"].quantile(0.25)
    Q3_Fare = df["Fare"].quantile(0.75)
    IQR = Q3_Fare - Q1_Fare

    def compare_Fare(value: float) -> float: 
        if Q1_Fare - (1.5 * IQR) > value:
            return Q1_Fare - (1.5 * IQR)
        elif Q3_Fare + (1.5 * IQR) < value:
            return Q3_Fare + (1.5 * IQR)
        return value

    df["Fare"] = df["Fare"].map(compare_Fare)
    return round(df["Fare"].mean(), 2)


def Q5(df):
    '''
       Problem 5:
            Impute missing value
            For number type column, impute missing values with mean
            What is the average (mean) of “Age” after imputing the missing values (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here
    for col in df.columns:
        numeric_but_categorical = ["PassengerId", "Survived", "Pclass"]
        if df[col].dtype in [int, float] and col not in numeric_but_categorical:
            mean = df[col].mean()
            df[col] = df[col].map(lambda x: mean if x is None else x)
    return round(df["Age"].mean().item(), 2)    


def Q6(df):
    '''
        Problem 6:
            Convert categorical to numeric values
            For the variable “Embarked”, perform the dummy coding.
            What is the average (mean) of “Embarked_Q” after performing dummy coding (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here
    df = pd.get_dummies(df)
    return round(df["Embarked_Q"].mean().item(), 2)


def Q7(df):
    '''
        Problem 7:
            Split train/test split with stratification using 70%:30% and random seed with 123
            Show a proportion between survived (1) and died (0) in all data sets (total data, train, test)
            What is the proportion of survivors (survived = 1) in the training data (round 2 decimal points)?
            Hint: Use function round(_, 2), and train_test_split() from sklearn.model_selection, 
            Don't forget to impute missing values with mean.
    '''
    # TODO: Code here
    from sklearn.model_selection import train_test_split
    copy_df = df.copy(deep=True)
    copy_df = copy_df[copy_df["Survived"].notna()]
    
    num_cols = copy_df.select_dtypes(include="number").columns.drop("Survived", errors="ignore")
    copy_df[num_cols] = copy_df[num_cols].fillna(copy_df[num_cols].mean())
    X = copy_df.drop(columns="Survived")
    y = copy_df["Survived"].astype(int)
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, stratify=y, random_state=123, train_size=0.7)
    
    # print(round(target.where(target == 1).count() / target.count(), 2))
    # print(round(target.where(target == 0).count() / target.count(), 2))
    # print(round(Y_test.where(Y_test == 1).count() / Y_test.count(), 2))
    # print(round(Y_test.where(Y_test == 0).count() / Y_test.count(), 2))
    return round(float(Y_train.mean()), 2)

