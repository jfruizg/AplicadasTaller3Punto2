import threading
import pruebaA
import PruebaC
import pruebaFI
import prueba4
import prueba5



if __name__ == '__main__':
    prueba1 = threading.Thread(target=pruebaA.prueba)
    prueba2 = threading.Thread(target=PruebaC.prueba)
    prueba3 = threading.Thread(target=pruebaFI.prueba)
    prueba4 = threading.Thread(target=prueba4.prueba)
    prueba5 = threading.Thread(target=prueba5.prueba)
    prueba1.start()
    prueba2.start()
    prueba3.start()
    prueba4.start()
    prueba5.start()



