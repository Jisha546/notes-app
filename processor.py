from typing import List, Dict, Tuple

PHARMA_KEYWORDS = [
    "pharma", "pharmaceutical", "biotech", "biotechnology", "inc", "llc", "ltd",
    "gsk", "pfizer", "novartis", "roche", "merck", "sanofi", "astrazeneca"
]

ACADEMIC_KEYWORDS = [
    "university", "institute", "college", "hospital", "research center", "lab", "laboratory"
]

def is_non_academic_affiliation(affiliation: str) -> bool:
    affiliation_lower = affiliation.lower()
    return not any(kw in affiliation_lower for kw in ACADEMIC_KEYWORDS)

def is_pharma_company(affiliation: str) -> bool:
    affiliation_lower = affiliation.lower()
    return any(kw in affiliation_lower for kw in PHARMA_KEYWORDS)

def extract_non_academic_authors(authors: List[Dict]) -> Tuple[List[str], List[str]]:
    non_academic_authors = []
    pharma_companies = set()

    for author in authors:
        name = author.get("name", "")
        affiliations = author.get("affiliations", [])
        non_acad = False
        pharma_found = False
        for aff in affiliations:
            if is_non_academic_affiliation(aff):
                non_acad = True
            if is_pharma_company(aff):
                pharma_found = True
                pharma_companies.add(aff)
        if non_acad:
            non_academic_authors.append(name)
    return non_academic_authors, list(pharma_companies)
