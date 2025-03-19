import duckdb as ddb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

db_filename = 'reviews.db'
conn = ddb.connect(database=db_filename, read_only=True)

def count_reviews():
    result = conn.execute(''' 
        SELECT COUNT(*) AS number_of_reviews FROM reviews
    ''').fetchone()
    print(f"Number of reviews: {result[0]}")

def avg_by_year():
    result = conn.execute( '''
    SELECT
        strftime('%Y', Date) AS Year,
        AVG(Rating) AS Average_Rating
    FROM
        reviews
    GROUP BY
        Year
    ORDER BY
        Year
    ''').fetch_df()
    fig = plt.figure(figsize=(6,6))
    plt.ylabel("Average_ratings")
    plt.xlabel("Years")
    #month = np.array([x[5:] for x in result['Month_Year']])
    plt.plot(result['Year'],result['Average_Rating'])
    plt.show()
    return result

def count_per_year_histogram():
    result2 = conn.execute('''
        SELECT strftime('%Y', Date) AS Year, COUNT(Rating) AS No
        FROM reviews
        GROUP BY Year
        ORDER BY YEAR ASC;
    ''').fetchdf()
    plt.figure(figsize=(10, 6))
    plt.bar(result2['Year'], result2['No'], color='blue')
    plt.xlabel('Year')
    plt.ylabel('Number of Ratings')
    plt.title('Number of Ratings per Year')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.show()
    return result2

def sort_by_date(limit):
    result = conn.execute('''
        SELECT (*) FROM reviews
        ORDER BY DATE DESC LIMIT '''+str(limit)).fetchdf()
    return result

def sort_by_rating(limit):
    result = conn.execute('''
        SELECT * FROM reviews
        ORDER BY Rating DESC LIMIT '''+str(limit)).fetchdf()
    return result

def sort_by_relevance():
    result = conn.execute(''' 
        SELECT (*) FROM reviews 
        WHERE Relevance >1 
        ORDER BY Relevance DESC
        --LIMIT 30;
    ''').fetchdf()
    return result

def sort_by_rating_and_relevance(ascRel, ascRat):
    stringosRel= ('ASC' if ascRel else 'DESC')
    stringosRat = ('ASC' if ascRat else 'DESC')
    query = '''SELECT (*) FROM (
        SELECT (*) FROM reviews 
        WHERE Relevance >1 
        ORDER BY Relevance '''+stringosRel+''') ORDER BY Rating 
        '''+stringosRat +' LIMIT 10;'
    result = conn.execute(query).fetchdf()
    return result

def ratings_of_most_relevant():
    result = conn.execute(''' 
        SELECT Rating, Relevance FROM reviews 
        WHERE Relevance >1 
        ORDER BY Relevance DESC
        --LIMIT 30;
    ''').fetchdf()
    return result


def avg_time_of_review():
    average_time_query = '''
    SELECT AVG(EXTRACT(EPOCH FROM Date) % 86400) AS avg_seconds_past_midnight
    FROM reviews
    '''

    avg_seconds_past_midnight = conn.execute(average_time_query).fetchall()[0][0]

    # Convert seconds past midnight to HH:MM:SS format
    average_time_of_day = str(datetime.timedelta(seconds=avg_seconds_past_midnight))
    print(f'Average time of review: {average_time_of_day}')

avg_time_of_review()
print(sort_by_date(20))
conn.close()