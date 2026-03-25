### Simulador de CarInterface ###

import math
import time

class SimulatorInterface:

    def __init__(self):

        # Simulamos una conexión exitosa y comenzamos a contar el tiempo para generar valores de RPM.
        self.start_time = time.time()
        self.connected = True

    def connect(self):

        # Simulamos un retraso de conexión
        print("Simulando conexión con adaptador ELM327...")
        time.sleep(1)
        return "Connected"


    def get_query(self, command_name):
        
        #Simula la respuesta del comando RPM con una onda senoidal para que los valores suban y bajen .
        
        if command_name == "RPM":

            #elapsed --> Tiempo: cuánto tiempo ha pasado desde que se inició la simulación. 
            elapsed = time.time() - self.start_time

            #Creo una oscilación entre 800 y 4000 RPM

            #base_rpm --> RPM base alrededor del cual oscilará el valor.
            base_rpm = 2400

            #amplitude --> Amplitud de la oscilación: cuánto varían las RPM alrededor del valor base.
            amplitude = 1600

            # math.sin crea el efecto de subir y bajar 
            simulated_value = base_rpm + amplitude * math.sin(elapsed * 0.5)   #  RPM = base + amplitude * sin(tiempo * frecuencia)
            
            # MockResponse simula la respuesta de la consulta OBD-II, con un valor de RPM que varía con el tiempo.
            # Es una clase interna porque solo se usa dentro de este método.
            class MockResponse:

                # val --> Valor simulado de RPM que se le pasa al crear la instancia de MockResponse.
                def __init__(self, val):

                    #value --> Simula el atributo 'value' de la respuesta OBD-II 
                    #tiene un atributo 'magnitude' con el valor numérico de RPM.
                    self.value = type('obj', (object,), {'magnitude': val})()
                    #type('obj', (object,), {'magnitude': val})() crea un objeto con un atributo 'magnitude' 
                    #sin definir una clase completa.

                #Simula el método is_null() de la respuesta OBD-II, simulamos que siempre es válida.
                def is_null(self): return False
            
            #Devuelvo el valor simulado de RPM dentro de un objeto MockResponse. 
            #Uso abs() (valor absoluto) para asegurarnos de que no sea negativo.
            return MockResponse(abs(simulated_value))
        
        return None

    #Simulo que siempre estoy conectada
    def is_connected(self):
        return self.connected

    def close(self):
        self.connected = False