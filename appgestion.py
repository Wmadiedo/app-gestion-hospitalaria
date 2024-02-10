class Paciente:
    def __init__(self, documento, nombre, sexo, fecha_nacimiento):
        self.documento = documento
        self.nombre = nombre
        self.sexo = sexo
        self.fecha_nacimiento = fecha_nacimiento
        self.historia_clinica = HistoriaClinica()

class HistoriaClinica:
    def __init__(self):
        self.signos_vitales = []
        self.notas_evolucion = []
        self.imagenes_diagnosticas = []
        self.resultados_examenes = []
        self.medicamentos_formulados = []

class Cama:
    def __init__(self, numero):
        self.numero = numero
        self.paciente = None

class Medicamento:
    def __init__(self, nombre, dosis):
        self.nombre = nombre
        self.dosis = dosis

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.camas = []

    def agregar_cama(self, numero):
        self.camas.append(Cama(numero))

    def asignar_paciente_a_cama(self, paciente, numero_cama):
        for cama in self.camas:
            if cama.numero == numero_cama:
                cama.paciente = paciente
                break

    def generar_reporte_ocupacion_hospitalaria(self):
        total_camas = len(self.camas)
        camas_ocupadas = sum(1 for cama in self.camas if cama.paciente is not None)
        porcentaje_ocupacion = (camas_ocupadas / total_camas) * 100
        return porcentaje_ocupacion

    # Otros métodos para generar reportes de indicadores y realizar operaciones de gestión hospitalaria

# Ejemplo de uso
if __name__ == "__main__":
    hospital = Hospital("Hospital XYZ")
    hospital.agregar_cama(1)
    hospital.agregar_cama(2)

    paciente1 = Paciente("123456789", "Juan Perez", "Masculino", "1990-01-01")
    paciente2 = Paciente("987654321", "Maria Garcia", "Femenino", "1985-05-15")

    hospital.asignar_paciente_a_cama(paciente1, 1)
    hospital.asignar_paciente_a_cama(paciente2, 2)

    print("Porcentaje de ocupación hospitalaria:", hospital.generar_reporte_ocupacion_hospitalaria())
