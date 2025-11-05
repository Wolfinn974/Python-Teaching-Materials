# 🔁 02 – Loops & Conditions

## 🎯 Objectif du module
Approfondir la logique avec les **boucles** (`for`, `while`) et les **conditions imbriquées**.  
Ces exercices aident à comprendre comment automatiser des actions répétitives et prendre des décisions complexes dans un programme.

---

## 🧠 Rappels de notions vues

| Notion | Description courte | Exemple |
|--------|--------------------|----------|
| `for` | Répète un bloc de code pour chaque élément d’une séquence. | `for i in range(5): print(i)` |
| `while` | Répète tant qu’une condition est vraie. | `while x < 10: x += 1` |
| `break` / `continue` | `break` arrête la boucle / `continue` saute à l’itération suivante. | `if x == 3: break` |
| Conditions imbriquées | Un `if` dans un autre `if`. | `if a > 0: if b > 0: print("OK")` |
| Opérateurs logiques | `and`, `or`, `not` pour combiner plusieurs tests. | `if x > 0 and y > 0:` |

---

## 🧩 Exercices inclus

### 1. `10_first_prime.py`
Afficher les 10 premiers nombres premiers  
> 🧰 Notions : boucles `for`, `while`, modulo `%`, intro aux fonctions.

---

### 2. `guess_number.py`
Faire deviner un nombre aléatoire entre 1 et 100 à l’utilisateur.  
> 🧰 Notions : boucle `while`, conditions, `random.randint()`.

---

### 3. `count_vowels.py`
Compter le nombre de voyelles dans une phrase donné par l’utilisateur.  
> 🧰 Notions : boucles sur une chaîne, conditions, compteurs.

---

### 4. `mystery_word.py`
Faire deviner à l'utilisateur un mot choisi à l'avance.Même principe que guess the number.
> 🧰 Notions : boucles `while`, conditions, listes, random.

---

## 💬 Conseils

- Fais attention aux **conditions infinies** avec `while`.  
- Utilise `break` pour stopper proprement une boucle quand le but est atteint.  
- Teste des variantes : et si la borne change ? si l’utilisateur tape un texte au lieu d’un nombre ?  

---

## 🧾 Auteur
Ces exercices ont été créés pour mes élèves en initiation à Python.  
> Libre d’utilisation et de modification à des fins pédagogiques.  