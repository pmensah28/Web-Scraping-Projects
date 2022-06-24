# _*_ coding: utf-8 _*_
"""
Created on Fri June 24 14:39:57 2022

@author:Prince
"""

import glassdoor_scraper as gd
path = "/home/prince/Documents/Web_Scraping_Project/chromedriver"
df = gd.get_jobs('data scientist', 300, False, path, 15)
df.to_csv('glassdoor_jobs', index=False)