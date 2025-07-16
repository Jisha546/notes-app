from typing import List, Dict, Any
import requests
import logging
from xml.etree import ElementTree as ET

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(query: str, max_results: int = 100) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    response = requests.get(BASE_URL + "esearch.fcgi", params=params)
    response.raise_for_status()
    data = response.json()
    ids = data.get("esearchresult", {}).get("idlist", [])
    logging.debug(f"Found {len(ids)} papers for query '{query}'")
    return ids

def fetch_details(pubmed_ids: List[str]) -> List[Dict[str, Any]]:
    if not pubmed_ids:
        return []
    ids_str = ",".join(pubmed_ids)
    params = {
        "db": "pubmed",
        "id": ids_str,
        "retmode": "xml"
    }
    response = requests.get(BASE_URL + "efetch.fcgi", params=params)
    response.raise_for_status()
    root = ET.fromstring(response.text)
    articles = []
    for article in root.findall(".//PubmedArticle"):
        pmid_el = article.find(".//PMID")
        pmid = pmid_el.text if pmid_el is not None else ""

        title_el = article.find(".//ArticleTitle")
        title = title_el.text if title_el is not None else ""

        date_el = article.find(".//PubDate")
        pub_date = ""
        if date_el is not None:
            year_el = date_el.find("Year")
            medline_date_el = date_el.find("MedlineDate")
            if year_el is not None:
                pub_date = year_el.text
            elif medline_date_el is not None:
                pub_date = medline_date_el.text

        authors = []
        for author in article.findall(".//Author"):
            last_name_el = author.find("LastName")
            first_name_el = author.find("ForeName")
            name = ""
            if last_name_el is not None and first_name_el is not None:
                name = f"{first_name_el.text} {last_name_el.text}"
            elif last_name_el is not None:
                name = last_name_el.text
            affiliations = []
            for aff in author.findall(".//AffiliationInfo/Affiliation"):
                affiliations.append(aff.text if aff.text else "")
            # Extract email if present
            email = None
            if author.find(".//Email") is not None:
                email = author.find(".//Email").text
            authors.append({
                "name": name,
                "affiliations": affiliations,
                "email": email
            })

        # Corresponding author email heuristic: take email of first author with email
        corresponding_email = ""
        for a in authors:
            if a.get("email"):
                corresponding_email = a["email"]
                break

        articles.append({
            "pmid": pmid,
            "title": title,
            "pub_date": pub_date,
            "authors": authors,
            "corresponding_email": corresponding_email
        })
    return articles
