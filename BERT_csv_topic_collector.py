import pandas as pd
from bertopic import BERTopic

# CSV Reader
df = pd.read_csv("***FILE***.csv")

# Convert data frame to a list of strings
text_list = df['***Column***'].tolist()

# Create BERTopic instance
bt = BERTopic()

# Get Topic from the text
topics = bt.predict(text_list) #contains the topic extracted from the forum

#Export results to CSV?

df_topics = pd.DataFrame(topics)
df_topics.tocsv(***FILENAME.csv***, index = False)



