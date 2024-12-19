import random


zimejumi = [
    '''
     -----
     |   |
         |
         |
         |
         |
    -----''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    -----''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    -----''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    -----''',
    '''
     -----
     |   |
     O   |
    /|\  |
         |
         |
    -----''',
    '''
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    -----''',
    '''
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    -----'''
]

vardi = ['janis', 'programesana', 'cola', 'jazz', 'novembris']

vards = random.choice(vardi)
minetais_vards = ['_'] * len(vards)
minejumi = set()
meginajumi = 6 

print("Karatavu spele")
print("megini uzminet vardu. Katru reizi, kad neuzminesi pareizi, klusi tuvak zaudet un diemzel liksim tev pakarties >:).")

while meginajumi > 0:
    print("n" + zimejumi[6 - meginajumi]) 
    print("Vards: " + ' '.join(minetais_vards))  
    print("Ievadiet burtu:")
    
    minejums = input().lower()

    if minejums in minejumi:
        print("Jus jau minejat sito vardu -_-.")
        continue
    
    minejumi.add(minejums)
    
    if minejums in vards:
        print(f"Pareizs burts: {minejums}")
        for i in range(len(vards)):
            if vards[i] == minejums:
                minetais_vards[i] = minejums
    else:
        print(f"Nepareizs burts: {minejums}")
        meginajumi -= 1

    if '_' not in minetais_vards:
        print("wow, nu jums paveicas soreiz! Vards ir:", vards)
        break
else:
    print("nu ko, sodien laime nespideja, ATA >:). Vards bija:", vards)