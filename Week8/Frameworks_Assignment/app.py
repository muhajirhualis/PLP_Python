import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df = df.dropna(subset=['title', 'publish_time'])
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Sidebar filters
years = df['year'].dropna().unique()
year_range = st.slider("Select year range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))

filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Publications by year
st.subheader("Publications by Year")
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
st.pyplot(fig)

# Word cloud
st.subheader("Word Cloud of Titles")
text = " ".join(filtered['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Sample data
st.subheader("Sample Data")
st.dataframe(filtered.head(20))
