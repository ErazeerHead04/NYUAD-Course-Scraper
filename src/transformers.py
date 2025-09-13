"""
transformers.py
----------------
Transformation pipeline for scraped course data.
Adds derived fields, normalizes text, etc.
"""

def transform_record(record):
    """
    Apply transformations to a single record.
    Example: normalize title capitalization, convert credits to integer if possible.
    """
    new_record = record.copy()

    # Normalize title
    if new_record.get("title"):
        new_record["title"] = new_record["title"].strip().title()

    # Convert credits to integer if possible
    if new_record.get("credits"):
        try:
            new_record["credits"] = int(new_record["credits"])
        except ValueError:
            new_record["credits"] = new_record["credits"]  # leave as string

    return new_record
