#!/usr/bin/python

# puts markdown site content into html skeleton

import pystache
from markdown import Markdown
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

with open('site.md', 'r') as site:
    m = Markdown()
    body = m.convert(site.read())
with open('skeleton.html','r') as skeleton:
    with open('index.html', 'w') as site:
        site.write(pystache.render(skeleton.read(), {'body': body}))
