class Auto:
    Modelo = ""
    Marca = ""
    Anio = ""
    Serie = ""
    def setModelo(self,modelo):
        self.Modelo = modelo
    def setMarca(self,marca):
        self.Marca = marca
    def setAnio(self,anio):
        self.Anio = anio
    def setSerie(self,serie):
        self.Serie = serie
    def getModelo(self):
        return self.Modelo
    def getMarca(self):
        return self.Marca
    def getAnio(self):
        return self.Anio
    def getSerie(self):
        return self.Serie

class Agenda():
    def cargarAgenda(self):
        self.archivo = open("Agenda.txt", 'a')

    def guardarAgenda(self):
        self.archivo.close()

    def agregar(self,Auto):
        Modelo = Auto.getModelo()
        Marca = Auto.getMarca()
        Anio = Auto.getAnio()
        Serie = Auto.getSerie()
        self.archivo.write(Modelo + "," + Marca + "," + Anio + "," + Serie + '\n')

    def mostrar_agenda(self):
        archivo = open("Agenda.txt", 'r')
        for element in archivo:
            arreglo = element.split(',')
            print("Modelo: " + arreglo[0])
            print("Marca: " + arreglo[1])
            print("Anio: " + arreglo[2])
            print("Serie: " + arreglo[3])
        archivo.close()

def main():
    agenda = Agenda()
    agenda.cargarAgenda()
    while True:
        print("MENU PRINCIPAL\n1. Agregar auto \n2. Mostrar agenda \n0. Salir")
        try:
            opc = int(input("Elige la opción deseada: "))
            if opc == 1:
                Coche = Auto()
                modelo = str(input("Dame el modelo del auto: "))
                marca = str(input("Dame el marca del auto: "))
                anio = str(input("Dame la anio del auto: "))
                serie = str(input("Dame el serie del auto: "))
                Coche.setModelo(modelo)
                Coche.setMarca(marca)
                Coche.setAnio(anio)
                Coche.setSerie(serie)
                agenda.agregar(Coche)
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