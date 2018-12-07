import nltk
import heapq
import math

def summarize(rawText, reducedText, percentReduction):
    maxSentLen = 30

    sentenceList = _extractSentences(rawText)
    wordFreqTable = _createWordFrequencyTable(reducedText)
    weightedFreqTable = _weightFrequencyTable(wordFreqTable)
    sentenceScores = _getSentenceScores(sentenceList, weightedFreqTable, maxSentLen)
    summary = _assembleSummary(sentenceScores, percentReduction)

    return summary




def _extractSentences(rawText):
    sentenceList = nltk.sent_tokenize(rawText)
    return sentenceList

def _createWordFrequencyTable(reducedText):
    stopwords = nltk.corpus.stopwords.words('english')
    wordFrequencies = {}
    for word in nltk.word_tokenize(reducedText):
        if word not in stopwords:
            if word not in wordFrequencies.keys():
                wordFrequencies[word] = 1
            else:
                wordFrequencies[word] += 1

    return wordFrequencies

def _weightFrequencyTable(freqTable):
    maxFrequency = max(freqTable.values())
    weightedFreqTable = {}

    for word in freqTable.keys():
        weightedFreqTable[word] = (freqTable[word]/maxFrequency)

    return weightedFreqTable


def _getSentenceScores(sentenceList, weightedFreqTable, maxSentLen):
    sentenceScores = {}
    for sentence in sentenceList:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in weightedFreqTable.keys():
                if len(sentence.split(' ')) < maxSentLen:
                    if sentence not in sentenceScores.keys():
                        sentenceScores[sentence] = weightedFreqTable[word]
                    else:
                        sentenceScores[sentence] += weightedFreqTable[word]
    return sentenceScores


def _assembleSummary(sentenceScores, percentReduction):
    numOfSentences = math.floor(float(percentReduction / 100) * len(sentenceScores))
    print('Number of sentences: %d \n' % numOfSentences)


    summarySentences = heapq.nlargest(numOfSentences, sentenceScores, key=sentenceScores.get)
    summary = ' '.join(summarySentences)

    return summary
