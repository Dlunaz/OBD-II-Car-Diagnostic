### Simulador a main ###

import time
from SimulatorInterface import SimulatorInterface
from RPMReader import RPMReader

def run_simulation():
    
    sim_car = SimulatorInterface()
    sim_car.connect()

    reader = RPMReader(sim_car)

    print("\n--- INICIANDO SIMULACIÓN ---")
    print(" Ctrl+C para detener\n")

    try:
        while True:
            rpm = reader.get_current_rpm()
            status = reader.get_status_message(rpm)
            
            # Barra de progreso para la terminal
            bar_length = int(rpm / 200)                                 #200 RPM por cada bloque de la barra
            
            bar = "█" * bar_length + "-" * (35 - bar_length)            # Barra de 35 caracteres de longitud total
            
            print(f"[{bar}] {rpm:>4} RPM | {status}      ", end="\r")   
            
            time.sleep(0.1)                                             # Actualización
            
    except KeyboardInterrupt:
        print("\n\nSimulacion detenida.")
    finally:
        sim_car.close()

if __name__ == "__main__":
    run_simulation()