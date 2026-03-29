#CODIGO INICIAL DE LA CALCULADORA DE INSTALACIONES AA
class CalculadoraANN:
    def __init__(self):
        # Nuevos valores actualizados
        self.__INSTALACION_BASICA_3500 = 170000.0
        self.__INSTALACION_BASICA_5000 = 190000.0
        self.__KIT_MATERIALES = 100000.0
        self.__INSTALACION_ELECTRICA = 85000.0
        self.__METRO_ADICIONAL = 33000.0
        self.contacto = "2236243600"

    def formatear(self, valor):
        return f"${valor:,.2f}"

    def calcular_presupuesto(self, opcion, altura, kit, metros, elec):
        # 1. Validación de Visita Técnica (Prioridad Máxima)
        if opcion == '3' or altura.lower() in ['s', 'si']:
            motivo = "EQUIPO > 5000 FRIGORÍAS" if opcion == '3' else "TRABAJO EN ALTURA / ELEVACIÓN"
            return f"\n⚠️ VISITA TÉCNICA REQUERIDA\nMotivo: {motivo}\n📞 Contacto: {self.contacto}"

        # 2. Determinar Base de Instalación
        if opcion == '1':
            total = self.__INSTALACION_BASICA_3500
            detalle = [f"✅ Inst. Básica (hasta 3500): {self.formatear(total)}"]
        else:
            total = self.__INSTALACION_BASICA_5000
            detalle = [f"✅ Inst. Básica (3500 a 5000): {self.formatear(total)}"]

        # 3. Sumar Kit de Materiales (Si el usuario pone 's' o 'si')
        if kit.lower() in ['s', 'si']:
            total += self.__KIT_MATERIALES
            detalle.append(f"✅ Kit de Materiales: {self.formatear(self.__KIT_MATERIALES)}")

            # 4. Sumar Metros Adicionales (Solo si lleva kit y supera los 3m)
            if metros > 3:
                adicionales = metros - 3
                costo_metros = adicionales * self.__METRO_ADICIONAL
                total += costo_metros
                detalle.append(f"✅ Metros adicionales ({adicionales}m): {self.formatear(costo_metros)}")

        # 5. Sumar Instalación Eléctrica
        if elec.lower() in ['s', 'si']:
            total += self.__INSTALACION_ELECTRICA
            detalle.append(f"✅ Instalación Eléctrica: {self.formatear(self.__INSTALACION_ELECTRICA)}")

        # 6. Salida de Resultados
        resultado = "\n" + "—"*40 + "\n"
        resultado += f"💰 TOTAL FINAL: {self.formatear(total)}\n"
        resultado += "—"*40 + "\n"
        resultado += "\n".join(detalle)
        resultado += f"\n\nPara coordinar: {self.contacto}\n" + "—"*40
        return resultado

# --- Interacción con el Cliente ---
calc = CalculadoraANN()

print("❄️ BIENVENIDO A ANN MULTISERVICIOS")
print("1. Equipo hasta 3500 Frigorías")
print("2. Equipo de 3500 a 5000 Frigorías")
print("3. Equipo de más de 5000 Frigorías")

op = input("\nSeleccione capacidad (1, 2 o 3): ")
alt = input("¿Requiere andamios o medios de elevación? (s/n): ")

if op == '3' or alt.lower() in ['s', 'si']:
    print(calc.calcular_presupuesto(op, alt, "", 0, ""))
else:
    kit_mat = input("¿Incluye kit de materiales? (s/n): ")
    distancia = float(input("¿Cuántos metros totales de cañería? (Mínimo 3): "))
    inst_elec = input("¿Requiere instalación eléctrica? (s/n): ")

    # Llamada al método con todos los parámetros
    print(calc.calcular_presupuesto(op, alt, kit_mat, distancia, inst_elec))
