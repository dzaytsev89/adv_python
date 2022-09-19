import bs4
import requests
import re
from fake_headers import Headers
from pprint import pprint

header = Headers(browser="chrome", os="win", headers=True)
header = header.generate()
KEYWORDS = ['дизайн', 'фото', 'web', 'python', ]
base_url = 'https://habr.com'
main_url = '/ru/all/'
match_list = {}


def search_word(pattern, *args):
    match = re.search(pattern, str([arg for arg in args]).lower())
    if match is not None:
        return True


def main():
    response = requests.get(base_url+main_url, headers=header)
    text = response.text
    soup = bs4.BeautifulSoup(text, 'html.parser')
    articles = soup.find_all(class_='tm-articles-list__item')
    for article in articles:
        title_data = article.find(class_='tm-article-snippet__title-link').text
        post_url = base_url + article.find(class_='tm-article-snippet__title-link').attrs['href']
        post_data = article.find('time').attrs['title']
        hubs = article.find_all(class_='tm-article-snippet__hubs-item-link')
        hubs = [hub.text.strip().lower() for hub in hubs]
        post_preview = \
            article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-1')
        if post_preview is None:
            post_preview = \
                article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
        post_response = requests.get(post_url, headers=header)
        post_text_soup = post_response.text
        soup_article = bs4.BeautifulSoup(post_text_soup, 'html.parser')
        post_text = \
            soup_article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
        if post_text is None:
            post_text = \
             soup_article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-1')
        post_text.find_next_sibling('p')
        for k in KEYWORDS:
            if search_word(k, title_data, post_preview.text, post_text, *hubs):
                find_match = f'<{post_data}> - <{title_data}> - <{post_url}>'
                match_list[k] = []
                for kk, v in match_list.items():
                    if find_match not in v:  # check for duplicate match
                        v.append(find_match)
                    else:
                        continue

    pprint(match_list)


if __name__ == '__main__':
    main()
