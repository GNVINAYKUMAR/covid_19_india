from bs4 import BeautifulSoup
import requests
f1=open("covid_data.txt","w").close()
f=open("covid_data.txt","a")
url="https://www.grainmart.in/news/covid-19-coronavirus-india-state-and-district-wise-tally/"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")
#print(soup)
list2=soup.find_all("div",attrs={"class":"skgm-td"})
for list1 in list2:
    if(list1.string==None):
        #print(list1)
        f.write(list1.contents[1].contents[1])
        f.write("\n")
        #print(list1.contents[1].contents[1])
    
    else:
        f.write(list1.string.strip())
        f.write("\n")
        #print(list1.string.strip())
f.write('end')
f.close()