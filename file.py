import requests
from bs4 import BeautifulSoup
import csv

page  = requests.get('https://github.com/trending')
soup = BeautifulSoup(page.text , 'html.parser')
#repo = soup.find(class_="Box")
repo_list = soup.find_all(class_='Box-row')
print(len(repo_list))

file_name = "github_trending_today.csv"
f = csv.writer(open(file_name,'w',newline=''))
f.writerow(['Developer', 'Repo Name' , 'Number of Stars'])
for repo in repo_list:
	# Developer Name # Repository name 
	full_repo_name = repo.find(class_='h3 lh-condensed').text.split('/')
	developer = full_repo_name[0].strip()
	repoName  = full_repo_name[1].strip() 
	#Count of stars 	
	star_count = repo.find(class_='octicon octicon-star').parent.text
	stars = star_count.strip()
	print("D.N. - " + developer + "    Repo N. - " + repoName + "    stars - " + stars)
	print("\n")
	f.writerow([developer, repoName , stars])

