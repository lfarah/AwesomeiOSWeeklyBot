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

ghGist = Simplegist(username= 'lfarah', api_token= '')

def getGist(index):
    lastGist = ghGist.profile().listall()[index]
    if "AwesomeiOSWeekly" not in lastGist:
        print lastGist
        return getGist(index + 1)
    else :
        return lastGist

lastGist = getGist(0)
mainContent = ghGist.search('lfarah').content(name=lastGist)
announcements = mainContent.split("#### Announcements")[1].split("Links of the week")[0]
links = mainContent.split("Links of the week")[1].split("Wanna see your library here")[0]
libraries = mainContent.split("Here are the **5 awesome libraries of the week**:")[1]
markdowner = Markdown()
announcementsHTML = markdowner.convert(announcements)
linksHTML = markdowner.convert(links)
librariesHTML = markdowner.convert(libraries)
libNumber = re.findall(r'\d+', lastGist)[0]
header = "<h1 id=\"awesomeiosweekly" + libNumber  + "\">AwesomeiOS.Weekly [" + libNumber + "]</h1><p> </p><p> </p><p> </p><h4 id=\"announcements\">Announcements</h4>"
footer = "That's all for this week! Please <a href=\"mailto:lucas.farah@me.com?Subject=Hello%20again\" target=\"_top\">give us feedback</a> and <a href=\"https://twitter.com/intent/tweet?text=AwesomeiOS%20weekly%20" + libNumber + "%20is%20out!%20http://bit.ly/2lJvy0P\" target=\"_top\">share on Twitter</a></h5></html>"

with open('header.html','r') as headerFile:
    # header = headerFile.read() + announcementsHTML
    header = headerFile.read()
    with open('links.html','r') as linksFile:
        links = linksFile.read() + linksHTML
        header += links
        with open('libraries.html','r') as librariesFile:
            libraries = librariesFile.read() + librariesHTML
            print libraries
            header += libraries
            with open('footer.html','r') as footerFile:
                footer = footerFile.read()
                header += footer
                with open('output.html','w') as output:
                    output.write(header)
                    output.close()
                    headerFile.close()
                    linksFile.close()
                    librariesFile.close()