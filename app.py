import streamlit as st
import requests
from datetime import datetime

# Streamlit Secrets에서 API 키 가져오기
api_key = st.secrets["newsapi"]["api_key"]
query = 'AI Coding'
url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'

def get_news():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error('Failed to fetch news')
        return None

st.title('Real-time News on AI Coding')
st.markdown("### Click on the news title to read the full article")

news_data = get_news()
if news_data:
    articles = news_data['articles']
    articles.reverse()  # Reverse the order to display from bottom to top

    for article in articles:
        title = article['title']
        url = article['url']
        published_at = datetime.strptime(article['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
        published_at_str = published_at.strftime('%Y-%m-%d %H:%M:%S')

        st.markdown(f"#### [{title}]({url})")
        st.caption(f"Published at: {published_at_str}")

if st.button('Refresh'):
    st.experimental_rerun()
