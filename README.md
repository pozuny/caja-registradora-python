# Proyecto 1: Caja Registradora en Python

Programa de consola que simula la caja de un pequeño negocio: registra productos, calcula descuento e impuesto, genera la factura y calcula el cambio.

## Fase 1 - Problema
Un negocio pequeño necesita cobrar rápido y sin errores de cálculo.

## Fase 2 - Requisitos
- Pedir nombre del cliente y cantidad de productos.
- Por cada producto: nombre, precio y cantidad.
- Rechazar precios o cantidades menores o iguales a 0.
- Descuento: 5% si el subtotal es >= 2000, 10% si es >= 5000.
- Cliente frecuente: +2% de descuento, solo si ya tiene algún descuento.
- Calcular ITBIS (18%) sobre el subtotal con descuento.
- Mostrar factura, pedir el pago y calcular cambio o faltante.

## Fase 3 - Diseño
1. Entrada de datos -> 2. Loop de productos -> 3. Descuento -> 4. Factura -> 5. Pago y cambio

## Fase 4 - Código
Archivo: `caja_registradora.py`. Conceptos usados: variables, `input`, `print`, `if/elif/else`, comparaciones, `and/or`, `for` con `range`.

## Fase 5 - Pruebas
| Caso | Entrada | Resultado esperado |
|---|---|---|
| Compra grande, frecuente | Arroz 100x30, Pollo 250x10, si, paga 6000 | Subtotal 5500, descuento 660, total 5711.2, cambio 288.8 |
| Sin descuento | 1 producto de 500 x 1, no | Descuento 0, total 590 |
| Dato inválido | precio 0 | "Datos inválidos", producto no se cuenta |
| Pago insuficiente | total 590, paga 100 | "Faltan RD$ 490.0" |

## Fase 6 - Mejoras (cuando avances)
- [ ] Guardar los productos en una **lista** y mostrar la factura detallada (cuando domines listas).
- [ ] Usar **funciones** para separar el cálculo del descuento.
- [ ] Guardar las facturas en un **archivo** (cuando llegues a archivos).
- [ ] Manejar errores con **excepciones** (si escriben letras en vez de números).
      
