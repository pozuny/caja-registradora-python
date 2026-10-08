# ==========================================
# PROYECTO 1: CAJA REGISTRADORA
# Usa: variables, input, print, if/elif/else,
# operadores de comparación, and/or/not, for + range
# ==========================================

ITBIS = 0.18  # impuesto (puedes cambiarlo si cambia la tasa)

print("=== CAJA REGISTRADORA ===")
nombre_cliente = input("Nombre del cliente: ")
cantidad_productos = int(input("¿Cuántos productos diferentes compra? "))

subtotal = 0.0

# --- 1. Registrar productos ---
for i in range(1, cantidad_productos + 1):
    print("\nProducto", i)
    nombre = input("Nombre: ")
    precio = float(input("Precio unitario (RD$): "))
    cantidad = int(input("Cantidad: "))

    if precio <= 0 or cantidad <= 0:
        print("Datos inválidos. Este producto no se cuenta.")
    else:
        total_producto = precio * cantidad
        subtotal = subtotal + total_producto
        print(nombre, "x", cantidad, "= RD$", total_producto)

# --- 2. Calcular descuento ---
es_frecuente = input("\n¿Es cliente frecuente? (si/no): ") == "si"

if subtotal >= 5000:
    descuento_porcentaje = 0.10
elif subtotal >= 2000:
    descuento_porcentaje = 0.05
else:
    descuento_porcentaje = 0.0

# Cliente frecuente: 2% extra, pero solo si ya tiene algún descuento
if es_frecuente and descuento_porcentaje > 0:
    descuento_porcentaje = descuento_porcentaje + 0.02

descuento = subtotal * descuento_porcentaje
subtotal_con_descuento = subtotal - descuento
impuesto = subtotal_con_descuento * ITBIS
total = subtotal_con_descuento + impuesto

# --- 3. Mostrar factura ---
print("\n=========== FACTURA ===========")
print("Cliente:", nombre_cliente)
print("Subtotal:           RD$", round(subtotal, 2))
print("Descuento:         -RD$", round(descuento, 2))
print("ITBIS:              RD$", round(impuesto, 2))
print("TOTAL A PAGAR:      RD$", round(total, 2))
print("===============================")

# --- 4. Pago y cambio ---
if total > 0:
    pago = float(input("\n¿Con cuánto paga el cliente? RD$ "))
    if pago >= total:
        print("Cambio: RD$", round(pago - total, 2))
        print("¡Gracias por su compra!")
    else:
        print("Pago insuficiente. Faltan RD$", round(total - pago, 2))
else:
    print("\nNo hay nada que cobrar.")
