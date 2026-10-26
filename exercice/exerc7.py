NB_ETUDIANTS = 3
 
print("=" * 30)
print("Groupe 01")
print("=" * 30)
total = 0
for i in range(1, NB_ETUDIANTS + 1):
       valide = False
       while not valide:
          try:
              note = float(input(f"Note {i} : "))
              if 0 <= note <= 100:
                  valide = True
              else:
                  print("La note doit être entre 0 et 100.")
          except ValueError:
              print("Ce n'est pas un nombre.")
total += note
print(f"Moyenne : {total / NB_ETUDIANTS:.1f}")

print("=" * 30)
print("Groupe 02")
print("=" * 30)
total = 0
for i in range(1, NB_ETUDIANTS + 1):
      valide = False
      while not valide:
          try:
              note = float(input(f"Note {i} : "))
              if 0 <= note <= 100:
                  valide = True
              else:
                  print("La note doit être entre 0 et 100.")
          except ValueError:
              print("Ce n'est pas un nombre.")
total += note
print(f"Moyenne : {total / NB_ETUDIANTS:.1f}")

print("=" * 30)
print("Groupe 03")  
print("=" * 30)
total = 0
for i in range(1, NB_ETUDIANTS + 1):
      valide = False
      while not valide:
          try:
              note = float(input(f"Note {i} : "))
              if 0 <= note <= 100:
                  valide = True
              else:
                  print("La note doit être entre 0 et 100.")
          except ValueError:
              print("Ce n'est pas un nombre.")
      total += note
print(f"Moyenne : {total / NB_ETUDIANTS:.1f}")