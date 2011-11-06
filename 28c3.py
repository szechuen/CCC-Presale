import requests
from BeautifulSoup import BeautifulSoup
from time import sleep

s = requests.session()

username = ''
password = ''

# SignIn

page1 = s.get("https://presale.events.ccc.de/accounts/sign_in")
soup1 = BeautifulSoup(page1.content)

post2 = {}
for item in soup1.findAll("input", type="hidden"): post2[item['name']] = item['value']
for item in soup1.findAll("input", type="submit"): post2[item['name']] = item['value']
post2['account[username]'] = username
post2['account[password]'] = password

link2 = "https://presale.events.ccc.de" + soup1.find("form")['action']

# Account

page2 = s.post(link2, data=post2)
soup2 = BeautifulSoup(page2.content)

ordered = False
page = page2
soup = soup2

while not ordered:

	post3 = {}
	for item in soup.findAll("input", type="hidden"): post3[item['name']] = item['value']
	for item in soup.findAll("input", type="submit"): post3[item['name']] = item['value']

	link3 = "https://presale.events.ccc.de" + soup.find("form")['action']

	page = s.post(link3, data=post3)
	soup = BeautifulSoup(page.content)

	last = open("last.html", "w")
	last.write(soup.prettify())
	last.close()

	if soup.find(text=lambda(x): x.find("There are currently not enough tickets available") != -1): 
		print "Not Open"
		sleep(1)
	else:
		print "Ordered"
		ordered = True
