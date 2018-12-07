""" PySum summarizes a given article """
import sys
import scraper
import preprocess
import nlp


def main():
    """ Main entry point into PySum """
    try:
        inputURL = sys.argv[1]
    except IndexError:
        inputURL = 'https://en.wikipedia.org/wiki/Natural_language_processing'

    rawArticleText = scraper.scrapeArticle(inputURL)
    (articleText, articleTextReduced) = preprocess.cleanAndFormat(rawArticleText)

    print(articleText)
    print('\n')
    print(articleTextReduced)


# --- Tests --- #
def testPySumLoaded():
    return 'PySum Loaded'
