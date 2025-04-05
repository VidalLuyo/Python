class ConfiguracionGlobal:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            print("Creando configuración global...")
            cls._instancia = super().__new__(cls)
        else:
            print("Configuración global ya existe. Usando la instancia existente.")
        return cls._instancia

    def __init__(self, ip="192.168.0.1", puerto=8080, timeout=30):
        self.ip = ip
        self.puerto = puerto
        self.timeout = timeout

# Crear dos instancias de ConfiguracionGlobal
config1 = ConfiguracionGlobal()
config2 = ConfiguracionGlobal("192.168.0.2", 9090, 60)

print(f"Config1 IP: {config1.ip}, Puerto: {config1.puerto}, Timeout: {config1.timeout}")
print(f"Config2 IP: {config2.ip}, Puerto: {config2.puerto}, Timeout: {config2.timeout}")
print(config1 is config2)  # Debería devolver True
