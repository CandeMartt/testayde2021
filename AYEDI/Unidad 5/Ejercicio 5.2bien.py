def es_palindromo():
    palabra_original = input("Ingrese una palabra original: ")
    if not palabra_original.isalpha():
        print("La palabra no es correcta.")
    else:
        palabra_original_lista = list(palabra_original)
        palabra_reversa = palabra_original_lista.copy()
        palabra_reversa.reverse()
        if palabra_original_lista == palabra_reversa:
            print("OK! Es una palabra capicua")
        else:
            print("ERROR! No es una palabra capicua")

es_palindromo()