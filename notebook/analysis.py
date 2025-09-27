import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("../data/metadata.csv")

# Explore
print(df.shape)
print(df.info())
print(df.isnull().sum())

# Clean
df = df.dropna(subset=["title", "publish_time"])
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# Analysis: Publications by year
year_counts = df["year"].value_counts().sort_index()
year_counts.plot(kind="bar", title="Publications by Year")
plt.show()

# Top journals
top_journals = df["journal"].value_counts().head(10)
top_journals.plot(kind="barh", title="Top Journals")
plt.show()

# Word cloud
text = " ".join(df["title"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
