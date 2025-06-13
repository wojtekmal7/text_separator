with open("dialogues_pl.txt", "r", encoding="utf-8") as f:
    pl_dialogues = [line.strip().split(". ", 1)[1] for line in f.readlines()]

# Otwórz oryginalny plik i podmień teksty
with open("napisy.ass", "r", encoding="utf-8") as f:
    original_lines = f.readlines()

translated_lines = []
dialogue_idx = 0
for line in original_lines:
    if line.startswith("Dialogue:") and dialogue_idx < len(pl_dialogues):
        parts = line.strip().split(",", 9)
        if len(parts) == 10:
            parts[9] = pl_dialogues[dialogue_idx]
            translated_lines.append(",".join(parts) + "\n")
            dialogue_idx += 1
        else:
            translated_lines.append(line)
    else:
        translated_lines.append(line)

# Zapisz do nowego pliku
with open("napisy_PL.ass", "w", encoding="utf-8") as f:
    f.writelines(translated_lines)
