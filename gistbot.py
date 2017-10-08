import json
from pprint import pprint
import requests
from simplegist import Simplegist
import re
from markdown2 import Markdown
# encoding=utf8
import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

ghGist = Simplegist(username= os.environ['GITHUB_USER'], api_token= os.environ['GITHUB_TOKEN'])

def getGist(index):
    lastGist = ghGist.profile().listall()[index]
    if "AwesomeiOSWeekly" not in lastGist:
        print lastGist
        return getGist(index + 1)
    else :
        return lastGist

lastGist = getGist(0)
readmeMD = ghGist.search('lfarah').content(name=lastGist).split("#### Announcements")[1]
markdowner = Markdown()
main = markdowner.convert(readmeMD)
libNumber = re.findall(r'\d+', lastGist)[0]
header = "<h1 id=\"awesomeiosweekly" + libNumber  + "\">AwesomeiOS.Weekly [" + libNumber + "]</h1><p> </p><p> </p><p> </p><h4 id=\"announcements\">Announcements</h4>"
footer = "That's all for this week! Please <a href=\"mailto:lucas.farah@me.com?Subject=Hello%20again\" target=\"_top\">give us feedback</a> and <a href=\"https://twitter.com/intent/tweet?text=AwesomeiOS%20weekly%20" + libNumber + "%20is%20out!%20http://bit.ly/2lJvy0P\" target=\"_top\">share on Twitter</a></h5></html>"

with open('newsletterCSS.txt','r') as cssFile:
    css = cssFile.read() + "<html>"

    with open('output.txt','w') as output:
        output.write(css + header + main + footer)
        output.close()