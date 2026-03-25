import time
from CarInterface import CarInterface
from RPMReader import RPMReader

def main():
    
    #Guardo la instancia de CarInterface para comunicarme con el coche. 
    car = CarInterface()
    print("Buscando adaptador USB...")
    
    if car.connect() == "Not Connected":       
        print("Error: No se realizó la conexión con el coche. Revisar el USB.")
        return

    #Conexión realizada

    #Guardo la instancia de RPMReader para leer las RPM del coche. Recibe la interface car.
    reader = RPMReader(car)
    print("Conectado con éxito. Leyendo RPM ...")

    #Bucle para leer las RPM hasta que se interrumpa el programa (Ctrl+C)
    #try --> Intenta ejecutar el bloque de código, y si ocurre una excepción (KeyboardInterrupt), se maneja en except.
    try:

        #Mientras se pueda leer
        while True:    
            rpm = reader.get_current_rpm()
            msg = reader.get_status_message(rpm)
            
            # El \r permite que la línea se sobrescriba en la terminal
            print(f"RPM: {rpm} | Estado: {msg}          ", end="\r")
            
            time.sleep(0.5) # Pausa de medio segundo para no saturar el bus
    
    #Ctrl+C
    except KeyboardInterrupt:
        print("\nFinalizando programa...")

    #Cierra conexión    
    finally:
        car.close()

# El bloque if __name__ == "__main__": asegura que main() solo se ejecute si este archivo es el programa principal, 
# y no si se importa como módulo en otro script.
if __name__ == "__main__":
    main()