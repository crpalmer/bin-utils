#!/usr/bin/python3

import sys
import json
from html.parser import HTMLParser
import textwrap

class HTMLFilter(HTMLParser):
    text = ""
    p = ""

    def handle_data(self, data):
        self.p += data

    def handle_starttag(self, tag, attrs):
        if tag == "p" or tag == "h2":
            self.collect()
        if tag == "h2":
            self.p += " *** "

    def handle_endtag(self, tag):
        if tag == "h2":
            self.p += " *** "
        if tag == "p" or tag == "h2":
            self.collect()

    def collect(self):
        self.p = self.p.strip()
        if len(self.p) > 0:
            self.text += textwrap.fill(f.p, width = 80)
            self.text += '\n\n'
            self.p = ""

    def get_text(self):
        return text + textwrap.fill(f.p, width = 80)

data = json.load(sys.stdin)
for article in data['articles']:
  print(article['title'])

  if 'pubDate' in article:
    print(article['pubDate'], end='')
    if 'contentModified' in article:
      print(" (modified " + article['contentModified'] + ")")

  print()

  f = HTMLFilter()
  f.feed(article['body'])
  print(f.text)
