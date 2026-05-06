# ---------------------------------------------------------
# TP3 - PATRONES DE CREACIÓN (Puntos 2, 3 y 4)
# Facultad de Ciencia y Tecnología - UADER
# ---------------------------------------------------------

from abc import ABC, abstractmethod

# ---------------------------------------------------------
# PUNTO 2 - SINGLETON (CÁLCULO DE IMPUESTOS)
# ---------------------------------------------------------
# Arquitectura: Instancia Única.
# Garantiza que todas las clases utilicen la misma instancia para 
# el cálculo de impuestos sobre la base imponible.

class CalculadoraImpuestos:
    # Atributo de clase para almacenar la instancia única
    _instance = None 

    def __new__(cls):
        # Lógica de control de creación de instancia única
        if cls._instance is None:
            cls._instance = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instance

    def calcular_total(self, base):
        # Cálculo de impuestos según consigna:
        # IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%)
        iva = base * 0.21
        iibb = base * 0.05
        municipal = base * 0.012
        return base + iva + iibb + municipal


# ---------------------------------------------------------
# PUNTO 3 - FACTORY METHOD (HAMBURGUESAS)
# ---------------------------------------------------------
# Arquitectura: Producto Abstracto y Concreto.
# Define una interfaz para instanciar una comida rápida que pueda 
# ser entregada en mostrador o enviada por delivery.

class Hamburguesa(ABC):
    """Producto Abstracto"""
    @abstractmethod
    def entregar(self):
        pass

    def precio_base(self):
        return 1000.0

class HamburguesaMostrador(Hamburguesa):
    """Producto Concreto 1"""
    def entregar(self):
        print("Método de entrega: Mostrador [Punto 3]")

class HamburguesaDelivery(Hamburguesa):
    """Producto Concreto 2"""
    def entregar(self):
        print("Método de entrega: Delivery [Punto 3]")


# ---------------------------------------------------------
# PUNTO 4 - FACTORY METHOD (FACTURACIÓN) 
# ---------------------------------------------------------
# Arquitectura: Separación de tipos de comprobantes.
# Implementa facturas de acuerdo a la condición impositiva 
# del cliente (IVA Responsable o IVA Exento).

class Factura(ABC):
    """Producto Abstracto"""
    @abstractmethod
    def imprimir(self, importe):
        pass

class FacturaResponsable(Factura):
    """Producto Concreto A"""
    def imprimir(self, importe):
        print("Condición: IVA Responsable - Total: $" + str(round(importe, 2)))

class FacturaExento(Factura):
    """Producto Concreto C"""
    def imprimir(self, importe):
        print("Condición: IVA Exento - Total: $" + str(round(importe, 2)))


# ---------------------------------------------------------
# JERARQUÍA DE CREADORES (FACTORY METHOD)
# ---------------------------------------------------------
# Arquitectura de Fábricas: Define el método de fabricación 
# para desacoplar la creación de la lógica de negocio.

class Creador(ABC):
    @abstractmethod
    def crear(self):
        """Factory Method"""
        pass

class CreadorDelivery(Creador):
    def crear(self):
        return HamburguesaDelivery()

class CreadorFacturaResponsable(Creador):
    def crear(self):
        return FacturaResponsable()


# ---------------------------------------------------------
# FLUJO DE LLAMADOS DEL SISTEMA
# ---------------------------------------------------------

if __name__ == "__main__":
    # Implementación Punto 3 (Instanciación de Hamburguesa)
    fabrica_comida = CreadorDelivery()
    pedido = fabrica_comida.crear()
    pedido.entregar()

    # Implementación Punto 2 (Uso de instancia única de cálculo)
    motor_fiscal = CalculadoraImpuestos()
    monto_final = motor_fiscal.calcular_total(pedido.precio_base())

    # Implementación Punto 4 (Generación de Factura según condición)
    fabrica_fiscal = CreadorFacturaResponsable()
    comprobante = fabrica_fiscal.crear()
    comprobante.imprimir(monto_final)