import hashlib

alfabeto = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
claveCifrada = "a911c42c9b290bfe6a28f153165d7a82641486a5"

class prueba():
    for p1 in range(24, 52):
        if (alfabeto[p1].isupper() == True):
            for p2 in range(0, 52):
                if (alfabeto[p2].isupper() == False):
                    for p3 in range(0, 52):
                        if (alfabeto[p3].isupper() == True):
                            for p4 in range(0, 52):
                                if (alfabeto[p4].isupper() == False):
                                    for p5 in range(0, 52):
                                        if (alfabeto[p5].isupper() == True):
                                            for p6 in range(0, 52):
                                                if (alfabeto[p6].isupper() == True):
                                                    for p7 in range(0, 52):
                                                        cadena = alfabeto[p1] + alfabeto[p2] + alfabeto[p3] + alfabeto[
                                                            p4] + \
                                                                 alfabeto[
                                                                     p5] + \
                                                                 alfabeto[p6] + alfabeto[p7]
                                                        if (cadena.isupper()):
                                                            break
                                                        for p8 in range(0, 52):
                                                            cadena = alfabeto[p1] + alfabeto[p2] + alfabeto[p3] + \
                                                                     alfabeto[
                                                                         p4] + \
                                                                     alfabeto[
                                                                         p5] + \
                                                                     alfabeto[p6] + alfabeto[p7] + alfabeto[p8]
                                                            if (cadena.isupper()):
                                                                break
                                                            clave = cadena.encode('utf-8')
                                                            resultado = hashlib.sha1(clave).hexdigest()
                                                            print(cadena, ":", resultado)
                                                            if (resultado == claveCifrada):
                                                                print("Eureka!!!!")
