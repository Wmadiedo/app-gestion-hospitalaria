#ENUNCIADO El Hospital San Vicente es un centro de salud de alta complejidad ubicado en la ciudad de Cartagena.
#Cuenta con una capacidad de 300 camas y atiende alrededor de 1.000 pacientes al día. Actualmente, el hospital almacena las historias clínicas de los pacientes en archivos físicos que se guardan en el área de Archivo. 
#Cuando un médico necesita consultar la historia de un paciente, debe solicitar el archivo al área de Archivo y esperar a que le sea entregado. Esto genera una serie de problemas, tales como. Demoras en la atención,
#ya que se debe esperar la entrega física de la historia clínica. En promedio se tarda 20 minutos. Riesgos de extravío de historias clínicas, lo cual sucede aproximadamente en el 5% de las solicitudes. 
#Dificultades para compartir en tiempo real información de un paciente entre médicos de diferentes especialidades. Imposibilidad de generar reportes y estadísticas a partir de los datos de las historias clínicas.
#El hospital desea desarrollar un sistema de información que permita digitalizar y centralizar las historias clínicas de los pacientes,
#de forma que estén disponibles en línea para los médicos autorizados y se pueda obtener información para la gestión hospitalaria.
#El producto mínimo viable que se requiere es; gestionar historia clínica electrónica de cada paciente, generar reportes de indicadores como: porcentaje de ocupación hospitalaria, promedios de estancia por servicio, 
#cantidad de admisiones y altas por servicio, pacientes con enfermedades crónicas y prescripción de medicamentos por servicio.
#Los datos de entrada que se le solicitarán a los pacientes son los siguiente:
#Datos del paciente (documento, nombre, sexo, fecha nacimiento)
#Signos vitales (presión arterial, temperatura, saturación O2, frecuencia respiratoria) Notas de evolución Imágenes diagnósticas
#Resultados de exámenes de laboratorio
#Medicamentos formulados
#Los beneficios que se logran con dicha aplicación son tales como el acceso rápido a la información de los pacientes, mejor coordinación entre especialidades médicas,
#reducción del riesgo de pérdida de historias clínicas y toma de decisiones gerenciales basada en datos. El desarrollo se hará con Python, aplicando POO para representar conceptos como Historia Clínica, Paciente, Cama y Medicamentos.
#Se debe utilizar PEP8 para estandarización.
#Wollman Madiedo Hoyos T00065230
class Paciente:
  #El paciente posee una informacion personal ya mencionada en el enunciado
  def __init__(self, documento, nombre, sexo, fecha_nacimiento):
      self.documento = documento
      self.nombre = nombre
      self.sexo = sexo
      self.fecha_nacimiento = fecha_nacimiento
#cada paciente lleva asignada una historia clinica
class HistoriaClinica:
  def __init__(self, paciente):
      self.paciente = paciente
      self.signos_vitales = []
      self.notas_evolucion = []
      self.imagenes_diagnosticas = []
      self.resultados_examenes = []
      self.medicamentos_formulados = []
#y cada cama puede o no estar asignada a un paciente
class Cama:
  def __init__(self, numero):
      self.numero = numero
      self.paciente = None  # Paciente asignado a la cama

class Medicamento:
  def __init__(self, nombre, dosis):
      self.nombre = nombre
      self.dosis = dosis

# aqui creo una lista de los pacientes registrados hasta el momento
pacientes = []

def agregar_paciente():
  documento = input("Ingrese el documento del paciente: ")
  nombre = input("Ingrese el nombre del paciente: ")
  sexo = input("Ingrese el sexo del paciente (M/F): ")
  fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
  paciente = Paciente(documento, nombre, sexo, fecha_nacimiento)
  pacientes.append(paciente)
  return paciente
print("Ingrese los datos del nuevo paciente:")
nuevo_paciente = agregar_paciente()
def agregar_historia_clinica(paciente):
    historia_clinica = HistoriaClinica(paciente)
    paciente.historia_clinica = historia_clinica
    return historia_clinica
def asignar_cama(paciente):
    numero_cama = int(input("Ingrese el número de la cama a asignar: "))
    cama = Cama(numero_cama)
    paciente.cama_asignada = cama
    cama.paciente = paciente
asignar_cama(nuevo_paciente)
def prescribir_medicamento(paciente):
  nombre = input("Ingrese el nombre del medicamento: ")
  dosis = input("Ingrese la dosis del medicamento: ")
  medicamento = Medicamento(nombre, dosis)
  paciente.historia_clinica.medicamentos_formulados.append(medicamento)
# Agregar historia clínica
print("\nAgregue la historia clínica del paciente:")
agregar_historia_clinica(nuevo_paciente)

# Prescribir medicamentos
while input("¿Desea prescribir un medicamento? (S/N): ").upper() == "S":
    prescribir_medicamento(nuevo_paciente)
# Función para mostrar la información de todos los pacientes
def mostrar_pacientes():
    for paciente in pacientes:
        print("Documento:", paciente.documento)
        print("Nombre:", paciente.nombre)
        print("Sexo:", paciente.sexo)
        print("Fecha de nacimiento:", paciente.fecha_nacimiento)
        print("\nInformación de la historia clínica del paciente:")
        print("Signos vitales:", paciente.historia_clinica.signos_vitales)
        print("Notas de evolución:", paciente.historia_clinica.notas_evolucion)
        print("Imágenes diagnósticas:", paciente.historia_clinica.imagenes_diagnosticas)
        print("Resultados de exámenes:", paciente.historia_clinica.resultados_examenes)
        print("Medicamentos formulados:", [med.nombre for med inpaciente.historia_clinica.medicamentos_formulados])
        print("\nInformación de la cama asignada al paciente:")
        print("Número de cama:", paciente.cama_asignada.numero)
        print()
#y la llamamos
print("Información de todos los pacientes:")
mostrar_pacientes()
