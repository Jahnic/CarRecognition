# utils.py

import pandas as pd 

def get_locations():
    """Retrieves local data on craigslist locations"""
    df = pd.read_csv("../../../data/raw/cl_locations.csv")
    return df.loc[:, "0"]

def get_start_urls() -> list:
    """Retrieves local data of craigslist locations and returns list of locations in the form
    that is required for start urls"""
    locations = get_locations()
    start_urls = [(str(location) + "/") for location in locations]
    return start_urls

def get_allowed_domains() -> list:
    """Retrieves local data of craigslist locations and returns list of locations in the form
    that is required for allowed domains"""
    locations = get_locations()
    allowed_domains = [(str(location).replace('/search/cta', '')
                        .replace('https://', '') for location in locations)]
    return allowed_domains