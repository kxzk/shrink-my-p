<h3 align="center">SHRINK MY P (WIP)</h3>

> Essentially, seeing how much we can shrink the prompt without losing meaning.

<br>

~~1. Replace words with emojis - [Emoji Translate](https://github.com/fabriceyhc/emoji_translate)~~

2. Replace long words with shorter synonyms - process below

<br>

#### Shorter Synonym Process

* Use [TOP 10k WORDS](https://github.com/kadekillary/shrink-my-p/blob/main/top_10000_words.py) and [Thesaurus API](https://api-ninjas.com/api/thesaurus)
* Filter list to those synonyms with length < original word
* Calculate word similarity using [Spacy](https://www.geeksforgeeks.org/python-word-similarity-using-spacy/)
* Use [Flashtext](https://github.com/vi3k6i5/flashtext) to replace in prompt

<br>

#### Usage

```
# basic example
pip3 install -r requirements

python3 shrink_my_p.py

# will need to further validate actual translation with
# no meaning being lost
```

<br>

#### Links

* [Flashtext (0N) replace algo](https://github.com/vi3k6i5/flashtext)
* [Parrot - paraphrasing](https://github.com/PrithivirajDamodaran/Parrot_Paraphraser)
* [Word Similarity](https://www.geeksforgeeks.org/python-word-similarity-using-spacy/)
