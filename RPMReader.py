### Lee y procesa las RPM ###

class RPMReader:

    #interface --> Instancia de CarInterface para comunicarse con el coche.
    def __init__(self, interface):
        self.interface = interface

    def get_current_rpm(self):

        #Consulta el comando 'RPM' al coche usando la interfaz y procesa la respuesta.
        response = self.interface.get_query("RPM")
        
        if response and not response.is_null():

            # .magnitude devuelve el entero de rpm
            return int(response.value.magnitude)
        return 0

    def get_status_message(self, rpm):
        if rpm > 5000:
            return "RPM por encima de 5000"
        elif rpm > 3000:
            return "RPM por encima de 3000"
        elif rpm > 1000:
            return "RPM por encima de 1000"
        elif rpm > 0:
            return "Motor encendido"
        return "Motor apagado o sin datos"
