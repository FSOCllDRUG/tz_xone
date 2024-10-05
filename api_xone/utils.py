import requests
from bs4 import BeautifulSoup


def fetch_link_metadata(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('meta', property='og:title') or soup.find('title')
    description = soup.find('meta', attrs={'property': 'og:description'}) or soup.find('meta',
                                                                                       attrs={'name': 'description'})
    image = soup.find('meta', property='og:image')
    link_type = soup.find('meta', property='og:type')

    music_tags = soup.find_all(
        lambda tag: tag.has_attr('class') and any(word in tag['class'] for word in ['music', 'album', 'song']))
    music_tags += soup.find_all(
        lambda tag: tag.has_attr('id') and any(word in tag['id'] for word in ['music', 'album', 'song']))

    if music_tags:
        link_type = 'music'
    elif link_type:
        link_type = link_type['content']
    else:
        link_type = 'website'

    return {
        'title': title.get('content', '') if title else '',
        'description': description.get('content', '') if description else '',
        'image': image['content'] if image else '',
        'link_type': link_type,
    }
