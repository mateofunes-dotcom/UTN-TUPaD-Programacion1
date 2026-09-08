#Diseño, Implementación y Arquitectura Modular de Funciones
#Programación 1 / POO Nivel: Intermedio - Avanzado 
#Modalidad: Individual / Duplas

#Ejercicio 1: Funciones puras con parámetros opcionales y keyword arguments. CONCEPTO: PARÁMETROS
"""Contexto: En un sistema de e-commerce, el cálculo de facturación requiere aplicar impuestos, descuentos y recargos opcionales sin duplicar código
ni forzar al cliente a pasar todos los argumentos siempre.
Consigna Implementá la función calcular_factura_final siguiendo exactamente la firma y comportamiento especificados:

def calcular_factura_final(monto_base: float, impuesto: float = 21.0, descuento: float = 0.0, envio_prioritario: float | None = None) -> float:
#Retorna el importe total final procesado.

Requerimientos Técnicos:
Calcular primero el monto con descuento: monto_base * (1 - descuento / 100)
Aplicar el impuesto sobre el monto descontado: subtotal * (1 + impuesto /100).
Si envio_prioritario no es None, sumar dicho valor fijo al total obtenido.
Retornar el valor númerico redondeado a 2 decimales.
PRUEBAS OBLIGATORIAS A EJECUTAR:
1. calcular_factura_final (1000.0) -> Esperado: 1210.0
2. calcular_factura_final (1000.0, descuento= 10.0) -> Esperado: 1089.0
3. calcular_factura_final (1000.0, impuesto = 10.0, descuento = 5.0, envio_prioritario = 150.0) -> Esperado: 1195.0"""

print("#################################### Actividad 1 ####################################")

def calcular_factura_final(monto_base: float, impuesto: float = 21.0, descuento:
float = 0.0, envio_prioritario: float | None = None) -> float:
    #Calcular primero el monto con descuento: monto_base * (1 - descuento / 100)
    monto_con_descuento = monto_base * (1 - descuento / 100)

    #Aplicar el impuesto sobre el monto descontado: subtotal * (1 + impuesto /100)
    subtotal = monto_con_descuento * (1 + impuesto /100)

    #Si envio_prioritario no es None, sumar dicho valor fijo al total obtenido.
    if envio_prioritario is not None:
        total = subtotal + envio_prioritario
    else:
        total = subtotal

    return round(total, 2)

print(calcular_factura_final(1000.0))
print(calcular_factura_final(1000.0, descuento=10.0))
print(calcular_factura_final(1000.0, impuesto=10.0, descuento=5.0, envio_prioritario=150.0))

#Ejercicio 2: Métodos Estáticos (@staticmethod) como Librería de utilidades
"""Concepto:
@Staticmethod
Contexto: En aplicaciones financieras es conveniente agrupar validaciones y
conversiones matemáticas en clases de utilidad sin necesidad de instanciar objetos
repetidamente en memoria.
Consigna: Diseña la clase ValidadorFinanciero que funcione exclusivamente como un
contenedor estático.

Requerimientos Técnicos:
La clase no debe poseer método __init__.
Implementar @staticmethod es_cuit_valido(cuit: str) -> bool: Verifica que el string
contenga exactamente 11 dígitos numéricos (usar isdigit() y validación de longitud).
Implementar @staticmethod convertir_moneda(monto: float, tasa_cambio: float,
comision: float = 0.02) -> float: Convierte el monto multiplicándolo por la tasa y
descontando el porcentaje de comisión indicado.

class ValidadorFinanciero: @staticmethod def es_cuit_valido(cuit: str) -> bool:
# Lógica de validación pass

PRUEBAS OBLIGATORIAS (SIN INSTANCIAR CON `()`):
print(ValidadorFinanciero.es_cuit_valido("20384920194")) → True
print(ValidadorFinanciero.es_cuit_valido("20-38492019-4")) → False
print(ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05)) →
95000.0"""

