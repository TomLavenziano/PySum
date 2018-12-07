import context
import pysum
import scraper

import unittest

class BasicTestSuite(unittest.TestCase):
    def testPySumLoaded(self):
        self.assertEqual(pysum.testPySumLoaded(), 'PySum Loaded')

    def testScraper(self):
        self.assertEqual(scraper.testScraperLoaded(), 'Scraped')

if __name__ == "__main__":
    # execute only if run as the entry point into the program
    unittest.main()
