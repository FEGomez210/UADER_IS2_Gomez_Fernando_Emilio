# -------------------------------------------------------------------------
# Facultad: FCyT - UADER[cite: 1]
# Alumno: Gómez, Fernando Emilio[cite: 1]
# Cátedra: Ingeniería de Software II[cite: 1]
# Profesor: Dr. Pedro E. Colla[cite: 1]
# Ayudante: Lic. Lucía Blanc[cite: 1]
# -------------------------------------------------------------------------

class Ping:
    """Clase que representa el servicio real de red."""
    
    def execute(self, ip: str):
        """Realiza 10 intentos de ping si la IP inicia con 192."""
        # Validación de dominio de red específica según requerimiento[cite: 1]
        if ip.startswith("192."):
            for i in range(1, 11):
                print(f"Intento {i}: Ping a {ip} - Exitoso")
        else:
            print("Error: Protocolo solo permitido para red local 192.x")

    def execute_free(self, ip: str):
        """Método sin validación de prefijo de IP."""
        # Se utiliza para saltar la restricción del método execute[cite: 1]
        for i in range(1, 11):
            print(f"Intento {i}: Ping Libre a {ip} - Conectado")

class PingProxy:
    """Clase Proxy que intercepta y gestiona las peticiones a Ping."""
    
    def __init__(self):
        # Mantiene una referencia al objeto real para delegar tareas[cite: 1]
        self._ping_real = Ping()

    def execute(self, ip: str):
        """Controla el acceso y redirige según la dirección IP provista."""
        # Regla de negocio: si la IP es la específica del servidor final[cite: 1]
        if ip == "192.168.0.254":
            print("Proxy: Detectada IP de gestión. Redirigiendo a Google...")
            # Delega a execute_free para evadir la validación[cite: 1]
            self._ping_real.execute_free("www.google.com")
        else:
            # Para cualquier otra IP, usa el flujo estándar de validación[cite: 1]
            self._ping_real.execute(ip)

# Ejemplo de uso
if __name__ == "__main__":
    interceptor = PingProxy()
    interceptor.execute("192.168.0.254")
