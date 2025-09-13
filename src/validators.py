"""
validators.py
--------------
Validation rules for scraped data.
Ensures that required fields exist and are non-empty.
"""

def validate_record(record):
    """
    Validate a single course record.
    Returns True if valid, False otherwise.
    """
    if not record:
        return False

    required_fields = ["code", "title"]

    for field in required_fields:
        if not record.get(field):  # Missing or empty string
            return False

    return True