print("#################################### Actividad 2 ####################################")

class ValidadorFinanciero: 

    @staticmethod 
    def es_cuit_valido(cuit:str) -> bool:
        return len(cuit) == 11 and cuit.isdigit()

    @staticmethod
    def convertir_moneda(monto: float, tasa_cambio: float, comision: float = 0.02) -> float:
        monto_convertido = monto * tasa_cambio * (1 - comision)
        return round(monto_convertido, 2)

print(ValidadorFinanciero.es_cuit_valido("20384920194"))
print(ValidadorFinanciero.es_cuit_valido("20-38492019-4"))
print(ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05))

print("#################################### Actividad 3 ####################################")

#Ejercicio 3: Interacción Inter-Clase, Métodos de instancia y Delegación
"""Concepto: Colaboración de Objetos.
Contexto: En un sistema transaccional, la clase encargada de procesar pagos delega la
emisión de comprobantes a un objeto notificador independiente.
Consigna: Creá las clases Notificador y ProcesadorPagos para simular el cobro de un
carrito de compras.

Requerimientos Técnicos:

Clase Notificador: Posee el método enviar_recibo(self, cliente: str, total: float) ->
None que imprime un resumen formal del cobro.

Clase ProcesadorPagos:
En su __init__ recibe o instancia un objeto de tipo Notificador.

Método procesar_transaccion(self, cliente: str, items: list[dict],
descuento_cupon: float = 0.0) -> float.

La función itera los items (cada uno un dict con claves "nombre" y "precio"), suma los
precios, aplica el descuento opcional de cupón y llama a enviar_recibo del notificador.

PRUEBA DE INTEGRACIÓN:
carrito = [{"nombre": "Teclado", "precio": 50.0}, {"nombre": "Mouse", "precio": 30.0}]
procesador = ProcesadorPagos()
procesador.procesar_transaccion("Ana Gómez", carrito, descuento_cupon=10.0)"""

class Notificador:
    def enviar_recibo(self, cliente: str, total: float) -> None:
        print(f"Cliente : {cliente}")
        print(f"Total a abonar: {total:.2f}")

class ProcesadorPagos:
    def __init__(self, notificador=None):
        if notificador is None:
            self.notificador = Notificador()
        else:
            self.notificador = notificador

    def procesar_transaccion(self, cliente: str, items: list[dict], descuento_cupon: float = 0.0) -> float:
        subtotal_descuento = 0.0
        for item in items:
            subtotal_descuento += item["precio"]

        #descuento
        total_descuento = subtotal_descuento * (1 - descuento_cupon / 100)

        self.notificador.enviar_recibo(cliente, total_descuento)

        return total_descuento

carrito = [{"nombre": "Teclado", "precio": 50.0},
            {"nombre": "Mouse", "precio": 30.0}
            ]

procesador = ProcesadorPagos()
total_descuento =  procesador.procesar_transaccion("Ana Gómez", carrito, descuento_cupon=10.0)
print(f"Total retornado: ${total_descuento:.2f}")

#Ejercicio 4
#Manejo de Aridad Variable (*args y **kwargs) CONCEPTO : *ARGS / **KWARGS
"""Contexto: Los subsistemas de logging debeen registrar una cantidad indeterminada de eventos de texto junto a metadatos de contexto variables
(IP, usuario, tiempo, ejecución, etc.)
Consigna: Implementá la función generar_auditoria_sistema capaz de recibir cualquier número de mensajes y metadatos clave-valor.

def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:
# Retorna un reporte formateado multi-línea

Requerimientos Técnicos:
modulo: Parámetro posicional obligatorio que se formateará en mayúsculas.
*mensajes: Captura N líneas de log y las numera secuencialmente ([1] ... [2] ...).
**metadatos: Captura N pares clave=valor y los desglosa en el formato CLAVE: VALOR.
PRUEBA REQUERIDA:
log = generar_auditoria_sistema("AUTH", "Intento fallido", "Bloqueo de IP",
usuario="admin", ip="192.168.1.10")
"""
print("#################################### Actividad 4 ####################################")

