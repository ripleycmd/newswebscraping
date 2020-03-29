import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/') #get request to get this page
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.find())  #'soup' object 
#print(soup.select(.score)) ---> grabs all of the spans scores
links = soup.select('.storylink')
subtext = soup.select('.subtext')
# print(votes[0]) #grabs the link to the story wih the highest vote count
# print(votes[0].get('id'))

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))