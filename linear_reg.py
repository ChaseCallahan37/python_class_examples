import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("https://raw.githubusercontent.com/rashida048/Datasets/master/home_data.csv")
df.to_csv('kings_county_data.csv', index=False)

df = pd.read_csv('kings_county_data.csv')
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df['id'].nunique())
print(len(df))

print(df)
# df.to_excel('kings_county_homedata.xlsx',index=False)
print(df.columns)
print(df['date'])

df['year'] = pd.DatetimeIndex(df['date']).year
print(df[['date', 'year']])
print(df['year'].value_counts())

df = df[df['year'] == 2014]
print(df['year'].value_counts())
print(df['id'].nunique() / len(df))
print(df['price'].describe())

# plt.figure()
# plt.boxplot(df['price'])
# plt.show()

print(len(df[df['price'] <= 1500000]) / len(df))
print(len(df))

df = df[df['price'] <= 1500000]
print(df['price'].describe())





help(plt.axvline)



def price_distribution(df):
    median_price = df['price'].median()
    mean_price = df['price'].mean()
    
    plt.figure()
    plt.hist(df['price'], bins=20, edgecolor='gray', 
             color='beige')
    plt.axvline(x = median_price, ymin=0, ymax=1, 
                label=f'Median Price: {round(median_price/1000000, 2)}$ Mil', 
                linestyle='dashed', linewidth=3, color='blue')
    plt.axvline(x = mean_price, ymin=0, ymax=1, 
                label=f'Mean Price: {round(mean_price/1000000, 2)}$ Mil', 
                linestyle='dashed', linewidth=3, color='green')
    # plt.xlim(0, 2000000)
    plt.title("Home Price Distribution", fontsize=18, 
              color='crimson')
    plt.xlabel('Price (Million $)')
    plt.ylabel('Number of Homes')
    plt.xticks(np.arange(0, 1500000, 100000), rotation=90)
    plt.legend(fontsize=12)
    plt.show()
    
price_distribution(df)