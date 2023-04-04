#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from emoji_translate.emoji_translate import Translator

    emo = Translator(exact_match_only=False, randomize=True)

    # read csv file and process each line
    P_COUNT = 0
    with open("prompts.csv", "r") as f:
        for line in f:
            if P_COUNT == 100:
                exit()
            line = line.strip()
            line_emoji = emo.emojify(line)
            print(
                f"PC (og): {len(line)}\tPC (emoji): {len(line_emoji)}\tPC (-): {len(line) - len(line_emoji)}"
            )
            P_COUNT += 1
