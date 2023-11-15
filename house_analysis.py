import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.formula.api import ols, logit
from sklearn.metrics import mean_absolute_error, confusion_matrix, classification_report

file_name= "kings_county_homedata.csv"


def main():

    df = get_house_data()
    df = df[df['price'] <= 1500000]
    print(df)

    df["year"] = pd.DatetimeIndex(df["date"]).year

    print(df[["date", "year"]])

    df = df[df["year"] == 2014]

    print(df["year"].value_counts())

    print(df["id"].nunique())

    houses_under_1_5 = df[df["price"] <= 1_500_000]

    # plt.figure()
    # plt.boxplot(houses_under_1_5["price"])
    # plt.show()


    # plt.figure()
    # plt.boxplot(df["price"])
    # plt.show()

    # print(df["price"].describe())

    # plt.figure()
    # plt.xlim(0, 2_000_000)
    # plt.xticks(np.arange(0, 1_500_000, 100_000), rotation=90)
    # plt.hist(houses_under_1_5["price"], bins=20, color="beige", edgecolor="gray")
    # plt.title("Home Price Distribution")
    # plt.xlabel("Price (Millions$)")
    # plt.ylabel("Number of Homes")

    median = houses_under_1_5["price"].median()
    mean = houses_under_1_5["price"].mean()

    plt.axvline(x = houses_under_1_5["price"].median(), ymin=0, ymax=1, label=f"Median {median}")
    plt.axvline(x = houses_under_1_5["price"].mean(), ymin=0, ymax=1, label=f"Median {median}")


    # plt.show()

    # print(df.columns)
    # print(df.info())
    # print(df.isnull().sum())
    # print(df["id"].nunique())
    # print(len(df))



    print(stats.pearsonr(df['price'], df['sqft_living']))
    print(stats.pearsonr(df['price'], df['id']))

    plt.figure()
    plt.scatter(df['sqft_living'], df['price'], s=1)
    plt.title("Price vs Sqft Living")
    plt.xlabel("Sqft Living")
    plt.ylabel("Price ($ Million)")
    # plt.show()


    # print(ols.pre)

    ols_model = ols("price ~ sqft_living + bedrooms + grade", df).fit()

    print(ols_model)

    print(ols_model.summary())

    print(ols_model.params["sqft_living"])

    df["price_pred"] = ols_model.predict(df[["sqft_living", "grade", "bedrooms"]])

    print(df[['price', 'price_pred']])

    # plt.figure()
    # plt.scatter(df["sqft_living"], df['price'], s=1, color='blue')
    
    # print(200.5197 / 1.848)


    sqft_living_coef = ols_model.params['sqft_living']
    print(sqft_living_coef)

    sqft_living_stderr = ols_model.bse['sqft_living']
    print(sqft_living_stderr)

    print(sqft_living_coef / sqft_living_stderr)

    print(df['grade'].value_counts())

    mae = mean_absolute_error(df["price"], df["price_pred"])

    print(mae)
    print(df["price"].mean())

    mse = mean_absolute_error(df["price"], df["price_pred"])
    print(mse)

    rmse = mse ** .5
    print(rmse)

    df['price_diff_abs'] = df.apply(lambda x: abs(x["price"] - x["price_pred"]), axis=1)
    df['price_diff_abs_squared'] = df.apply(lambda x: (x["price"] - x["price_pred"]) ** 2, axis=1)


    print(df['price_diff_abs'].mean())
    print(df['price_diff_abs_squared'].mean())

    df['price_high'] = df['price'].apply(lambda x: 1 if x > df['price'].mean() else 0)

    print(df[["price", "price_high"]])

    print(df["price_high"].value_counts() / len(df))

    low_avg_price_df = df[df["price_high"] == 0]
    high_avg_price_df = df[df["price_high"] == 1]

    print(low_avg_price_df["price_high"])



    # plt.figure()
    # plt.scatter(df["long"], df["lat"], s=1, c=df["price_bin"])
    # plt.show()
    
    # plt.scatter(df["sqft_living"], df['price'], s=1, color='blue')
    
    # print(200.5197 / 1.848)

    plt.figure()

    plt.scatter(high_avg_price_df["long"], high_avg_price_df["lat"], s=1, label="High", alpha=.5)
    plt.scatter(low_avg_price_df["long"], low_avg_price_df["lat"], s=1, label="Low", alpha=.5)

    plt.legend(loc=(1.01, .75))

    # plt.show()

    # Logit Model
    logit_model = logit("price_high ~ sqft_living + grade + view + bedrooms", df).fit()
    print(logit_model.summary())


    df["price_high_prob"] = logit_model.predict(df[['sqft_living', 'grade']])

    df['price_high_pred'] = df['price_high_prob'].apply(lambda x: 1 if x >= .5 else 0)

    print(df["price_high_pred"])

    print(df[["sqft_living", "price_high", "price_high_prob"]].sort_values("sqft_living"))

    plt.figure()
    plt.scatter(df['sqft_living'], df['price_high'], s=1,  alpha=.5)
    plt.scatter(df['sqft_living'], df['price_high_pred'], s=1, alpha=.5)
    plt.scatter(df['sqft_living'], df['price_high_prob'], s=1, alpha=.5)


    conf_mat= confusion_matrix(df["price_high"], df["price_high_pred"])
    class_report = classification_report(df["price_high"], df["price_high_pred"])

    print(conf_mat)
    print(class_report)

    plt.show()

    print("\nEnd of main\n")



def price_corr_analysis(df):
    price_cor = df.corr(numeric_only=True)["price"].abs().sort_values(ascending=False)

    print(df.corr(numeric_only=True)["sqft_living"])

    print(stats.pearsonr(df['price'], df['sqft_living']))
    print(stats.pearsonr(df['price'], df['id']))


def pull_house_data():
    file_url = "https://raw.githubusercontent.com/rashida048/Datasets/master/home_data.csv"
    df = pd.read_csv(file_url, sep=",")
    df.to_excel("kings_county_homedata.xlsx", index=False)
   
def get_house_data():
    return pd.read_csv(file_name)


main()