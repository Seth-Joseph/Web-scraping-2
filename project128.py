import requests
import csv

from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

def scrape():
	headers = ["Name", "Radius", "Mass", "Distance"]
	r = requests.get(URL)
	
	soup = BeautifulSoup(r.text, "html.parser")
	table = soup.find_all("tbody")[7]

	star_data = []

	for tr_tag in table.find_all("tr"):
		td_tags = tr_tag.find_all("td")
		temp_list = []
		
		for index, td_tag in enumerate(td_tags):
			if index == 0:
				if td_tag.find('a') != None:
					a_tag = td_tag.find_all("a")[0]
					temp_list.append(a_tag.text)
				else:
					temp_list.append(td_tag.text)
			elif index == 5 or index == 7 or index == 8:
				try:
					temp_list.append(r'{}'.format(td_tag.contents[-1]))

				except:
					temp_list.append("")

		star_data.append(temp_list)

	return star_data, headers

star_data, headers = scrape()

with open("main.csv", "a", encoding = "utf-8") as file:
	csv_writer = csv.writer(file)
	csv_writer.writerow(headers)
	csv_writer.writerows(star_data)