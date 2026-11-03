from pathlib import Path

messy = Path("messy"); messy.mkdir(exist_ok=True)

for fname in ["a.jpg", "b.png", "c.pdf", "d.doc", "e.txt", "f.zip"]:
    (messy / fname).touch()