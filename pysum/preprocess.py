import re as regex

def cleanAndFormat(text):
    articleText = _stripWikiBrackets(articleExtractedText) if 'wikipedia' in url else articleExtractedText
    articleTextReduced = _reduceToAlpha(articleText)

    return (articleText, articleTextReduced)



def _stripWikiBrackets(text): return regex.sub(r'\s+', ' ', regex.sub(r'\[[0-9]*\]', ' ', text))

def _reduceToAlpha(text): return regex.sub(r'\s+', ' ', regex.sub('[^a-zA-Z]', ' ', text))
