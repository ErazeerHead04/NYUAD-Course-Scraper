# ARCHITECTURE.md

## Overview
This scraper collects course information from the NYUAD course catalog.  
The site’s course list page is rendered dynamically with JavaScript, which made initial HTML scraping attempts fail.  
By inspecting the **Network tab** in DevTools, we discovered a hidden XML API:
[](https://services.nyuad.nyu.edu/public/v2/academics/courses)


This API provides structured course data in XML format, which we parse, validate, and transform into JSON.

---

## System Components

### 1. `scraper.py`
- Fetches XML data from the NYUAD API with retries and exponential backoff.  
- Parses XML using **BeautifulSoup** in XML mode.  
- Extracts attributes like `peoplesoftID`, `title`, `description`, and `credits`.  
- Runs validation and transformation pipelines.  
- Saves output to `../data/sample_output.json`.

### 2. `validators.py`
- Defines rules for ensuring scraped data quality.  
- Required fields: `code` and `title`.  
- Rejects incomplete or malformed records.

### 3. `transformers.py`
- Cleans and normalizes fields:
  - Converts credits into integers (if possible).  
  - Capitalizes titles consistently.  
  - Can be extended to strip HTML tags from descriptions.

---

## Scraping Challenges and Solutions
| Challenge              | Difficulty (1–5) | Solution Strategy |
|-------------------------|------------------|-------------------|
| Dynamic JS content      | 3                | Bypassed by using hidden XML API |
| Rate limiting           | 2                | Retry logic + exponential backoff |
| Data structure variation| 2                | Validation and transformation pipeline |
| Session management      | 1                | Public API requires no authentication |

---

## Fallback Strategy
- If the API becomes unavailable:  
  - Use **Selenium** to render the dynamic course page.  
  - Scrape rendered HTML as a backup approach.  

---

## Data Flow Diagram
```
[API endpoint]
↓
fetch_courses()
↓
parse_xml()
↓
validate_record()
↓
transform_record()
↓
JSON output → data/sample_output.json
```

