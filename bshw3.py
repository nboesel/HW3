# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions"
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

soup1 = str(soup)
soup2 = soup1.replace("student", "AMAZING student")
soup3 = soup2.replace("https://www.youtube.com/embed/mimp_3gquc4?feature=oembed", "me.jpg")

final_soup = BeautifulSoup(soup3, "html.parser")

for p in final_soup.find_all(class_= "logo"):
	if p.img:
		p.img['src'] = "media/logo.png"
for p1 in final_soup.find_all(class_= "footer-logo"):
	if p1.img:
		p1.img['src'] = "media/logo.png"

f = open("bshw3.html", "w")
f.write (final_soup.prettify())
f.close()













