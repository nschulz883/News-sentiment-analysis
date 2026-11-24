

# libraries needed 
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from nltk.corpus import stopwords
from collections import Counter
import re
import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')


#fetches data news headlines and joins them together
#for sentiment analysis

#url can be changed to any news outlet of your choice
url = "https://realpython.com/python-datetime/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text,'html.parser')
    headlines  = [h.get_text() for h in soup.find_all(['h1','h2','h3'])]  
    news_text = " ".join(headlines)
else:
    print("Request failed:",response.status_code)     
    quit()

#sentiment analysis
blob = TextBlob(news_text)
sentiment_score = blob.sentiment.polarity
if sentiment_score > 0:
    sentiment_label = "Positive"

elif sentiment_score < 0:
    sentiment_label = "Negative"
else:
    sentiment_label = "Neutral"
    
#key word frequency and removing words like the is a it etc     
words = re.findall(r'\b\w+\b', news_text.lower())
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in words if w not in stop_words]
keyword_freq = Counter(filtered_words).most_common(10)


#topic searching
nouns = [word for word, pos in blob.tags if pos.startswith('NN')]
topics = Counter(nouns).most_common(10)         

#print out results

#print sentiment
print("\n Sentiment Analysis")
print(f"Polarity: {sentiment_score}, Label: {sentiment_label}")

print("\n Topics")
for topic, count in topics:
    print(f"{topic}:{count}")

print("\n Keywords")  
for keyword, freq in keyword_freq:
    print(f"{keyword}:{freq}")
