import requests
from bs4 import BeautifulSoup
import pprint

n = int(input("How many pages do you want to scan today (1-17): "))

page_list = list(range(1,n+1))

output = []

for i in page_list:
    res = requests.get("https://news.ycombinator.com/news?p=" + str(i))
    

    soup = BeautifulSoup(res.text, 'html.parser')

    links = soup.select('.titleline')
    subtext = soup.select('.subtext')

    def sort_stories_by_votes(hnlist):
        return sorted(hnlist, key = lambda k:k['votes'], reverse=True)

    # print(links)

    def create_custom_hn(links, subtext):
        hn = []
        for idx, item in enumerate(links):
            title = item.getText()
            # each titleline contains an <a> tag; grab its href attribute
            link_tag = item.find('a')
            href = None
            if link_tag:
                href = link_tag.get('href')
                # some links are relative; prepend base URL
                if href and href.startswith('item?'):
                    href = f"https://news.ycombinator.com/{href}"
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({ 'link' : href, 'title': title, 'votes': points})
        return sort_stories_by_votes(hn)
    output.extend(create_custom_hn(links, subtext))

pprint.pprint(output, width=150, indent= 2)

