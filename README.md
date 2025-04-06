# DAV_project_152

## Overview

Basic data analysis using Python -- Numpy,Pandas and matplotlib.

## Getting Started

### Prerequisites

* Python 3.x
* Numpy (`pip install numpy`)
* Pandas (`pip install pandas`)
* Matplotlib (`pip install matplotlib`)

## Operations
 **NumPy:**

* **Array Creation:** `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`
* **Array Manipulation:** `array.shape`, `array.reshape()`, `np.concatenate()`, `np.split()`
* **Mathematical Operations:** Element-wise operations (`+`, `-`, `*`, `/`), `np.sin()`, `np.cos()`, `np.sqrt()`
* **Linear Algebra:** `np.dot()`, `np.linalg.solve()`, `np.linalg.eig()`
* **Statistical Functions:** `np.mean()`, `np.median()`, `np.std()`

  **Pandas**

* **Inspection:** `head()`, `tail()`, `info()`, `describe()`, `dtypes`
* **Selection:** `df['col']`, `df[['col1', 'col2']]`, `loc[]`, `iloc[]`, conditional selection
* **Cleaning:** Handle missing (`isnull()`, `dropna()`, `fillna()`), duplicates (`duplicated()`, `drop_duplicates()`), rename columns
* **Aggregation:** `mean()`, `sum()`, `count()`, etc.


**Matplotlib:**

* **Basic Plotting:** `plt.plot()`, `plt.scatter()`, `plt.bar()`
* **Customization:** `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.legend()`, `plt.grid()`
* **Subplots:** `plt.subplot()`
* **Saving Figures:** `plt.savefig('filename.png')`
* **Showing Plots:** `plt.show()`


## Dataset Description

The dataset `Global_Music_Streaming_Listener_Preferences.csv` contains information about music streaming listeners and their preferences. Key features include:

* **User_ID:** Unique identifier for each user.
* **Age:** Age of the listener.
* **Gender:** Gender of the listener.
* **Country:** Country of the listener.
* **Subscription Type:** Type of subscription (e.g., Premium, Free).
* **Minutes Streamed Per Day:** Average minutes of music streamed per day.
* **Number of Songs Liked:** Total number of songs liked by the listener.
* **Streaming Platform:** The music streaming platform used by the listener.
* **Device Used:** The primary device used for streaming.

## Key Findings

Based on the analysis:

* The dataset contains [Number of Rows] listeners across [Number of Columns] features.
* The age distribution of listeners can be observed from the histogram.
* There might be a relationship (or lack thereof) between the age of listeners and the average minutes they stream per day, as shown in the scatter plot.
* The bar plot reveals the popularity of different streaming platforms among the listeners in the dataset.
* The average minutes streamed per day varies across different countries.
* The average minutes streamed might also differ based on the subscription type.

**Note:** To provide more specific key findings, a deeper statistical analysis and interpretation of the visualizations would be required.

## Insights from Visualizations

* **Age Distribution Histogram:** Provides insights into the demographic makeup of the listeners by showing the frequency of different age groups. This can help understand the target audience.
* **Age vs. Minutes Streamed Scatter Plot:** Helps to identify any potential correlation or patterns between a listener's age and their daily streaming duration. This can inform user engagement strategies.
* **Streaming Platform Bar Plot:** Clearly shows the market share or user base of each streaming platform within this dataset. This is valuable for understanding platform popularity and potential market opportunities.




