import csv
import time
from app_store_scraper import AppStore

app_id = '835843051'  # Replace with the Apple App Store ID of the app
# A comprehensive list of country codes
country_codes = [
    'us', 'ca', 'gb', 'au', 'fr', 'de', 'it', 'es', 'mx', 'br', 'ar', 'jp', 'kr', 'cn', 'in', 
    'ru', 'za', 'ng', 'eg', 'sa', 'ae', 'tr', 'ir', 'pk', 'bd', 'vn', 'th', 'my', 'ph', 'sg', 
    'id', 'hk', 'tw', 'nl', 'be', 'se', 'dk', 'no', 'fi', 'ie', 'pl', 'cz', 'sk', 'at', 'ch', 
    'hu', 'gr', 'pt', 'ro', 'bg', 'si', 'hr', 'rs', 'ua', 'by', 'kz', 'uz', 'az', 'ge', 'am', 
    'il', 'jo', 'lb', 'kw', 'qa', 'bh', 'om', 'iq', 'sy', 'af', 'lk', 'mm', 'np', 'bt', 'mv', 
    'bn', 'la', 'kh', 'mn', 'kg', 'tj', 'tm', 'ee', 'lv', 'lt', 'lu', 'is', 'mt', 'cy', 'md', 
    'al', 'ba', 'mk', 'me', 'xk', 'ad', 'mc', 'sm', 'li', 'va', 'ws', 'to', 'tv', 'nr', 'ki', 
    'sb', 'vu', 'pg', 'fj', 'nc'
]
csv_filename = 'apple_reviews.csv'

def fetch_and_save_reviews(app_id, country_codes, csv_filename):
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'User Name', 'Rating', 'Review', 'Relevance'])

    for country in country_codes:
        time.sleep(1)
        app = AppStore(country=country, app_name="byblos-bank-mobile-banking", app_id=app_id)
        try:
            app.review(how_many=1000)  # Increase the number of reviews to fetch

            with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for review in app.reviews:
                    relevance = review.get('userRatingCount', 0)
                    writer.writerow([review['date'], review['userName'], review['rating'], review['review'], relevance])

            print(f"Completed fetching reviews for {country}. Total reviews fetched: {len(app.reviews)}")

        except Exception as e:
            print(f"An error occurred for {country}: {e}")

# Fetch and save reviews
fetch_and_save_reviews(app_id, country_codes, csv_filename)
