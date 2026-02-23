import requests
from bs4 import BeautifulSoup

# Sample HTML
html = """
<html>
<head>
<title>My Page</title>
</head>
<body>

<h1>Welcome</h1>
<h2>First H2</h2>
<h2>Second H2</h2>

<p>This is a paragraph.</p>
<p>This is another paragraph.</p>

<a href="https://google.com">Google</a>
<a href="https://yahoo.com">Yahoo</a>

<p>This is <b>bold</b> text example.</p>

<table border="1">
<tr>
<th>Name</th>
<th>Age</th>
</tr>
<tr>
<td>Ankit</td>
<td>23</td>
</tr>
</table>

<img src="image1.jpg" alt="Image1">
<img src="image2.png" alt="Image2">

</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print("\n1. Title:", soup.title.text)
print("1. H1:", soup.h1.text)

print("\n2) All Paragraphs:")
for p in soup.find_all("p"):
    print(p.text)

print("\n3. All Links and Count:")
links = soup.find_all("a")
print("Total Links:", len(links))
for link in links:
    print(link.text, "->", link.get("href"))

print("\n4. Extract Attributes of First Link:")
first_link = soup.find("a")
print("Href:", first_link.get("href"))
print("Text:", first_link.text)

print("\n5. First H2:", soup.find("h2").text)

print("\n6. Bold Text:")
for b in soup.find_all("b"):
    print(b.text)

print("\n7. All href Values:")
for link in soup.find_all("a"):
    print(link.get("href"))

print("\n8. All Text Without Tags:")
print(soup.get_text())

print("\n9. Extract Title from Website (example.com):")
import certifi
response = requests.get("https://example.com", verify=certifi.where())
web_soup = BeautifulSoup(response.content, "html.parser")
print("Website Title:", web_soup.title.text)

print("\n10. All Headings (h1–h6):")
for i in range(1, 7):
    for heading in soup.find_all(f"h{i}"):
        print(f"h{i}:", heading.text)

print("\n11. Table Data:")
for row in soup.find_all("tr"):
    cols = row.find_all(["td", "th"])
    for col in cols:
        print(col.text, end=" ")
    print()

print("\n12. Image Sources:")
for img in soup.find_all("img"):
    print(img.get("src"))
