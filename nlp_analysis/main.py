import pandas as pd
import gzip
from textblob import TextBlob
import re

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

# df = getDF('reviews_Amazon_Instant_Video_5.json.gz')


# df = df.rename(columns={'reviewTime': "reviewDate",
#                 "overall": "rating",
#                 "reviewText": "comment"})

# print(df.info())

# x = df['comment'][0]

# print(TextBlob(x).sentiment)

# print(TextBlob("not great, really bad").sentiment[0])

# df['sentiment_score'] = df['comment'].apply(lambda x: TextBlob(x).sentiment[0])

# df.to_csv("reviews.csv")

df = pd.read_csv("/home/chase/projects/python_class/python_class_examples/nlp_analysis/reviews.csv")

df.sort_values(by="sentiment_score")

print(df[["comment", "sentiment_score"]])

def get_word_count(comment):
    comment = comment.strip().lower()
    comment = re.sub("[^a-z\s]", "")
    comment = re.sub("[ ]{2:}", " ")
    comment = comment.strip()

    if(comment == ""): 
      return 0
    
    return comment.count(" ") + 1

df['word_count'] = df['comment'].apply(get_word_count)

print(df[df["word_count"] <=5])