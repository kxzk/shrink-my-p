#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from top_10000_words import TOP_10000_WORDS

if __name__ == "__main__":
    import requests

    for word in TOP_10000_WORDS:
        api_url = f"https://api.api-ninjas.com/v1/thesaurus?word={word}"
        response = requests.get(api_url, headers={"X-Api-Key": ""})
        if response.status_code != requests.codes.ok:
            print(response.text)

        res_j = response.json()
        word_len = len(res_j["word"])
        if len(res_j["synonyms"]) > 0:
            for syn in res_j["synonyms"]:
                if len(syn) < word_len:
                    print(f"{word}, {syn}")
