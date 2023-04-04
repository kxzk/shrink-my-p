<h3 align="center">SHRINK MY P (WIP)</h3>

> Essentially, seeing how much we can shrink the prompt without losing meaning.

<br>

1. Replace words with emojis - [Emoji Translate](https://github.com/fabriceyhc/emoji_translate)
2. Replace long words with shorter synonyms - process below

<br>

#### Shorter Synonym Process

* Use [TOP 10k WORDS](https://github.com/kadekillary/shrink-my-p/blob/main/top_10000_words.py) and [Thesaurus API](https://api-ninjas.com/api/thesaurus)
* Filter list to those synonyms with length < original word
* Calculate word similarity using [Spacy](https://www.geeksforgeeks.org/python-word-similarity-using-spacy/)
* Use [Flashtext](https://github.com/vi3k6i5/flashtext) to replace in prompt

<br>

GPT models seem to understand complex meaning from emojis:

<img width="857" alt="Screenshot 2023-04-04 at 10 34 32" src="https://user-images.githubusercontent.com/25046261/229884134-b18a0b0f-496e-4b0f-a439-2fed578a67ec.png">

<br>

#### Links

* [Flashtext (0N) replace algo](https://github.com/vi3k6i5/flashtext)
* [Parrot - paraphrasing](https://github.com/PrithivirajDamodaran/Parrot_Paraphraser)
* [Emojis](https://unicode.org/Public/emoji/latest/emoji-sequences.txt)
* [Emoji Phrases](https://emojicombos.com/Emoji-Phrases)
* [Demoji](https://github.com/bsolomon1124/demoji)
* [Emoji Translate](https://github.com/fabriceyhc/emoji_translate)
* [Word Similarity](https://www.geeksforgeeks.org/python-word-similarity-using-spacy/)
