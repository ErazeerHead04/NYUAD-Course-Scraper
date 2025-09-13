# NYUAD Course Scraper

## Executive Summary
This project scrapes course data from New York University Abu Dhabi’s course catalog.  
The official course list is loaded dynamically with JavaScript, so standard HTML scraping fails.  
By inspecting the network requests, we discovered a hidden XML API that provides structured course data.  

Our scraper connects to this API, validates and transforms the data, and outputs it in JSON format.  
This dataset can be used by students, advisors, and researchers for course planning, analysis, and visualization.

---

## Features
- Fetches course data from the **NYUAD public XML API**.  
- Implements retries and exponential backoff (respectful scraping).  
- Validates required fields (`code`, `title`).  
- Transforms fields (normalizes capitalization, parses credits).  
- Outputs to `data/sample_output.json` with ~1800 course records.  

---

## Repository Structure
```
project-name/
├── src/
│ ├── scraper.py # Main scraping logic
│ ├── validators.py # Data validation rules
│ ├── transformers.py # Data transformation pipeline
├── docs/
│ ├── ARCHITECTURE.md # Technical design decisions
│ ├── AI_USAGE.md # AI collaboration documentation
├── data/
│ └── sample_output.json # Example scraped data
├── requirements.txt
├── README.md
└── .gitignore
```


## Environment Setup

Clone this repository and set up a virtual environment:

**Create virtual environment**
```
python3 -m venv .venv
```

**Activate it (Linux/Mac/WSL)**
```
source .venv/bin/activate
```

**Install dependencies**
```
pip install -r requirements.txt
```
**Run Instructions**

From inside the project root:

```
cd src
python scraper.py
```

**Output will be saved to:**
```
../data/sample_output.json
```

**Technical Architecture**
```
API endpoint → scraper.py → validators.py → transformers.py → JSON output
```


## Performance Metrics
- API calls per run: 1 (bulk download of all courses).

- Records per run: ~1820.

- Error rate: 0% (with retries).

- Run time: ~2 seconds.

## Ethical & Legal Notes

- The scraper respects NYUAD’s robots.txt and only uses public API endpoints.

- No PII (personal identifiable information) is collected.

- Data is stored in JSON for educational use only.

## License

Educational use only. Not for commercial redistribution of scraped data.
