liste_notes = [[10,10,10],[20,20,30],[40,40,10],[50,60,100]]
liste_examens = ["quiz 1","quiz 2","quiz 3"]
liste_eleves = ["david","Benoit","George","Mortimer"]

for eleve in liste_eleves:
    for note in eleve:
        print(note)




for i in range(len(liste_notes)):
    print(f"notes pour eleves:{liste_eleves[i]}")
    for j in range(len(liste_notes[i])):
        print(f"Examen: {liste_examens[j]}")
        print(f"Notes :{liste_notes[i][j]}")
