'''Install and import BeautifulSoup from the bs4 module.
Write a simple program to parse a small HTML string.
Given this HTML:
Extract the title text.
Extract the <h1> text.
Extract the paragraph text.
Write a program to:
Find the first <a> tag.
Print its href attribute.
Use .prettify() to format parsed HTML.
What is the difference between:
find()
find_all()
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
  </body></html>
 '''

from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

# HTML string
html_doc = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1>Welcome</h1>
    <p>This is a paragraph.</p>
    <a href="https://example.com">Click Here</a>
  </body>
</html>
"""

# Parse HTML
soup = BeautifulSoup(html_doc, "html.parser")

# Extract title text
print("Title:", soup.title.text)

# Extract h1 text
print("H1:", soup.h1.text)

# Extract paragraph text
print("Paragraph:", soup.p.text)

# Find first <a> tag
first_link = soup.find("a")

print("First <a> tag:", first_link)
print("Href attribute:", first_link["href"])

# Format HTML using prettify
print("\nFormatted HTML:\n")
print(soup.prettify())


'''
| Feature      | find()             | find_all()        |
| ------------ | ------------------ | ----------------- |
| Returns      | First matching tag | All matching tags |
| Return Type  | Single element     | List of elements  |
| If not found | None               | Empty list []     |

'''





'''
2.Scrape product details from an e-commerce sample page:
Product name
Price
Rating
Availability
Extract all image URLs from a webpage.
 
 '''

#https://books.toscrape.com/

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Find all products
products = soup.find_all("article", class_="product_pod")

for product in products:
    # Product Name
    name = product.h3.a["title"]

    # Price
    price = product.find("p", class_="price_color").text

    # Rating (stored as class name)
    rating = product.find("p", class_="star-rating")["class"][1]

    # Availability
    availability = product.find("p", class_="instock availability").text.strip()
    
    print("Name:", name)
    print("Price:", price)
    print("Rating:", rating)
    print("Availability:", availability)
    print("-" * 50)
