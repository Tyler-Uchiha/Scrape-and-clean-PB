import requests
from bs4 import BeautifulSoup
import pandas as pd

curr_page = 1
data = []

print("Enter start year to scrape :")
x = int(input())
print("Enter end year to scrape :")
y = int(input())


xx = x      #Allows us to output an excel file containing the date range
k = y-x     #Creates loop range end value

#Scrape the site k times
for i in range(k+1):
    
    while x != y:
        
        #Keeps track of the number of pages we are currently scraping
        print("scraping page ", curr_page)
    
        url = "https://www.powerball.net/southafrica/results/history/" + str(x)
        
        page = requests.get(url)
        
        soup = BeautifulSoup(page.text, "html.parser")
        
        all_nums = soup.find_all("div", class_="col-md-4")
        
        #Store individual dictionaries within a list   
        for num in all_nums:
            thing = {}
            
            # Key -> Characters, Value -> RHS code
            thing['Characters'] = num.find("a", class_="archive-box")
            
            data.append(thing)

        curr_page +=1
        x +=1
       
#Exports the list into an excel document       
df = pd.DataFrame(data)
years = "Powerball_" + str(xx) + '_' + str(y) +".xlsx"
df.to_excel(years)