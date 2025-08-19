import streamlit as st
from scraper import get_product_details

st.title("🛒 Amazon Product Scraper")

# Input field
urls_input = st.text_area("Enter Amazon product URLs (comma-separated):")

# Button to trigger scraping
if st.button("Scrape"):
    st.write("Scraping started...")
    st.write("URLs entered:", urls_input)
    
    urls = [url.strip() for url in urls_input.split(",") if url.strip()]
    if urls:
        st.write("### 🔍 Scraping Results:")
        for i, url in enumerate(urls, start=1):
            with st.spinner(f"Scraping product {i}..."):
                result = get_product_details(url)
                st.write(f"**Product {i}**")
                st.write(f"**Title:** {result['title']}")
                st.write(f"**Price:** {result['price']}")
                st.write(f"[🔗 View on Amazon]({result['product_url']})")
                st.write("---")
    else:
        st.warning("Please enter at least one valid URL.")
