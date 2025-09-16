

# NYUAD Course Scraper — Business Case

## Executive Summary
The **NYUAD Course Scraper** extracts structured course data from a hidden XML API, transforming it into JSON for search, planning, and analysis. It processes ~1,800 records in ~2 seconds with validation and transformation.  

We propose **CourseGraph**: a product that helps students plan courses, advisors optimize curricula, and researchers analyze trends. NYUAD serves as the pilot market, with expansion potential across NYU and other universities.

---

## Problem & Market Opportunity
- **Students:** Current catalog is slow and hard to filter. Planning requires juggling multiple tabs.  
- **Advisors:** No easy way to see curriculum balance or identify bottlenecks.  
- **Researchers:** Lack reproducible, bulk course datasets for academic studies.  

**Market size:** ~2,000 students and ~200 advisors at NYUAD, with scaling opportunities to 50k+ students across NYU campuses.

---

## Why XML API over HTML Parsing?
- The NYUAD course catalog is rendered dynamically with **JavaScript**, which blocks traditional HTML scrapers.  
- Initial HTML-based attempts returned **zero records** because the DOM was empty without JS execution.  
- By inspecting network requests, we discovered a **hidden XML API** that exposes all course data in structured form.  
- **Advantages:**  
  - Faster: one bulk call vs. hundreds of page loads.  
  - Cleaner: structured XML fields map directly to JSON.  
  - Reliable: no need for Selenium or brittle DOM selectors.  

This choice made the scraper **simpler, more robust, and ethically lighter** (minimal server load).

---
## Solution Overview
- **Scraper workflow:** Fetch XML → validate (`code`, `title`) → normalize fields → output JSON.  
- **Data product:**  
  - Student planner with conflict detection & credit tracking.  
  - Advisor dashboard for curriculum monitoring.  
  - Research dataset exports.  

The pipeline ensures quality via validation rules and transformers that clean and standardize records.

---

## Value Proposition
- **For students:** Simplifies planning, reduces mistakes in registration.  
- **For advisors:** Provides fast insights into workloads, oversubscribed classes, and gaps.  
- **For researchers:** Offers structured, reusable data for longitudinal curriculum studies.  

---

## Pricing Model
- **Freemium:** Free JSON datasets and planner tools for students.  
- **Premium tiers:**  
  - Advisor/Admin dashboards: \$5–\$10 per user/month.  
  - Research datasets: \$500–\$1,000 per semester with versioning.  
- **Future B2B:** Licensing to EdTech startups and expansion to other institutions.  

---

## Competition
- **Coursicle / ClassCentral:** Good UI, weak research access.  
- **University systems (NYU Albert):** Sufficient for registration but not for analytics.  
- **Generic scrapers:** Brittle and limited; our method is robust and efficient.  

**Our differentiator:** API-based scraping with clean, consistent JSON ready for analytics and visualization.

---

## Roadmap
1. Deploy student-facing planner at NYUAD.  
2. Release advisor dashboard prototype.  
3. Package and share research datasets.  
4. Scale to NYU NY/Shanghai and other universities.  

