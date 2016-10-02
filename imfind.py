import urllib
import re
import webbrowser

urll = raw_input('Enter the website : ')
website = urllib.urlopen(urll)
html = website.read()
pat = re.compile('<img src=\".*"')
img = pat.findall(html)
f = open("te.txt","w")
for x in img:
	f.write(urll+x+"\n")
        webbrowser.open(urll+str(x))        
f.close()



#f.close()
#web = 'http://www.shutterstock.com/<img src=^(.*)|([\/|.|\w|\s])*\.[a-z]*\/[a-z]*\_[a-z]*\_[a-z]*\_[a-z]*\/[0-9]*\/[0-9]*\/[a-z]*\-[a-z]*\-[a-z]*\-[a-z]*\-[0-9]*.|(?:jpg|gif|png)"'
#e=[web+x] for x in img
#webbrowser.open(e)
            

