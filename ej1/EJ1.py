notas = {
"perez": [],
"salatic": [],
"almada": [],
"prosppeti": [],
"moyano": []
}
def ver_ntas():
    print("Bienvendo al menu de las notas")
for alu, nlist in notas.items():
    if len(nlist) == 0:
        print(f"no hay notas cargadas {alu.capitalize()}")
else:
        print(f"{alu.capitalize()}: {nlist}")
def ver_por_alumno():
    alu = input("decime el apellido de alumno ")
    if alu in notas:
     if len(notas[alu]) == 0: 
        print(f"No hay ninguna nota cargada {alu.capitalize()}")        
    else:
        print(f"notas de {alu.capitalize()}: {notas[alu]}")
    else:
print("no esta registrado elapellido")
def cargar_notas():
    alu = input("ingresa el apellido que vas a cargar ")
    if alu in notas:
            nlist = []
    print("ingresa las 5 notas ") 
    for i in range(5):
            while True:
                 try: