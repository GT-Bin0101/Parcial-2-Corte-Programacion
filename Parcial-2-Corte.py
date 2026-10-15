vehiculos = [["", "", "", 0, 0, 0, 0] for _ in range(30)]
cuenta = 0


def registrar_ingreso():
    global cuenta
    if cuenta >= 30:
        print("No hay espacio para más vehículos.")
        return
    v = vehiculos[cuenta]
    v[0] = input("Placa: ")
    v[1] = input("Nombre del propietario: ")
    v[2] = input("Número de celular: ")
    v[3] = int(input("Día de ingreso: "))
    print("Vehículo registrado.")
    cuenta += 1


def registrar_salida():
    if cuenta == 0:
        print("No hay vehículos registrados.")
        return
    placa = input("Ingrese la placa del vehículo que sale: ")
    for i in range(cuenta):
        if vehiculos[i][0].upper() == placa.upper() and vehiculos[i][6] == 0:
            dia = int(input("Día de salida: "))
            vehiculos[i][4] = dia
            vehiculos[i][5] = dia - vehiculos[i][3]
            vehiculos[i][6] = 1
            print("Vehículo entregado y reparado.")
            return
    print("No se encontró un vehículo pendiente con esa placa.")


def reporte_terminados():
    ok = [v for v in vehiculos[:cuenta] if v[6] == 1]
    print("\nVehículos terminados:", len(ok))
    for v in ok:
        print(f"{v[0]} | {v[1]} | {v[5]} días")


def reporte_total():
    print("\nTodos los vehículos del mes:")
    for v in vehiculos[:cuenta]:
        print(f"{v[0]} | {v[1]} | {v[2]}")


while True:
    print("\n--- TALLER ---")
    print("1. Ingresar vehículo")
    print("2. Registrar salida")
    print("3. Reporte de terminados")
    print("4. Reporte de todos")
    print("5. Salir")
    op = input("Opción: ")
    if op == "1":
        registrar_ingreso()
    elif op == "2":
        registrar_salida()
    elif op == "3":
        reporte_terminados()
    elif op == "4":
        reporte_total()
    elif op == "5":
        print("Cerrando aplicación...")
        break
    else:
        print("Opción inválida.")
