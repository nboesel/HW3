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


import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = "https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions"
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, "html.parser")

soup1 = str(soup)
soup2 = soup1.replace("student", "AMAZING student")
soup3 = soup2.replace("https://www.youtube.com/embed/mimp_3gquc4?feature=oembed", "me.jpg")
soup4 = soup3.replace(/sites/default/themes/umsi/imgs/logo.png")

final_spup = BeautifulSoup(soup4, "html.parser")


f = open("bshw3.html", "w")
f.write (final_soup.prettify())
f.close()


# for line in soup.find_all("ul", {'class':"menu"}):
# 	if "students" in (line.a.string):
# 		line.a.string = line.a.string.replace("students", "AMAZING students")

# for line in soup.find_all(class = "fi"):
# 	try:
# 		if "student" in line.string:
# 			line.string = line.string.replace("student", "AMAZING student")
# 	except:
# 		pass
	
# for line in soup.find_all('h3'):
# 	if "student" in line.string:
# 		print (line)










