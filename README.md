# TallerElectronica

### 1. Patrones de Segmentos y Justificación
Para los dígitos del 0 al 9 se usaron los patrones estándar con las siguientes decisiones:
* **Dígito 1:** Dibujado a la derecha.
* **Dígito 6:** Dibujado cerrado (enciende el segmento superior A).
* **Dígito 9:** Dibujado cerrado (enciende el segmento inferior D).

Para los valores del 10 al 15 (prohibido usar A-F), se diseñaron los siguientes símbolos:
* **10 (Grados `°`):** Enciende A,B,F,G. Representa temperatura.
* **11 (Menú `≡`):** Enciende A,G,D. Ícono de interfaces gráficas.
* **12 (Corchete Izquierdo `[`):** Enciende A,D,E,F. Símbolo de programación.
* **13 (Corchete Derecho `]`):** Enciende A,B,C,D. Complemento lógico de la entrada 12.
* **14 (Cuadro Inferior `_`):** Enciende C,D,E,G. Indicador de nivel mínimo.
* **15 (Igual `=`):** Enciende D,G. Representa equidad en cálculos.

### 2. Comandos Utilizados
Para generar VHDL y simulación: `python sevensegdec.py`
Para pruebas unitarias: `pytest test_sevensegdec.py -v`

### 3. Resultados de Simulación y Explicación
* **¿Qué verifica el testbench?:** Recorre los 16 valores binarios posibles en la entrada, genera la salida simulada y la compara línea por línea contra la tabla de verdad original.
* **¿Por qué no hay errores?:** Porque la lógica combinacional se sintetiza con la misma tabla (LUT) que se usa como fuente de verdad para la prueba. Al ser consistentes, pasa silenciosamente.
* **¿Qué representan los 7 bits de `sseg`?:** Son las señales de control individuales para encender/apagar los 7 pines físicos del display (abcdefg).
* **Sobre el código HDL:** La tabla de búsqueda (LUT) se convierte en lógica combinacional (sin reloj) a través de sentencias `with/select` en VHDL.