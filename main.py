import numpy as np 
import pandas as pd 
# Loading the dataset into a Pandas DataFrame
df = pd.read_csv('Global_Music_Streaming_Listener_Preferences.csv')

print("displaying first 5 rows of the dataset")
print(df.head())

#introduction to numpy
print("datatypes of the columns")
print(df.dtypes)
print("\n")
print("shape of the dataset")
row,col=df.shape
print(f"no.of rows int the dataset: {row} and no. of columns in the dataset:{col}")
print("\n")

#creating arrays from df columns
print("creating arrays from df columns")
a=np.array(df['Age'])
print("numpy array of age col:",a[:5])

#array indexing
print("first element in the age array:",a[0])
print("last element in the age array:",a[-1])

#array slicing
print("age elements from 2 to 5:",a[2:5])

#reshaping the array
minutes_streamed = np.array(df['Minutes Streamed Per Day'])
print("minutes streamed array:",minutes_streamed[:5])
print("first element in the minutes streamed array:",minutes_streamed[0])
print("reshaping the array")
print("original shape of the array:",minutes_streamed.shape)

reshaped_minutes = minutes_streamed.reshape(len(minutes_streamed), 1)  # Reshape to a column vector
print("reshaped array:",minutes_streamed.reshape(len(minutes_streamed),1))
print("Reshaped Minutes Streamed array (column vector):\n", reshaped_minutes[:5])
print("\n")

# Array concatenation and splitting
array_concat = np.concatenate((a[:5], [100, 101]))
print("Concatenated array:", array_concat)
print("\n")

age_split = np.split(a, 2) # Split into 2 sub-arrays
print("Split arrays:", age_split)
print("Length of split arrays:", len(age_split))
print("Split array (first part):\n", age_split[0][:5])
print("Split array (second part):\n", age_split[1][:5])
print("\n")

liked_songs = np.array(df['Number of Songs Liked'])
print("liked songs array:",liked_songs[:5])
# Universal Functions (ufuncs)
squared_liked_songs = np.square(liked_songs)
print("Squared number of liked songs (first 5):\n", squared_liked_songs[:5])
print("\n")


ages=np.array(df['Age'])
print("ages array:",ages[:5])
# Aggregations
mean_age = np.mean(ages)
max_minutes = np.max(minutes_streamed)
print("Mean Age:", mean_age)
print("Maximum Minutes Streamed:", max_minutes)
print("\n")

# Broadcasting rules
age_plus_5 = ages + 5
print("Ages plus 5:", age_plus_5[:5])
print("\n")

# Comparisons
older_than_30 = ages > 30
print("Ages older than 30 (boolean array):\n", older_than_30[:10])
print("\n")

# Boolean Arrays and Masks
users_over_30 = ages[older_than_30]
print("Ages of users older than 30 (first 10):\n", users_over_30[:10])
print("\n")

# Fancy Indexing
specific_indices = [0, 5, 10]
selected_ages = ages[specific_indices]
print("Ages at specific indices:", selected_ages)
print("\n")

# Fast Sorting using np.sort and np.argsort
sorted_minutes = np.sort(minutes_streamed)
print("Sorted Minutes Streamed (first 5):", sorted_minutes[:5])

indices_sorted_by_likes = np.argsort(liked_songs)
print("Indices sorted by Number of Songs Liked (first 5):\n", indices_sorted_by_likes[:5])
print("Liked songs in sorted order (first 5):\n", liked_songs[indices_sorted_by_likes[:5]])
print("\n")



print("Pandas Operations")

# Series Object
cs = pd.Series(df['Country'])
print("Pandas Series of Countries (first 5):\n", cs.head())
print("\n")

# Data Frame Object (df is already a DataFrame)
print("DataFrame Info:")
df.info()
print("\n")

# Data Indexing and Selecting for Series
print("First country in the Series:", cs[0])
print("Countries at index 2 to 4:\n", cs[2:5])
print("\n")

# Data Indexing and Selecting for Data Frames
print("DataFrame with only 'User_ID' and 'Age' columns:\n", df[['User_ID', 'Age']].head())
print("\n")
print("Row at index 1 of the DataFrame:\n", df.loc[1])
print("\n")
print("Value in the 'Streaming Platform' column at index 3:", df.iloc[3, df.columns.get_loc('Streaming Platform')])
print("\n")

# Universal Functions for Index Preservation
def add_prefix(country):
    return "Country: " + country

countries_with_prefix = cs.map(add_prefix)
print("Series with added prefix:\n", countries_with_prefix.head())
print("\n")

# Index Alignment and Operations between Series and Data Frames
age_series = pd.Series(df['Age'], index=df['User_ID'])
minutes_series = pd.Series(df['Minutes Streamed Per Day'], index=df['User_ID'])

am = age_series + minutes_series 
print("Age + Minutes Streamed (first 5):\n", am.head())
print("\n")

# Handling missing data, operating on Null values
print("Checking for null values in the DataFrame:")
print(df.isnull().sum()) 
print("\n")

# Hierarchical Indexing
hierarchical_index = df.set_index(['Country', 'Streaming Platform'])
print("DataFrame with Hierarchical Index (first 5 rows):\n", hierarchical_index.head())
print("\n")
#combining dataframes
# Create a second sample DataFrame for demonstration
data2 = {'User_ID': ['U1000', 'U1005', 'U1025'],
         'Favorite Color': ['Blue', 'Green', 'Red']}
df2 = pd.DataFrame(data2)
print("Second DataFrame (df2):\n", df2)
print("\n")

# Concat
concatenated_df = pd.concat([df.head(3), df2], ignore_index=True)
print("Concatenated DataFrame:\n", concatenated_df)
print("\n")

# Append
appended_df = df.head(3).append(df2, ignore_index=True)
print("Appended DataFrame:\n", appended_df)
print("\n")

# Merge and Joins
merged_df = pd.merge(df, df2, on='User_ID', how='left') # Left join
print("Merged DataFrame (left join):\n", merged_df.head())
print("\n")

# Aggregation and Grouping
average_minutes_by_country = df.groupby('Country')['Minutes Streamed Per Day'].mean()
print("Average Minutes Streamed Per Day by Country:\n", average_minutes_by_country)
print("\n")

# Pivot Tables
pt = pd.pivot_table(df, values='Minutes Streamed Per Day', index='Country',
                            columns='Subscription Type', aggfunc='mean')
print("Pivot Table (Average Minutes Streamed by Country and Subscription Type):\n", pt)

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))  # Adjust figure size if needed
plt.hist(df['Age'], bins=20, edgecolor='black')
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Number of Users')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Minutes Streamed Per Day'])
plt.title('Age vs. Minutes Streamed Per Day')
plt.xlabel('Age')
plt.ylabel('Minutes Streamed Per Day')
plt.grid(True)
plt.show()

platform_counts = df['Streaming Platform'].value_counts()
plt.figure(figsize=(10, 6))
platform_counts.plot(kind='bar', edgecolor='black')
plt.title('Number of Users per Streaming Platform')
plt.xlabel('Streaming Platform')
plt.ylabel('Number of Users')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()