# News Headline Sentiment Analysis

A Python project that uses web scraping and Natural Language Processing (NLP) to analyse webpage headings and extract meaningful insights.

## Features

- **Web Scraping:** Extracts H1, H2 and H3 headings using BeautifulSoup.
- **Sentiment Analysis:** Uses TextBlob to classify text as positive, negative or neutral.
- **Keyword Analysis:** Identifies the 10 most frequent keywords after removing English stopwords.
- **Topic Identification:** Uses part-of-speech tagging to identify the 10 most frequent nouns.

## Technologies

- Python
- Requests
- BeautifulSoup
- TextBlob
- NLTK
- Regular Expressions
- Collections (Counter)

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/news-headline-sentiment-analysis.git
cd news-headline-sentiment-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python main.py
```

## Configuration

Change the `url` variable in `main.py` to analyse headings from a different webpage.

The script automatically downloads the required NLTK resources when executed.
