class Alumno:
    Codigo = ""
    Nombre = ""
    Carrera = ""
    Telefono = ""
    def setCodigo(self,codigo):
        self.Codigo = codigo
    def setNombre(self,nombre):
        self.Nombre = nombre
    def setCarrera(self,carrera):
        self.Carrera = carrera
    def setTelefono(self,telefono):
        self.Telefono = telefono
    def getCodigo(self):
        return self.Codigo
    def getNombre(self):
        return self.Nombre
    def getCarrera(self):
        return self.Carrera
    def getTelefono(self):
        return self.Telefono

class Agenda():
    def cargarAgenda(self):
        self.archivo = open("Agenda.txt", 'a')

    def guardarAgenda(self):
        self.archivo.close()

    def agregar(self,Alumno):
        Codigo = Alumno.getCodigo()
        Nombre = Alumno.getNombre()
        Carrera = Alumno.getCarrera()
        Telefono = Alumno.getTelefono()
        self.archivo.write(Codigo + "," + Nombre + "," + Carrera + "," + Telefono + '\n')

    def mostrar_agenda(self):
        archivo = open("Agenda.txt", 'r')
        for element in archivo:
            arreglo = element.split(',')
            print("Codigo: " + arreglo[0])
            print("Nombre: " + arreglo[1])
            print("Carrera: " + arreglo[2])
            print("Telefono: " + arreglo[3])
        archivo.close()

def main():
    agenda = Agenda()
    agenda.cargarAgenda()
    while True:
        print("MENU PRINCIPAL\n1. Agregar estudiante \n2. Mostrar agenda \n0. Salir")
        try:
            opc = int(input("Elige la opción deseada: "))
            if opc == 1:
                Estudiante = Alumno()
                codigo = str(input("Dame el codigo del estudiante: "))
                nombre = str(input("Dame el nombre del estudiante: "))
                carrera = str(input("Dame la carrera del estudiante: "))
                telefono = str(input("Dame el telefono del estudiante: "))
                Estudiante.setNombre(nombre)
                Estudiante.setCodigo(codigo)
                Estudiante.setCarrera(carrera)
                Estudiante.setTelefono(telefono)
                agenda.agregar(Estudiante)
                agenda.guardarAgenda()
                agenda.cargarAgenda()
                print("")
            elif opc == 2:
                agenda.mostrar_agenda()
                print("")
            elif opc == 0:
                print("Gracias por usar el programa vuelva pronto :)")
                break
            else:
                print("Opcion incorrecta, repita de nuevo :)")
        except:
            print("Tipo de dato no valido\n")

main()