import re as regex

def cleanAndFormat(articleText):
    articleTextReduced = _reduceToAlpha(articleText)
    return (articleText, articleTextReduced)

    
def _reduceToAlpha(text): return regex.sub(r'\s+', ' ', regex.sub('[^a-zA-Z]', ' ', text))
