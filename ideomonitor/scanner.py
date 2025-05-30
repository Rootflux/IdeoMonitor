import re

# Patterns for scanning — modular, practical, and editable.
PATTERNS = [
    r"\binternal use only\b",
    r"\bdo not distribute\b",
    r"\bproprietary\b",
    r"\bconfidential\b",
    r"\bauthorization\b",
]

def scan_file(file_path, patterns=PATTERNS):
    """
    Scans the given text file for specified regex patterns.
    Returns a list of dicts: {'line': int, 'pattern': str, 'context': str}
    """
    results = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            for pat in patterns:
                if re.search(pat, line, re.IGNORECASE):
                    results.append({
                        'line': i,
                        'pattern': pat,
                        'context': line.strip()
                    })
    return results
