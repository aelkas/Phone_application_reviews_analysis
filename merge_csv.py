import pandas as pd

# Load the two CSV files into DataFrames
df1 = pd.read_csv('reviews_time.csv')
df2 = pd.read_csv('apple_reviews.csv')

# Concatenate the DataFrames
combined_df = pd.concat([df1, df2])

# Drop duplicate rows based on all columns
combined_df.drop_duplicates(inplace=True)

# Save the merged DataFrame to a new CSV file
combined_df.to_csv('merged_final_time.csv', index=False)
print(combined_df.shape[0])
print(df2.shape[0])
#df2.drop_duplicates(inplace = True)
#print(df2.shape[0])
print("Files merged successfully without duplicates.")
