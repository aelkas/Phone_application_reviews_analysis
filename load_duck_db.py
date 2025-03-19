import duckdb
import pandas as pd

# Load CSV into a Pandas DataFrame
csv_filename = 'merged_final_time.csv'
df = pd.read_csv(csv_filename)

# Explicitly convert columns to the correct types
df['Date'] = pd.to_datetime(df['Date'])  # Convert to datetime
df['User Name'] = df['User Name'].astype(str)  # Convert to string
df['Rating'] = df['Rating'].astype(int)  # Convert to integer
df['Review'] = df['Review'].astype(str)  # Convert to string
df['Relevance'] = df['Relevance'].astype(int)  # Convert to integer

# Rename DataFrame columns to match DuckDB table schema
df.rename(columns={'User Name': 'User_Name'}, inplace=True)

# Connect to DuckDB and create a new database file
db_filename = '' #### INSERT DATABASE NAME
conn = duckdb.connect(database=db_filename, read_only=False)

# Drop existing tables if necessary
conn.execute('DROP TABLE IF EXISTS reviews_staging')
conn.execute('DROP TABLE IF EXISTS reviews')

# Create a staging table in DuckDB with all columns as VARCHAR to handle any data issues
conn.execute('''
    CREATE TABLE IF NOT EXISTS reviews_staging (
        Date VARCHAR,
        User_Name VARCHAR,
        Rating VARCHAR,
        Review VARCHAR,
        Relevance VARCHAR
    )
''')

# Insert DataFrame into DuckDB staging table
conn.register('df_view', df)
conn.execute('INSERT INTO reviews_staging SELECT * FROM df_view')

# Create the final table in DuckDB with correct types
conn.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        Date TIMESTAMP,
        User_Name TEXT,
        Rating INTEGER,
        Review TEXT,
        Relevance INTEGER
    )
''')

# Insert data from the staging table to the final table with type casting
conn.execute('''
    INSERT INTO reviews (Date, User_Name, Rating, Review, Relevance)
    SELECT
        CAST(Date AS TIMESTAMP) AS Date,
        User_Name,
        CAST(Rating AS INTEGER) AS Rating,
        Review,
        CAST(Relevance AS INTEGER) AS Relevance
    FROM reviews_staging
''')

# Verify data insertion
result = conn.execute('SELECT COUNT(*) FROM reviews').fetchall()
print(f'Total reviews in database: {result[0][0]}')

# Close the connection
conn.close()
