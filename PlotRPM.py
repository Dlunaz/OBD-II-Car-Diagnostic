    ### Script para mostrar gráfico ###

import time
from SimulatorInterface import SimulatorInterface
from RPMReader import RPMReader
from Graphics import rpm_graph

#Recopilo datos durando 30s y luego genero el gráfico
def plot_rpm_data(duration=30):
    #-------- SIMULADOR -------- 
    sim_car = SimulatorInterface()  #car= CarInterface()
    sim_car.connect()
    
    
    #Empiezo usando el RPMReader del simulador 
    reader = RPMReader(sim_car)
    
    time_list = []
    rpm_list = []
    start_time = time.time()
    
    print(f"\n--- RECOPILANDO DATOS DE RPM ({duration} segundos) ---")
    print(" Presiona Ctrl+C para detener\n")
    
    try:
        while True:
            #elapsed_time --> Tiempo transcurrido desde el inicio de la recopilación de datos.
            elapsed_time = time.time() - start_time
            
            if elapsed_time > duration:
                print(f"\n✓ Recopilación completada en {duration} segundos")
                break
            
            rpm = reader.get_current_rpm()
            time_list.append(elapsed_time)
            rpm_list.append(rpm)
            
            # Barra de progreso
            progress = int((elapsed_time / duration) * 40)
            bar = "█" * progress + "-" * (40 - progress)
            print(f"[{bar}] {elapsed_time:.1f}s | RPM: {rpm:>5} ", end="\r")
            
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        print(f"\n\n✓ Recopilación detenida")
    
    finally:
        sim_car.close()
    
    # Mostrar gráfico si se recopilaron datos
    if len(time_list) > 0:
        print(f"\nMostrando gráfico con {len(time_list)} puntos de datos...")
        rpm_graph(time_list, rpm_list)
    else:
        print("No se recopilaron datos.")

if __name__ == "__main__":
    # Ejecuto por 30 segundos 
    plot_rpm_data(duration=40)


