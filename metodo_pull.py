# Metodo Pull - Produccion bajo demanda

class SistemaPull:

    def __init__(self):
        self.inventario = 10  # inventario inicial cambiado a 10

    def recibir_pedido(self, cantidad):
        print(f"\nCliente solicita {cantidad} productos.")

        if cantidad <= self.inventario:
            print("Hay suficiente inventario. Entregando pedido...")
            self.inventario -= cantidad
        else:
            falta = cantidad - self.inventario
            print(f"No hay suficiente inventario. Faltan {falta} unidades.")
            print("Produciendo lo necesario...")
            self.producir(falta)
            self.inventario -= cantidad

        print(f"Pedido entregado. Inventario actual: {self.inventario}")

    def producir(self, cantidad):
        print(f"Fabricando {cantidad} unidades...")
        self.inventario += cantidad
        print("Produccion completada.")


# Simulacion del sistema Pull
sistema = SistemaPull()

sistema.recibir_pedido(1)
sistema.recibir_pedido(3)
sistema.recibir_pedido(2)