import re

# Wczytaj zawartość pliku z dialogami (tu jako tekst)
with open("napisy.ass", "r", encoding="utf-8") as file:
    lines = file.readlines()

dialogues = []
for line in lines:
    if line.startswith("Dialogue:"):
        # Wyciągamy czysty tekst z końca linii (po ostatnim przecinku)
        parts = line.strip().split(",", 9)
        if len(parts) == 10:
            text = parts[-1]
            dialogues.append(text)

# Zapisz każdy dialog z numerem
with open("dialogues_en.txt", "w", encoding="utf-8") as f:
    for idx, dialogue in enumerate(dialogues, 1):
        f.write(f"{idx}. {dialogue}\n")
