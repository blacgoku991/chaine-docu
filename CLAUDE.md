# Projet : chaîne YouTube « documentaires business » pilotée par agents IA

## Objectif
Chaîne YouTube FR de documentaires business & tech (« l'ascension / la chute / le secret de [entreprise] »), vidéos de 12 à 15 min, produites par une équipe d'agents IA et publiées après validation humaine. L'anglais passe par le doublage automatique de YouTube (même chaîne).

## Règles non négociables
1. **0 € de coûts** en plus de l'abonnement Claude : uniquement des outils gratuits / open source. Ne jamais définir `ANTHROPIC_API_KEY` (sinon facturation API) : tout passe par l'abonnement.
2. **Qualité > volume** : 2 vidéos par semaine maximum. YouTube démonétise ou supprime les chaînes « inauthentiques » (production de masse, scripts sur template, voix de synthèse sur images génériques). Chaque épisode a une vraie recherche, un angle propre et une structure différente des précédents.
3. **Tout est sourcé** : chaque fait ou chiffre a une URL dans `sources.md`. Aucune accusation non sourcée sur une personne ou une entreprise (risque de diffamation).
4. **Visuels** : interdit = extraits TV / news / films / clips (Content ID) et images IA réalistes de personnes réelles. Autorisé = graphiques, cartes et frises générés en code, stock libre de droits avec licence commerciale, illustrations non réalistes.
5. **Pas de conseil financier** (jamais « achetez », « investissez »). On raconte des histoires d'entreprises, on ne conseille pas.
6. **Aucune publication sans validation humaine.**

## Agents (`.claude/agents/`)
| Agent | Rôle | Sortie |
|---|---|---|
| `producteur` (maître) | Orchestre le pipeline, contrôle qualité final, notifie sur Telegram | `state/episodes.json` |
| `veille` | Propose des sujets à demande prouvée, sans doublon avec les épisodes existants | `state/backlog.md` |
| `recherche` | Faits, chiffres, chronologie, sources | `research.md`, `sources.md` |
| `scenariste` | Script 12-15 min : accroche, arc narratif, rebondissements | `script.md` |
| `fact-check` | Vérifie chaque affirmation contre les sources, rejette le non-sourcé et le « déjà vu » (compare la structure aux 5 derniers épisodes) | `review.md` (OK/KO + corrections) |
| `voix` | Narration FR avec Kokoro | `audio/` |
| `visuels` | Graphiques / cartes / frises en Python, stock libre | `visuals/`, `shotlist.json` |
| `montage` | Assemblage FFmpeg + sous-titres | `final.mp4`, `subs.srt` |
| `packaging` | Titre, description (avec sources), chapitres, miniature | `metadata.json`, `thumbnail.png` |
| `publication` | Upload YouTube en privé + notification Telegram | lien YouTube Studio |
| `analyste` | Stats YouTube → apprentissages pour la veille | `insights.md` |

Le producteur ne passe à l'étape suivante que si `review.md` = OK. Deux allers-retours max avec le scénariste, sinon il signale le blocage.

## Stack (gratuite)
- Orchestration : Claude Code + sous-agents. Exécution planifiée : routine Claude Code (cloud Anthropic, incluse dans l'abonnement, fonction en preview).
- Python 3.11+, FFmpeg, MoviePy, matplotlib.
- Voix : Kokoro (Apache 2.0, voix FR, usage commercial autorisé).
- YouTube Data API v3 (quota gratuit), Telegram Bot API.
- Secrets : credentials de l'environnement de la routine ou variables d'environnement. Jamais dans le repo.

## Publication et validation
- Flux cible : la routine produit l'épisode → upload sur YouTube **en privé** avec titre, description, chapitres, miniature → message Telegram avec le lien → l'utilisateur vérifie et passe la vidéo en public dans YouTube Studio (c'est ça, la validation). Pour refuser : il répond sur Telegram avec ses corrections, la run suivante les lit et relance l'épisode.
- ⚠️ Tant que le projet Google Cloud n'a pas passé l'audit de l'API YouTube, les vidéos uploadées par API restent bloquées en privé. Demander l'audit dès le début (formulaire + CGU + politique de confidentialité, quelques semaines). En attendant : « kit d'upload » (mp4 + metadata + miniature) envoyé à l'utilisateur, qui uploade à la main.
- ⚠️ OAuth Google : un écran de consentement en mode « Testing » donne un refresh token qui expire au bout de 7 jours. Le passer en production.
- Déclarer le contenu synthétique à l'upload quand c'est pertinent (case prévue par YouTube). Activer le doublage automatique.

## Routines
- `production` : lundi et jeudi, à une minute décalée (ex. 9:07) pour éviter les retards de l'heure pile.
- `analyste` : une fois par semaine.
- Environnement réseau **Custom** : seulement les domaines nécessaires (Google / YouTube, Telegram, Hugging Face pour les poids Kokoro) + liste par défaut des gestionnaires de paquets. Setup script : installe FFmpeg, les dépendances Python et télécharge Kokoro (résultat mis en cache).
- Les fichiers texte des épisodes sont commités. Les médias lourds (`*.mp4`, `*.wav`) sont dans `.gitignore`.
- Si le rendu vidéo est trop lourd dans le cloud : déplacer l'étape montage sur une machine perso, le reste ne change pas.

## Structure
```
.claude/agents/    sous-agents
pipeline/          tts.py, charts.py, render.py, upload.py, telegram.py
episodes/<slug>/   research.md, sources.md, script.md, review.md, metadata.json
state/             backlog.md, episodes.json
insights.md
```

## Étapes
1. **[EN COURS]** Créer les sous-agents + épisode pilote « Comment Free a cassé le marché du mobile » jusqu'au script validé par le fact-check. L'utilisateur juge la qualité avant la suite.
2. Voix Kokoro + rendu local du pilote → l'utilisateur juge le rendu.
3. Bot Telegram (notifications + lecture des retours).
4. Projet Google Cloud, OAuth YouTube, demande d'audit API.
5. Routine Claude Code planifiée.
6. Agent analyste + boucle d'amélioration.

## Style de travail
Français informel, direct. Une étape courte à la fois, pas de sur-ingénierie. Chaque étape se termine par un livrable testable.
