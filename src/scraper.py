"""
scraper.py
-----------
Main scraping script for Project 2.
Fetches course data from the NYUAD hidden XML API, parses it,
validates and transforms it, and saves it to JSON.

Usage:
    python scraper.py
"""

import requests               # For making HTTP requests
import json                   # For saving data to JSON
import time                   # For exponential backoff retries
from bs4 import BeautifulSoup # For XML parsing

# Import local validation and transformation modules
from transformers import transform_record
from validators import validate_record

# API endpoint discovered via DevTools inspection
COURSES_URL = "https://services.nyuad.nyu.edu/public/v2/academics/courses"

# Output file location
OUTPUT_PATH = "../data/sample_output.json"


def fetch_courses():
    """
    Fetch raw XML from the NYUAD courses API.
    Includes retries with exponential backoff to handle transient errors.
    """
    retries = 3
    backoff = 1  # start at 1 second

    for attempt in range(retries):
        try:
            print(f"Fetching data (attempt {attempt+1})...")
            response = requests.get(COURSES_URL, timeout=15)
            response.raise_for_status()
            return response.text  # return XML string

        except requests.RequestException as e:
            print(f"Error: {e}. Retrying in {backoff} seconds...")
            time.sleep(backoff)
            backoff *= 2  # double wait each time

    print("❌ Failed to fetch data after retries.")
    return None

def parse_xml(xml_text):
    """
    Parse XML text and extract course records.
    Handles namespaces and attributes.
    """
    soup = BeautifulSoup(xml_text, "xml")

    # Debug: preview
    print("\n--- XML Preview ---")
    print(xml_text[:500])
    print("--- End Preview ---\n")

    courses = []
    for c in soup.find_all(["course", "ns2:course"]):
        record = {
            # peoplesoftID is stored as an attribute
            "code": c.get("peoplesoftID"),
            "title": c.find("title").get_text(strip=True) if c.find("title") else None,
            "description": c.find("description").get_text(strip=True) if c.find("description") else None,
            "credits": c.find("credits").get_text(strip=True) if c.find("credits") else None,
        }
        courses.append(record)

    print(f"Found {len(courses)} course records in XML.")
    return courses



def main():
    # Step 1: Fetch raw XML
    xml_text = fetch_courses()
    if not xml_text:
        print("No data fetched. Exiting.")
        return

    # Step 2: Parse XML into records
    raw_records = parse_xml(xml_text)

    # Step 3: Validate + Transform
    cleaned_records = []
    for rec in raw_records:
        if validate_record(rec):          # ensure required fields exist
            cleaned_records.append(transform_record(rec))  # normalize

    # Step 4: Save cleaned records to JSON
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(cleaned_records, f, indent=2, ensure_ascii=False)

    print(f"✅ Scraped {len(cleaned_records)} valid records and wrote to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
