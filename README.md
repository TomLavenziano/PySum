# PySum

PySum is a text summarization system specifically tuned for summarizing online articles

### Summarization Steps:
1. Associate words with their grammatical counterparts. (e.g. "city" and "cities")
2. Calculate the occurrence of each word in the text.
3. Assign each word with points depending on their popularity.
4. Detect which periods represent the end of a sentence. (e.g "Mr." does not).
5. Split up the text into individual sentences.
6. Rank sentences by the sum of their words' points.
7. Return X of the most highly ranked sentences in chronological order.
