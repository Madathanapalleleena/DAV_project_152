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

