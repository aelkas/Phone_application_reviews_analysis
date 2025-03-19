import csv
from google_play_scraper import Sort, reviews_all

#app_package = 'mobi.foo.byblos.mbanking'
app_package = 'mobi.foo.byblos.mbanking'
csv_filename = 'reviews_time.csv'
countries = ['LB']  # List of country codes including UAE (Dubai), Qatar, Bahrain, and others
lang_code = 'en'  # Language code, change to 'ar' or other as needed

def fetch_and_save_reviews(app_package, csv_filename, countries):
    index = 0
    mode = 'w'  # Start with write mode to create the file

    with open(csv_filename, mode=mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'User Name', 'Rating', 'Review', 'Relevance'])

        for country in countries:
            print(f"Fetching reviews for country: {country}")

            # Fetch all reviews for the app
            result = reviews_all(
                app_package,
                lang=lang_code,
                country=country,
                sort=Sort.NEWEST
            )

            for review in result:
                relevance = review.get('thumbsUpCount', 0)
                #print(review)
                writer.writerow([review['at'], review['userName'], review['score'], review['content'], relevance])
                index += 1

                if index % 100 == 0:
                    print(f"Scraped {index} reviews.")

    print(f"Completed fetching reviews. Total reviews fetched: {index}")

# Fetch and save reviews
fetch_and_save_reviews(app_package, csv_filename, countries)
