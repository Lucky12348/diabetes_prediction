import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# A function that allows to check if the data points data types corresponds to their columns' data type
def dtype_per_column(df):
    # Initialize the result dictionary
    dtype_counts = {}

    # Loop through each column in the dataframe
    for col in df.columns:
        dtype_count = {}

        # Count the data types in each column
        for value in df[col]:
            dtype_name = type(value).__name__
            dtype_count[dtype_name] = dtype_count.get(dtype_name, 0) + 1
        
        # Convert the count for each column into the desired format
        dtype_counts[col] = [f"{dtype}:{count}" for dtype, count in dtype_count.items()]

    # Create the new DataFrame and transpose it to align data types as rows
    new_df = pd.DataFrame(dtype_counts).T
    
    return new_df.T

# A function that allows to generate and compare descriptive statistics for a specific column across multiple dataframes
def compare_statistics_per_col(dataframes, dataframes_names, column):
    descriptive_statistics = []
    
    for df in dataframes:
        statistics = df[column].describe()
        descriptive_statistics.append(statistics)
    
    result = pd.concat(descriptive_statistics, axis=1, keys=dataframes_names)

    print("---" * 10)
    print(f"Comparison of descriptive statistics for \x1B[4m{column}\x1B[0m:")
    print("---" * 10)
    return result

# A function that allows to generate and compare histograms for a specific column across multiple dataframes
def compare_histograms_per_col(dataframes, dataframes_names, column):

    n = len(dataframes)
    fig, axes = plt.subplots(ncols=n, nrows=1, figsize=(5 * n, 4))
    
    for i in range(n):
        ax = axes[i]
        df = dataframes[i]
        name = dataframes_names[i]
        sns.histplot(data=df, x=column, ax=ax, kde=True)
        ax.set_title(f"{name}")
    
    print("---" * 10)
    print(f"Comparison of data distributions for \x1B[4m{column}\x1B[0m:")
    print("---" * 10)
    
    plt.tight_layout()
    plt.show()


# A function that generates point cloud from two difference columns of the dataset. 
def point_clouds_per_col(dataframes, dataframes_names, column0, column1):

    n = len(dataframes)
    fig, axes = plt.subplots(ncols=n, nrows=1, figsize=(5 * n, 4))
    
    for i in range(n):
        name = dataframes_names[i]
        axes[i].scatter(dataframes[i][column0], dataframes[i][column1])
        axes[i].set_title(f"{column0} vs.  {column1}: {name} group")
        axes[i].set_xlabel(f"{column0}")
        axes[i].set_ylabel(f"{column1}")
            
    plt.tight_layout()
    plt.show()



# A function that generates heat map from two difference columns of the dataset. 
def heatmap_per_col(dataframes,dataframes_names, column0, column1):
    n = len(dataframes)

    fig, axes = plt.subplots(ncols=n, nrows=1, figsize=(5 * n, 4))
    for i in range(n):
        name = dataframes_names[i]
        sns.kdeplot(x=dataframes[i][column0],y=dataframes[i][column1],fill=True,cmap='hot', ax=axes[i])

        axes[i].set_title(f"{column0} vs.  {column1}: {name} group")
        axes[i].set_xlabel(f"{column0}")
        axes[i].set_ylabel(f"{column1}")
            
    plt.tight_layout()
    plt.show()


# A function that allows to check of the top 10 most frequent values per column in a dataframe
def top_10_frequent_values(df,col_name = None):#add col_name, optional parameter to print only values for selected column
    if(col_name is None):
        for col in df:
            print(f"Top 10 most frequent values for \x1B[4m{col}\x1B[0m::")
            print(df[col].value_counts().head(10))
            print("\n")
    else:
        print(f"Top 10 most frequent values for \x1B[4m{col_name}\x1B[0m::")
        print(df[col_name].value_counts().head(10))
        print("\n")
# A function that allow to check of duplicated data points per column
def duplicate_cells_per_column(df):
    for col in df.columns:
        print(f"{col}: {df[col].duplicated().sum()}")

