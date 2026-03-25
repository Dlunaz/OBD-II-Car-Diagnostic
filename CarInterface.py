### Habla con el coche usando el adaptador ELM327 ###

#Libreria OBD-II para Python
import obd

class CarInterface:

    #Self --> Referencia al objeto actual (como .this)
    #Port --> Puerto del adaptador ELM327 (ej: 'COM3' en Windows o '/dev/ttyUSB0' en Linux)
    def __init__(self, port=None):

        #Si port es None, la librería busca el USB automáticamente.

        self.port = port            #Puerto del adaptador ELM327
        self.connection = None      #Objeto de conexión OBD-II (inicialmente None)


    #Intenta conectar al coche usando el puerto especificado.
    def connect(self):

        # Intentamos conectar. 'fast=False' es más lento pero más estable.
        # Si la conexión es exitosa, 'self.connection' será un objeto OBD. Si falla, seguirá siendo None.
        #fast --> Desactiva el modo rápido de conexión, lo que puede mejorar la estabilidad en algunos casos.
                #el modo rapido es sirve para acelerar la conexión, pero puede dar problemas con algunos adaptadores o vehículo.
        self.connection = obd.OBD(self.port, fast=False)

        #true sise estableció la conexión.
        return self.connection.status()

    
    #command_name --> Nombre del comando OBD-II a consultar (ej: 'RPM', 'SPEED', 'COOLANT_TEMP', etc.)
    def get_query(self, command_name):

        #Verificamos que tengamos conexión
        if self.connection and self.connection.is_connected():

            #getattr --> Permite obtener un atributo de un objeto por su nombre como string.
            cmd = getattr(obd.commands, command_name)

            #Query --> Ejecuta el comando OBD-II y devuelve la respuesta. 
            response = self.connection.query(cmd)
            return response
        return None


    #Cierra la conexión con el coche.
    def close(self):
        if self.connection:
            self.connection.close()