from bs4 import BeautifulSoup
from tqdm import tqdm
import urllib.request
import re
import csv

def not_relative_uri(href):
	return re.compile('^https://').search(href) is  not  None

url =  'https://www.webdevstudios.org/gen/'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

progress = tqdm(total=len(url), desc="Tiến trình crawling", unit="URL")

div_Baoquanh1 = soup.find('div', class_='overflow-hidden').find_all(
	'div',
	class_='Gen_gen_generation_container__3IT9D',
) # ket qua tra ve danh sach cac the div thoa man voi yeu cau 


# for div in div_Baoquanh1:
#   name = div.select('p[class*="Gen_gen_department__"]')
#   role = div.select('p[class*="Gen_gen_name__2KGRs text-primary]')

with open('data.csv', 'w', newline='', encoding='utf-8') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(['Name', 'Role'])

	# Lặp qua từng phần tử trong container
	for div in div_Baoquanh1:
		
		name_tags = div.select('div > div > div > p.Gen_gen_department__IA-6p')
		role_tags = div.select('div > div > div > p.Gen_gen_name__2KGRs')
  
		for name, role in zip(name_tags, role_tags):
			name_text = name.text.strip() if name else "N/A"
			role_text = role.text.strip() if role else "N/A"
	
			writer.writerow([name_text, role_text])
			progress.total += 1
			progress.refresh()
