import pandas as pd

df = pd.read_csv("metadata.csv")
print(df.shape)
print(df.info())
df.head()

df.isnull().sum()
df.describe(include='all')


df.isnull().sum()
df.describe(include='all')



df = df.dropna(subset=['title', 'publish_time'])


df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

df['abstract_word_count'] = df['abstract'].astype(str).apply(lambda x: len(x.split()))





import matplotlib.pyplot as plt
import seaborn as sns

year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
sns.barplot(x=year_counts.index, y=year_counts.values)
plt.title("Publications by Year")
plt.show()


top_journals = df['journal'].value_counts().head(10)
sns.barplot(y=top_journals.index, x=top_journals.values)
plt.title("Top 10 Journals Publishing COVID-19 Research")
plt.show()


from wordcloud import WordCloud

text = " ".join(df['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


df['source_x'].value_counts().head(10).plot(kind='bar')
plt.title("Top Sources of Research Papers")
plt.show()

