url = "https://www.xstt5.com/renwen/9462/{}.html"
beg_idx = 533543
end_idx = 533581
output_file = "说话的艺术.txt"
import re
import urllib.request
import bs4
import lxml

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html=html.decode("utf-8")
    html = bs4.BeautifulSoup(html,"lxml")
    title = html.find("h1").text
    content = html.find("div",{"class":"zw"}).find_all("p")
    content = [p.text for p in content]
    return title,content
with open(output_file,"w",encoding="utf-8") as f:
    for idx in range(beg_idx,end_idx+1):
        url_idx = url.format(idx)
        title,content=getHtml(url_idx)
        f.write(title+"\n")
        for line in content:
            f.write(line)
            f.write("\n")
