#! /usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.content

def balance_parens(text, stack):
    s = stack.copy()
    for char in text:
        if char == '(':
            s.append(char)
        elif char == ')' and len(s) > 0 and s[-1] == '(':
            s.pop()
    return s

def find_link_in_p(p):
    def is_text_element(el):
        return not child.name

    def is_outside_parens(stack):
        return len(stack) == 0

    stack = []

    for child in p.children:
        if is_text_element(child):
            stack = balance_parens(child, stack)
        elif child.name == 'a' and is_outside_parens(stack):
            return child.get('href')

    return None

def find_first_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.find_all(class_='mw-parser-output')[0]
    paragraphs = body.find_all('p')
    for p in paragraphs:
        link = find_link_in_p(p)
        if link:
            return link
    return None

def make_next_url(orig_url, path):
    prefix = '/'.join(orig_url.split('/')[0:3])
    return prefix + path

def get_next_url(url):
    html = get_html(url)
    link = find_first_link(html)
    next_url = make_next_url(url, link)
    return next_url

def is_philosophy(url):
    return url.endswith('/wiki/Philosophy')

def find_philosophy(start_url):
    crawls = 0
    url = start_url
    chain = [url]
    while True:
        if is_philosophy(url):
            return chain
        elif crawls > 99:
            return 'cycle'
        else:
            url = get_next_url(url)
            chain.append(url)
            crawls += 1

def main():
    url = sys.argv[1]
    chain = find_philosophy(url)
    print(chain)


if __name__ == '__main__':
    main()
