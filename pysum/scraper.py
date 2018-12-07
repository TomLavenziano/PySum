import bs4 as soup
import urllib.request
import re

def scrapeArticle(url):
    url = _verifyURL(url)
    print('Article URL: ' + url + '\n\n')

    articleHTML = _getRawHTML(url)

    extractedText = _extractTextFromHTML(articleHTML)
    sanitizedText = _stripWikiBrackets(extractedText) if 'wikipedia' in url else extractedText

    return sanitizedText




### Utilities ###

def _verifyURL(url): return url if 'http' in url else 'http://' + url

def _stripWikiBrackets(text): return re.sub(r'\s+', ' ', re.sub(r'\[[0-9]*\]', ' ', text))



### HTML processing ###

def _getRawHTML(url):
    rawReqData = urllib.request.urlopen(url)
    rawHTML = soup.BeautifulSoup(rawReqData.read(), 'lxml')
    return rawHTML

def _extractTextFromHTML(html):
    extractedText = ""
    extractedParagraphs = html.find_all('p')
    extractedText = ''.join([p.text for p in extractedParagraphs])
    return extractedText


### Tests ###

def testScraperLoaded():
    return 'Scraped'
