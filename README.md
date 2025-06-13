# Subtitle Translation Tool for .ASS Files

This repository contains two Python scripts to support the translation of subtitles from English to Polish in `.ass` subtitle files.

## Scripts

### 1. `text_separator.py`
Extracts all dialogue lines from a `.ass` subtitle file and saves them to a numbered text file `dialogues_en.txt`, which can then be translated manually.

### 2. `text_swap.py`
Replaces the original English dialogue lines in the `.ass` file with translated lines from `dialogues_pl.txt`, and outputs a new subtitle file `napisy_PL.ass`.

## Usage

1. Place your original `.ass` file as `napisy.ass` in the project folder.
2. Run `text_separator.py` to extract dialogues.
3. Translate the lines in `dialogues_en.txt` and save them as `dialogues_pl.txt`.
4. Run `text_swap.py` to generate `napisy_PL.ass` with translated lines.

## Note

- Make sure the number of lines in `dialogues_pl.txt` matches the number of original dialogues.
- The scripts assume UTF-8 encoding.

## License

For personal or educational use only.
