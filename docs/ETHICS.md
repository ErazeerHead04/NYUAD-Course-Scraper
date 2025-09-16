
# NYUAD Course Scraper — Ethics & Legal Analysis

## Purpose
This project collects **public course metadata** (course code, title, description, credits) from the NYUAD course catalog. The data supports **student planning, advising efficiency, and academic research**. No personal or sensitive data is scraped.

---

## Legal Analysis
- **Robots.txt & Terms:** The endpoint (`/public/v2/academics/courses`) is public; no restrictions bypassed.  
- **CFAA (U.S.)**: Courts (e.g., *hiQ v. LinkedIn*) confirm scraping public data generally does not violate unauthorized access laws.  
- **DMCA:** No digital rights management circumvented.  
- **Local context:** This project is non-commercial, educational, and aligns with fair research practices.  

---

## Impact on Website Operations
- **Low load:** One bulk request per run retrieves the full catalog.  
- **Respectful scraping:** Retries use exponential backoff to avoid stressing servers.  
- **Update frequency:** Runs can be limited to once per semester, minimizing impact.  

---

## Privacy Considerations
- **No PII collected:** Only metadata about courses.  
- **Data minimization:** Store only essential fields for the product.  
- **Secure handling:** JSON data is stored locally; sensitive or large dumps can be `.gitignore`d.  

---

## Ethical Framework
We follow principles of:  
- **Beneficence:** Provide clear benefits to students, advisors, and researchers.  
- **Transparency:** Document AI vs human contributions (`AI_USAGE.md`).  
- **Respect:** Comply with requests from NYU if policies change.  
- **Alternatives-first:** If official APIs or datasets are released, prefer them over scraping.  

---

## Alternatives Considered
- **Official APIs:** Not documented or accessible to students.  
- **Manual entry:** Infeasible for ~1,800 records.  
- **Headless browser scraping:** Less efficient, more server load; avoided while XML API exists.  

---

## Educational Use Statement
This project is for **educational and research purposes only**. Any future commercial use would require explicit approval from the University and compliance with applicable law.

