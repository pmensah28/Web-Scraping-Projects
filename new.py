import glassdoor_scraper as gs
import pandas as pd
path = "/home/prince/Documents/Web_Scraping_Project/chromedriver"
df = gs.get_jobs('data_scientist',15, False, path, 15)
print(df)