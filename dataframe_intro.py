# Read the data from inp ut_df.txt into a pandas dataframe
# Print, the number of records, number of columns, column names
# Print summary stats for grade, print the mean and median separately after converting the summary stats to a dictionary
# Print frequency stats for class_rank
# Print the first 5 records and the last 5 records and 6th to 8th record
# Create a column for the letter grades (>=90: A, >=80: B, <80: C), use both apply and apply with lambda functions
# Create a column for the enrollment years
# Create a table (pivot type) for the number of students across the different letter grades and enrollment years and plot this data
# Drop the records with missing values in either class_rank or grade columns and save the data in a csv, text and excel file
# Drop the records with missing values in any of the columns and save the data in a csv, text and excel file




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('input.txt', sep='\t')
# print(df)
# print(df.info())
# print(df.describe())

# print(df['class_rank'].value_counts())
# print(df.isnull().sum())
# print(df.shape[1])
# print(len(df))


def get_letter_grade(value):
    if np.isnan(value):
        return np.nan
    elif value >= 90:
        return 'A'
    elif value >= 80:
        return 'B'
    else:
        return 'C'

# df['letter_grade'] = df['grade'].apply(get_letter_grade)
# df['letter_grade'] = df['grade'].apply(lambda value: get_letter_grade(value))
df['letter_grade'] = df.apply(lambda y: get_letter_grade(y['grade']), axis=1)
# print(df)

df_nomiss = df.dropna()
# print(df_nomiss)

df_nomiss1 = df.dropna(subset=['class_rank'])
# print(df_nomiss1)

df_nomiss2 = df.dropna(subset=['class_rank', 'grade'])
# print(df_nomiss2)

# print(df)

# df_nomiss3 = df.dropna(subset=['class_rank', 'grade'], how='all')
# print(df_nomiss3)


# print(df['letter_grade'].value_counts())

df['letter_grade'].value_counts().plot(kind='barh')

# print(df)


df['enroll_year'] = pd.DatetimeIndex(df['enroll_date']).year
# print(df)

# print(df.dtypes)

# print(df.groupby(['class_rank']).mean(numeric_only=True)['grade'])

# print(df.groupby(["class_rank"])['letter_grade'].value_counts())


# print(df.groupby(['class_rank', 'enroll_year'])['letter_grade'].value_counts())


def get_year_letter_df():
    year_letter_df = df.groupby(['enroll_year'])['letter_grade'].value_counts().to_frame()
    year_letter_df.columns = ['count']
    print(year_letter_df.index)
    year_letter_df = year_letter_df.reset_index()
    return year_letter_df

year_letter_df = get_year_letter_df()
print(year_letter_df)

def get_letter_year_df_sp(my_df, year):
    new_df = my_df[my_df['enroll_year'] == year].drop(['enroll_year'], axis = 1)
    new_df.columns = ['letter_grade', 'count_' + str(year)]
    return new_df


def get_merged_data(df1, df2):
    year_letter_df_all = pd.merge(df1, df2
                              ,on='letter_grade'
                              ,how="outer" )
    year_letter_df_all = year_letter_df_all.fillna(0)
    year_letter_df_all["count_2020"] = year_letter_df_all['count_2020'].astype('int')
    year_letter_df_all = year_letter_df_all.set_index(['letter_grade'])

    year_letter_df_all.plot(kind="bar")

    year_letter_df_all = year_letter_df_all.sort_index()

    return year_letter_df_all



year_letter_df_2019 = get_letter_year_df_sp(year_letter_df, 2019)
year_letter_df_2020 = get_letter_year_df_sp(year_letter_df, 2020)
year_letter_df_all = get_merged_data(year_letter_df_2019, year_letter_df_2020)


# print(year_letter_df_2019)
# print(year_letter_df_2020)



# Display Chart

# plt.figure()
# year_letter_df_all.plot(kind="bar")
# plt.title('Grade Distribution by Enrollment Year')
# plt.xlabel("Letter Grade")
# plt.ylabel("Count")
# plt.legend(loc="upper right")
# plt.xticks(rotation=45)
# plt.show()


print(year_letter_df)
# print(year_letter_df_all)

df_pivot = year_letter_df.pivot(index="letter_grade", columns="enroll_year", values="count")
df_pivot[2020.0] = df_pivot[2020.0].fillna(0)


df_pivot.columns = map(lambda x: f"count_{int(x)}", df_pivot.columns)


df_pivot = df_pivot.astype("int")

print(df_pivot)

df = df.sort_values(["class_rank", "letter_grade"], ascending=[False, True])
# print(df.groupby("class_rank").describe())
# print(df.groupby("class_rank").count())
# print(df[df["name"] == "jason" or "macy"].describe())

print(df.tail(10))

# print(dict(df.iloc[5]))


new_student = {
    "name": "caitlin",
    "class_rank": "junior"
}

new_student_df = pd.DataFrame([new_student])

df = pd.concat([df, new_student_df], ignore_index=True)
print(df)


# df.to_excel('df_excel_student.xlsx')

# df.to_csv("df_csv.csv", sep="\t")

# df.loc[len(df)] = {"name": "Chase"}

# print(df)
# print(df[("jason" in df["name"])].describe())


# my_list = [1,2,3]



# def test_function(rank, grade):
#     if rank == 'junior' and grade >= 85:
#         return'y'
#     else:
#         return 'n'

# df['test_col'] = df.apply(lambda x: test_function(x['class_rank'], x['grade']), axis=1)
# print(df)






# grades = list(df['grade'])
# print(grades)
# print(np.isnan(grades[2]))


# letter_grades = []

# for grade in grades:
#     if grade >= 90:
#         letter_grades.append('A')
#     elif grade >= 80:
#         letter_grades.append('B')
#     elif grade < 80:
#         letter_grades.append('C')
#     else:
#         letter_grades.append(np.nan)

# print(letter_grades)

# df['letter_grade'] = letter_grades
# print(df)


# print(df['grade'].describe()['50%'])

