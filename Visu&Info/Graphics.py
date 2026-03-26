### Generador de gráficos para las RPM ###

# Biblioteca para gráficos
import matplotlib.pyplot as plt

#Biblioteca para anmaciones en tiempo real
import matplotlib.animation as animation

#Grafico en función del tiempo  y las RPM
def rpm_graph(time, rpm):
    plt.figure(figsize=(12, 6))

    #marker --> Puntos para cada valor
    plt.plot(time, rpm, label='RPM', color='pink', linewidth=2, marker='*', markersize=4)
    plt.title('RPM en función del Tiempo', fontsize=16, fontweight='bold')
    plt.xlabel('Tiempo (s)', fontsize=12)
    plt.ylabel('RPM', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=11)

    #Limites dinámicos
    plt.tight_layout()
    plt.show()

#Grafico en tiemmpo real
def rpm_graph_animated(time_list, rpm_list):

    #fig --> Figura donde va el grafico
    #ax --> ejes del grafico
    fig, ax = plt.subplots(figsize=(12, 6))
    
    #Actualización
    def animate(frame):
        ax.clear()

        #time_list --> Lista de tiempos
        #rpm_list --> Lista de RPM
        if len(time_list) > 0:
            ax.plot(time_list[:frame+1], rpm_list[:frame+1], 'b-', linewidth=2, marker='o', markersize=4)
        
        ax.set_title('RMP en función del tiempo actualmente', fontsize=16, fontweight='bold')
        ax.set_xlabel('Tiempo (s)', fontsize=12)
        ax.set_ylabel('RPM', fontsize=12)
        ax.grid(True, alpha=0.3)

        
        if len(rpm_list) > 0:
            #set_ylim --> Ajusta el límite del eje Y para que se adapte a los datos de RPM, 
            #con un margen del 10% por encima del valor máximo.
            ax.set_ylim(0, max(rpm_list) * 1.1 if max(rpm_list) > 0 else 100)
        ax.set_xlim(0, max(time_list) if len(time_list) > 0 else 1)
    
    #ani --> Animación que actualiza el gráfico en tiempo real, con ticks cada 100ms.
    ani = animation.FuncAnimation(fig, animate, frames=len(time_list), repeat=False, interval=100)
    
    #Ajuste de diseño para evitar solapamientos
    plt.tight_layout()
    return fig, ani