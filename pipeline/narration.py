"""Extrait la narration d'un script.md et compte les mots.

La narration = le texte des sections « ## N. Titre », sans les lignes « > VISUEL : »,
sans les sous-titres et sans les tags [Sn]. C'est ce que la voix lira.

Usage :
    python pipeline/narration.py episodes/<slug>/script.md          # comptage
    python pipeline/narration.py episodes/<slug>/script.md --texte  # narration brute
"""

import re
import sys
from pathlib import Path

SECTION = re.compile(r"^##\s+\d+\.\s*")
TAG = re.compile(r"\s*\[S\d+\]")
MOTS_PAR_MINUTE = 150
FOURCHETTE = (1800, 2300)


def sections(script: str) -> list[tuple[str, str]]:
    """Liste de (titre de section, texte de narration)."""
    out: list[tuple[str, str]] = []
    titre, lignes = None, []
    for ligne in script.splitlines():
        if re.match(r"^#{1,2}\s", ligne):
            if titre is not None:
                out.append((titre, " ".join(lignes)))
            titre = SECTION.sub("", ligne).strip() if SECTION.match(ligne) else None
            lignes = []
        elif titre is not None:
            brut = ligne.strip()
            if brut and not brut.startswith((">", "###")):
                lignes.append(TAG.sub("", brut).replace("**", "").strip())
    if titre is not None:
        out.append((titre, " ".join(lignes)))
    return out


def compter_mots(texte: str) -> int:
    return sum(1 for mot in texte.split() if re.search(r"\w", mot))


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    secs = sections(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if "--texte" in sys.argv:
        print("\n\n".join(texte for _, texte in secs))
        return
    total = 0
    for i, (titre, texte) in enumerate(secs, 1):
        n = compter_mots(texte)
        total += n
        print(f"{i:>2}. {titre[:60]:<60} {n:>5} mots  ~{n / MOTS_PAR_MINUTE:4.1f} min")
    ok = FOURCHETTE[0] <= total <= FOURCHETTE[1]
    print(f"TOTAL : {total} mots, ~{total / MOTS_PAR_MINUTE:.1f} min "
          f"({'dans' if ok else 'HORS'} la fourchette {FOURCHETTE[0]}-{FOURCHETTE[1]})")


if __name__ == "__main__":
    main()
