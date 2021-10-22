#La funcion imprime el listado de Alumnos
def lista_alumnos(Alumnos):  
  print(f"NOMBRE  \t EDAD \t E-MAIL")
  for i in range(len(Alumnos[0-1])):
    print(f"{Alumnos[0][i]} \t {Alumnos[1][i]} \t {Alumnos[2][i]}")

#La funcion imprime el listado de materias
def lista_materias(Materias):  
  print(f"MATERIAS")
  for i in Materias:
    print(i) #imprime las materias una abajo de la otra

#La funcion permite agregar a un nuevo alumno
def agregar_alumno(Alumnos):
    try:
        while True:
            nuevo_alumno = input("Por favor, ingrese el nombre completo del nuevo alumno: ")
            if nuevo_alumno not in Alumnos:
                Alumnos[0].append(nuevo_alumno) #agrega el alumno ya que su nombre no esta registrado en el sistema
                break
            else:
                print("Por favor ingrese un nuevo alumno.")
        while True:
            edad_nuevo_alumno = int(input("Por favor, ingrese la edad del nuevo alumno: "))
            if (edad_nuevo_alumno >= 10) and (edad_nuevo_alumno <= 18):
                Alumnos[1].append(edad_nuevo_alumno) #agrega la edad ya que es mayor de 10 y menor de 18
                break
            else:
                print("La edad del alumno debe ser entre 10 y 18 años")
        while True:
            mail_nuevo_alumno = input("Por favor, ingrese el mail del nuevo alumno: ")
            if "@" in mail_nuevo_alumno:
                Alumnos[2].append(mail_nuevo_alumno) #agrega ya que hay arroba en el mail
                break
            else:
                print("El mail debe contener un @.")
    except:
        print("ERROR.")
    print(f"{Alumnos}")
    return Alumnos

#La funcion editará la edad de un alumnos
def editar_edad(Alumnos):
    while True:
        try:
            indicar_alumno = input("Ingrese el nombre de alumno al que desee cambiarle la edad: ")
            edad_nueva = int(input("Por favor, ingrese la edad del nuevo alumno: "))
            if (edad_nueva >= 10) and (edad_nueva <= 18): #verifica si el rango de edad se respeta
                if indicar_alumno in Alumnos[0]: #busca si el alumno esta en el sistema
                    Alumnos[1][Alumnos[0].index(indicar_alumno)]= edad_nueva #reemplaza por la nueva nueva edad ya que el alumno esta en el sistema y respeta el min y max de edad
                    print(f"La nueva edad de {indicar_alumno} es {Alumnos[1][Alumnos[0].index(indicar_alumno)]}")
                    break
                else:
                    print("Este alumno no esta registrado en la base de datos.")
            else:
                print("La edad del alumno debe ser entre 10 y 18 años")
        except:
            print("ERROR.")
    return Alumnos

#La función agrega materias
def agregar_materias(Materias):
    while True:
        try:
            nueva_materia = input("Por favor, ingrese una nueva materia: ")
            if nueva_materia not in Materias:
                Materias.append(nueva_materia) #agrega la materia ya que no esta en la base de datos
                print(f"{Materias}")
                break
            else:
                print("Esta materia ya se encuentra registrada. Por favor ingrese una nueva.")
        except:
            print("ERROR.")
    return Materias


