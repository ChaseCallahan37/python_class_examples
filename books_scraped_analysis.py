import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from word2number import w2n

df = pd.read_csv("scraped_books.txt", sep="\t")

df["word_to_num_stars"] = df["stars_text"].apply(w2n.word_to_num)
df1 = df["word_to_num_stars"].value_counts().sort_index()
print(df1)

# plt.figure()
show = df["stars"].value_counts()
# plt.bar( show.index, show.values)
# plt.show()

import seaborn as sns

plt.figure()
sns.countplot(data=df, x="stars")
plt.show()

# plt.figure()
# plt.boxplot(df["price"])
# plt.show()

# df1.plot(kind="hist")
# plt.show()
# plt.show()

# df1 = df["stars"].value_counts().sort_index().to_frame()
# df1.pivot_table(columns="count", index="start")

# print(df1.to_frame())

# print(df)
# print(df.columns)
# print(df.shape)
# print(df.info())

# print(df.to_string())

# plt.figure()
# plt.hist(df['price'], bins=20, edgecolor='grey', color='crimson')
# plt.ylabel("Count")
# plt.xlabel("Price")
# plt.title("Price Distribution")
# print(df.max())
# plt.xlim(0, 100)
# plt.show()