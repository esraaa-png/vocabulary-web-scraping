# Vocabulary Web Scraping System

A Python-based web scraping system that extracts vocabulary data from online dictionary websites and stores it in structured formats for further processing and analysis.

The project collects vocabulary information including meanings, translations, pronunciation, example sentences, images, and audio pronunciation files.

---

## Overview

This project demonstrates practical web scraping and data extraction techniques using Python.

The system automates the process of collecting vocabulary content from dictionary websites, cleaning and organizing the extracted data, then storing it in reusable formats such as JSON and CSV.

The project was designed to simulate real-world data collection workflows including error handling, file management, and structured data storage.

---

## Features

- Web scraping of vocabulary data
- Extract word meanings and translations
- Extract pronunciation information
- Download vocabulary images
- Download audio pronunciation files
- Store extracted data in JSON format
- Export cleaned data to CSV
- Handle missing or inconsistent data
- Structured and reusable scraping workflow

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Programming Language | Python |
| Web Scraping | BeautifulSoup |
| HTTP Requests | Requests |
| Data Storage | JSON / CSV |
| File Handling | Python OS Module |

---

## Project Structure

```bash
vocabulary-web-scraping/
│
├── data/
│   ├── json/
│   ├── csv/
│   ├── images/
│   └── audio/
│
├── project.py
├── requirements.txt
└── README.md
```

---

## Workflow

```text
Dictionary Website
        │
        ▼
Send HTTP Requests
        │
        ▼
Extract HTML Content
        │
        ▼
Parse Data with BeautifulSoup
        │
        ▼
Clean & Validate Data
        │
        ├── Save JSON
        ├── Save CSV
        ├── Download Images
        └── Download Audio Files
```

---

## Extracted Data

The scraper extracts:

- Word
- Meaning
- Translation
- Pronunciation
- Example Sentences
- Image URLs
- Audio Pronunciation Files

---

## Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-link>

cd vocabulary-web-scraping
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the Project

```bash
python project.py
```

---

## Output

The extracted data is automatically saved into:

- JSON files
- CSV files
- Downloaded image folders
- Downloaded audio folders

---

## Error Handling

The project includes handling for:

- Missing vocabulary fields
- Invalid URLs
- Connection errors
- Incomplete HTML elements
- Duplicate entries

---

## Future Improvements

- Multi-threaded scraping
- Database integration
- API-based vocabulary extraction
- Automated scheduling
- Support for multiple dictionary websites
- Data visualization dashboard

---

## Learning Outcomes

This project demonstrates practical experience with:

- Web Scraping
- HTML Parsing
- Data Cleaning
- File Handling
- HTTP Requests
- Structured Data Storage
- Error Handling in Python
- Automation Workflows

---

## Author

**Esraa Abdelazeem**  
Data Engineer | Data Analyst | AI Enthusiast

Passionate about building web scraping systems, automating data extraction workflows, and transforming raw vocabulary data into structured and reusable datasets.
