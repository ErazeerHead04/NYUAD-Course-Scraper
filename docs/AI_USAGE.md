# AI_USAGE.md

## Exact Prompts Used
Here are some representative prompts I used with LLM during this project:
- "python3 scraper.py says ModuleNotFoundError: No module named 'bs4'. How to fix this?"
- "Why is my scraper returning 0 records, is this a parsing problem or the web page is not allowing?"
- "What are the other possible way to scrap if HTML parsing don't work?"
- "Does my project fulfill the requirements of web scraping?"
- "How to write Run Instructions in Markdown?"

Most of these prompts were about **syntax issues, documentation formatting, and fallback strategies**. The key implementation decisions (finding the API, structuring validation, getting it to work) were handled manually.

---

## AI-Generated vs Human-Written Code
- **AI-Generated (initial drafts, later modified by me):**
  - Basic scraper template with `requests` + `BeautifulSoup`.  
  - To get the knowledge of Web Scraping and all the possible way to web scrap.
  - Syntaxes whenever needed.
  - Requirements file (`requirements.txt`) and `.gitignore` template.  
  - Drafts of documentation files (`README.md`, `ARCHITECTURE.md`).  

- **Human-Written / Heavily Modified by Me:**
  - Corrected **scraper.py** to work with XML instead of HTML.  
  - Debugged the logic when 0 records were saved.  
  - Implemented final validation logic and transformations.  
  - Managed the GitHub repo structure and testing environment.   
  - Verified all output manually.  

In summary: **AI suggested scaffolding and structure, but implemention of the working solution was done manually.**

---

## Bugs in AI Suggestions and Fixes
- **Bug 1:** AI’s initial scraper targeted the HTML page → returned `0` records.  
  - **Fix:** I inspected DevTools, found the hidden XML API, and rewrote the scraper to fetch XML instead.  

- **Bug 2:** AI suggested selectors that didn’t exist in the XML schema.  
  - **Fix:** I manually reviewed the XML structure and adjusted parsing (`peoplesoftID`, `title`, `description`, etc.).  

- **Bug 3:** AI initially produced very verbose `.gitignore` (with packaging, eggs, etc.) unnecessary for this project.  
  - **Fix:** I simplified it to only `.venv/`, `__pycache__/`, and data dumps, keeping it aligned with course requirements.  

---

## Performance Comparisons
- **AI’s HTML-based approach:** Returned 0 results because the page was dynamically generated.  
- **My XML API approach:** Returned ~1820 valid course records in one request, clean and complete.  
- **Efficiency:**  
  - **API method:** ~2 seconds, single request, 0% error rate.  
  - **HTML scraping with Selenium fallback (not used):** Would have been much slower (~30–60 seconds) and less reliable.  

The chosen solution (API scraping) was **faster, more robust, and cleaner**.

---

## Lessons Learned
- AI is helpful for scaffolding, debugging syntax, and writing documentation.  
- Real scraping success required **manual analysis of network traffic, critical thinking, and debugging**.  
- I drove the problem-solving process, while AI acted as a **secondary assistant**.  

