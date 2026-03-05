# metodo_push.py
# Método Push: se produce según el pronostico, antes de conocer la demanda real.

# Inventario inicial
inventario = 10

# Pronóstico de demanda para 5 dias
pronostico = [25, 30, 20, 35, 25]

# Demanda real
demanda_real = [30, 25, 40, 30, 20]

# Produccion planeada (Push) = pronostico
produccion = pronostico.copy()

print("Dia | Inv. inicial | Pronostico | Produccion | Inv. tras prod. | Demanda real | Atendida | Faltante | Inv. final")
print("---------------------------------------------------------------------------------------------------------------")

for dia in range(5):
    inv_inicial = inventario

    # 1) Se produce primero (Push)
    inventario += produccion[dia]
    inv_tras_prod = inventario

    # 2) Llega la demanda real
    demanda = demanda_real[dia]

    # 3) Se atiende lo que se pueda con el inventario disponible
    atendida = min(inventario, demanda)
    inventario -= atendida

    faltante = demanda - atendida  # si es > 0, no se pudo cubrir toda la demanda
    inv_final = inventario

    print(
        f"{dia+1:>3} | {inv_inicial:>11} | {pronostico[dia]:>10} | {produccion[dia]:>10} | {inv_tras_prod:>13} |"
        f" {demanda:>11} | {atendida:>7} | {faltante:>8} | {inv_final:>9}"
    )

    