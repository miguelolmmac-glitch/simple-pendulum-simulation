#Simple pendulum

import matplotlib.pyplot as plt
import sys
import math

#No consideramos el rozamiento del aire, por tanto, la energía mecánica total se conserva.
#theta_0_grad es el angulo inicial en grados cuando t=0.
#El tiempo t que meto en el argumento de la terminal es el tiempo final.
#La funcion theta_t_calculator me calcula el ángulo en el instante t.

def main():
    t = check_argv()
    m, l, g, theta_0_grad = input("Dame la masa, la longitud, la gravedad y el ángulo del péndulo: ").split(" ")

    try:
        m, l, g, theta_0_grad = map(float,(m, l, g, theta_0_grad))
    except ValueError:
        sys.exit("Error de valores asignados")

    if not 0 < theta_0_grad < 90:
        sys.exit("Valor de ángulo inválido")

    vel_ang = vel_ang_calculator(theta_0_grad, g, l, t)
    vel_lin = vel_lin_calculator(l, vel_ang)
    period = period_calculator(l, g)
    E_cin = E_cin_calculator(m, vel_lin)
    E_pot = E_pot_calculator(m, g, l, theta_0_grad)

    print(f"La velocidad angular en t es: {vel_ang}")
    print(f"La velocidad lineal en t es: {vel_lin}")
    print(f"El periodo del péndulo es: {period}")
    print(f"La energía cinética del péndulo es: {E_cin}")
    print(f"La energía potencial del péndulo es: {E_pot}")

    plot_energies(m, l, g, theta_0_grad, t)

def check_argv():
    if len(sys.argv) != 2:
        sys.exit("Te falta el tiempo o has puesto cosas de más o de menos")
    try:
        t = float(sys.argv[1])
        if not t > 0:
            sys.exit("Error de valor asignado")
        return t
    except ValueError:
        sys.exit("Error de valor asignado")

def vel_ang_calculator(theta_0, g, l, t):
    theta_0_rad = math.radians(theta_0)
    w = -theta_0_rad * math.sqrt(g/l) * math.sin(math.sqrt(g/l) * t)
    return w

def vel_lin_calculator(l, w):
    v = l * w
    return v

def period_calculator(l, g):
    T = 2 * math.pi * math.sqrt(l/g)
    return T

def E_cin_calculator(m, v):
    E_cin = 1/2 * m * v**2
    return E_cin

def E_pot_calculator(m, g, l, theta_0_grad):
    theta_0_rad = math.radians(theta_0_grad)
    E_pot = m * g * l * (1 - math.cos(theta_0_rad))
    return E_pot

def theta_t_calculator(theta_0_grad, g, l, t):
    theta_0_rad = math.radians(theta_0_grad)
    theta_rad = theta_0_rad * math.cos(math.sqrt(g / l) * t)
    return math.degrees(theta_rad)

def plot_energies(m, l, g, theta_0_grad, t):
    times = []
    E_potencial = []
    E_cinetica = []

    salto = 0.01
    tiempo = 0

    while tiempo <= t:
        w = vel_ang_calculator(theta_0_grad, g, l, tiempo)
        v = vel_lin_calculator(l, w)
        theta_actual = theta_t_calculator(theta_0_grad, g, l, tiempo)
        #Este theta es el que depende del tiempo que vaya transcurriendo

        times.append(tiempo)
        E_potencial.append(E_cin_calculator(m, v))
        E_cinetica.append(E_pot_calculator(m, g, l, theta_actual))

        tiempo += salto

    fig, (ax1, ax2) = plt.subplots(2, 1)


    ax1.plot(times, E_cinetica, color="green")
    ax1.set_title("Energía Cinética vs Tiempo")
    ax1.set_xlabel("Tiempo (s)")
    ax1.set_ylabel("Energía (J)")

    ax2.plot(times, E_potencial, color="orange")
    ax2.set_title("Energía Potencial vs Tiempo")
    ax2.set_xlabel("Tiempo (s)")
    ax2.set_ylabel("Energía (J)")

    plt.tight_layout() #Para ajustar los márgenes y los espacios de la figura
    plt.savefig("graficas_pendulo.png")  # <-- Guarda la imagen directamente
    plt.close()



if __name__ == "__main__":
    main()
