import streamlit as st
import requests
from bs4 import BeautifulSoup

# Define the categories
categories = ["Business", "Finance", "Legal", "Marketing", "Product", "Tech"]

# Create a dictionary to store the scraped resources and tools
resources = {}

# Scrape the website
for category in categories:
  url = f"https://www.founderresources.io/resources/{category}/"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  # Find all the resources and tools on the page
  resources[category] = []
  for resource in soup.find_all("div", class_="resource"):
    title = resource.find("h3").text
    link = resource.find("a", class_="resource-link")["href"]

    resources[category].append({
      "title": title,
      "link": link
    })

# Create a Streamlit page
st.set_page_config(page_title="Founder Resources", page_icon="logo.png")

# Display the title and header
st.title("Founder Resources")
st.header("Welcome to the Founder Resources Platform!")

# Display the resources and tools
for category in categories:
  st.subheader(category)

  for resource in resources[category]:
    st.markdown(f"- [{resource['title']}]({resource['link']})")

# Display the footer
st.markdown("For any questions or assistance, please contact us at info@founderresources.io.")
st.markdown("Made with ❤️ by Founder Resources")
