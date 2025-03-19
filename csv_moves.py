import pandas as pd

def rem_col(col_to_remove,df):
    # Remove a column (e.g., 'column_to_remove')
    df.drop(col_to_remove, axis=1, inplace=True)

    # Save the updated DataFrame to a new CSV file
    df.to_csv('updated_file.csv', index=False)

    print("Column removed successfully.")

def rename_col(old_col_name,new_col_name, df):
    # Rename a column (e.g., from 'old_column_name' to 'new_column_name')
    df.rename(columns={old_col_name: new_col_name}, inplace=True)

    # Save the updated DataFrame to a new CSV file
    df.to_csv('updated_file.csv', index=False)

    print("Column renamed successfully.")

def change_col_loc(column_to_move, df):
    # Change the column's location (e.g., move 'column_to_move' to the first position)
    #column_to_move = 'column_to_move'
    columns = [column_to_move] + [col for col in df.columns if col != column_to_move]
    df = df[columns]

    # Save the updated DataFrame to a new CSV file
    df.to_csv('updated_file.csv', index=False)

    print("Column moved successfully.")

# Load the CSV file into a DataFrame
#df = pd.read_csv('merged_file.csv')

#rem_col(['App_Name','Company_Name','Page_URL','Official_website','Email','Address','Privacy_policy','Developer_Reply'],df)

# df = df.copy()
# df.to_csv("updated_byblos.csv", index = False)


# Load the two CSV files into DataFrames
# Read the CSV file
df2 = pd.read_csv('merged__final_file.csv')

# # Convert the date column to datetime, handling both date and datetime formats
# df2['Date'] = pd.to_datetime(df2['Date'], errors='coerce')

# # Format the date column to 'year-month-day'
# df2['Date'] = df2['Date'].dt.date

# # Drop duplicates
# df2.drop_duplicates(inplace=False)

# # Save the updated DataFrame back to a CSV file
# df2.to_csv('2_final_file.csv', index=False)
print(df2.shape[0])