def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:
    reporte = ""
    reporte = reporte + "MODULO: " + modulo.upper() + "\n"
    for numero, mensaje in enumerate(mensajes, 1):
        reporte = reporte + f"[{numero}] {mensaje}\n"
    for clave, valor in metadatos.items():
        reporte = reporte + f"{clave.upper()}: {valor}\n"
    return reporte

log = generar_auditoria_sistema("AUTH", "Intento fallido", "Bloqueo de IP", 
                                usuario="admin", ip="192.168.1.10") 
print(log)

#Ejercicio 5
#Sistema Integrador (POO, Estáticos, Métodos y Kwargs)
"""Concepto: Integración total
Contexto: Integración final de componentes para una plataforma de salud y
rendimiento deportivo.
Consigna: Desarrolla las clases CalculadoraFitness y Atleta.

Requerimientos Técnicos:
CalculadoraFitness (Clase de utilidades estáticas):
@staticmethod calcular_imc(peso_kg: float, altura_m: float) -> float (Fórmula: peso /
(altura^2)).
@staticmethod clasificar_nivel(imc: float) -> str ("Bajo peso" < 18.5, "Normal" < 25.0,
"Sobrepeso" ≥ 25.0).
Atleta (Clase de entidad):
__init__(self, nombre: str, peso: float, altura: float)
obtener_reporte(self, incluir_recomendacion: bool = False, **metricas_extra) -
> str
El método obtener_reporte llama a los métodos estáticos de CalculadoraFitness,
adjunta las métricas dinámicas enviadas por **metricas_extra y agrega una
recomendación opcional.
"""
print("#################################### Actividad 5 ####################################")

class CalculadoraFitness():

    @staticmethod 
    def calcular_imc(peso_kg: float, altura_m: float) -> float:
        return peso_kg / (altura_m ** 2)

    @staticmethod 
    def clasificar_nivel(imc:float) -> str:
        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25.0:
            return "Normal"
        else:
            return "Sobrepeso"

class Atleta():
    def __init__ (self, nombre:str, peso: float, altura: float):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura


    def obtener_reporte(self, incluir_recomendacion: bool = False, **metricas_extra) -> str:
        imc = CalculadoraFitness.calcular_imc(self.peso, self.altura)
        nivel = CalculadoraFitness.clasificar_nivel(imc)

        reporte = f"Reporte {self.nombre}"
        reporte += f"Peso: {self.peso} kg "
        reporte += f"Altura: {self.altura} metros "
        reporte += f"IMC: {imc:.2f}"
        reporte += f"Nivel: {nivel}"

        if metricas_extra:
            reporte += "Metricas adicionales"
            for clave, valor in metricas_extra.items():
                reporte += f"{clave}: {valor}"

        if incluir_recomendacion:
            reporte += "Recomendación"
            if nivel == "Bajo peso":
                reporte += "Consulta a un nutricionista para aumentar de peso."
            elif nivel == "Normal":
                reporte += "Todo OK"
            elif nivel == "Sobrepeso":
                reporte += "Incorporá actividad física y alimentación"

        return reporte

print("=== PRUEBA 1: Atleta sin métricas extra ===\n")
atleta1 = Atleta("Carlos", 75, 1.75)
print(atleta1.obtener_reporte())

print("\n=== PRUEBA 2: Atleta con métricas extra ===\n")
atleta2 = Atleta("Ana", 60, 1.65)
print(atleta2.obtener_reporte(
    incluir_recomendacion=True,
    porcentaje_grasa=22.5,
))

print("\n=== PRUEBA 3: Atleta con sobrepeso ===\n")
atleta3 = Atleta("Pedro", 95, 1.70)
print(atleta3.obtener_reporte(incluir_recomendacion=True))
