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

    try:
        percentReduction = int(sys.argv[2])
    except IndexError:
        percentReduction = 40


    rawArticleText = scraper.scrapeArticle(inputURL)
    (articleText, articleTextReduced) = preprocess.cleanAndFormat(rawArticleText)

    articleSummary = nlp.summarize(articleText, articleTextReduced, percentReduction)


    print(articleText)
    print('\n')
    # print(articleTextReduced)
    print('\n')
    print('| ----------------------------------------------- |')
    print('|                 Article Summary                 |')
    print('| ----------------------------------------------- |')
    print('|                  Reduced to %d%%                 |' % percentReduction)
    print('| ----------------------------------------------- |')
    print('\n')
    print(articleSummary)



# --- Tests --- #
def testPySumLoaded():
    return 'PySum Loaded'
