from Apoyo import Apoyo
from Docente import Docente
from DocenteInvestigador import DocenteInvestigador
from Investigador import Investigador
from Personal import Personal
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
            6:self.opcion6,
            7:self.opcion7,
            8:self.opcion8,
            9:self.salir
        }
    def lanzarMenu(self,lista,objectEncoder):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1: Insertar un agente.')
            print('-Ingrese 2: Agregar un angente.')
            print('-Ingrese 3: Mostrar el tipo de agente.')
            print('-Ingrese 4: Mostrar docentes investigadores de la carrera')
            print('-Ingrese 5: Mostrar la cantidad de docentes investigadores e investigadores del area.')
            print('-Ingrese 6:Mostrar agentes.')
            print('-Ingrese 7:Mostrar docentes investigadores.')
            print('-Ingrese 8:Guardar los datos de todos los agentes.')
            print('-Ingrese 9:para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion>0 and opcion<8:
                ejecutar(lista)
            elif opcion==8:
                ejecutar(lista,objectEncoder)
            else:
                ejecutar()
    def opcion1(self,lista):
        pos=self.cargarNumeroEntero('Ingrese la posicion que desea guardar el elemento:')
        agente=self.cargarPersonal()
        if isinstance(agente,Personal):
            try:
                lista.insertarElemento(agente,pos)
            except IndexError:
                print('La posicion ingresada es incorrecta.')
        else:
            print('NO SE PUEDE INSERTAR.')

    def opcion2(self,lista):
        agente=self.cargarPersonal()
        if isinstance(agente,Personal):
            lista.agregarElemento(agente)
        else:
            print('NO SE PUEDE AGREGAR.')
    def opcion3(self,lista):
        pos=self.cargarNumeroEntero('Ingrese la posicion:')
        try:
            lista.mostrarElemento(pos)
        except IndexError:
            print('La posicion ingresada es incorrecta.')
    def opcion4(self,lista):
        carrera=input('Ingrese la carrera:')
        lista.mostrarOrdenadoPorCarrera(carrera)
    def opcion5(self,lista):
        area=input('Ingrese el area de investigacion:')
        lista.mostrarPorInvestigacion(area)
    def opcion6(self,lista):
        lista.mostrarAgentes()
    def opcion7(self,lista):
        categoriaE=input('Ingrese la categoria(I,II,III,IV o V):')
        lista.mostrarPorCategoria(categoriaE)
    def opcion8(self,lista,objectEncoder):
        lista.guardarArchivo(objectEncoder)
    def cargarPersonal(self):
        agente=None
        print('******Cargar Personal******')
        numero=self.cargarNumeroEntero('Ingrese 1)-Docente, 2)-Investigador, 3)-Apoyo, 4)-Docente Investigador:')
        if numero!=5:
            if numero==1:
                print('*******Cargar Docente*******')
                cuil=input('-Ingrese el cuil:')
                apellido=input('-Ingrese el apellido:')
                nombre=input('-Ingrese el nombre:')
                sueldo=self.cargarNumeroEntero('-Ingrese el sueldo:')
                antiguedad=self.cargarNumeroEntero('-Ingrese la antiguedad:')
                carrera=input('-Ingrese la carrera:')
                cargo=input('-Ingrese el cargo(simple-semiexclusivo-exclusivo):')
                catedra=input('-Ingrese la catedra:')
                personal=Docente(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra)
            elif numero==2:
                print('********Cargar Investigador*******')
                cuil=input('-Ingrese el cuil:')
                apellido=input('-Ingrese el apellido:')
                nombre=input('-Ingrese el nombre:')
                sueldo=self.cargarNumeroEntero('-Ingrese el sueldo:')
                antiguedad=self.cargarNumeroEntero('-Ingrese la antiguedad:')
                area=input('Ingrese el area de investigacion:')
                tipo=input('Ingrese el tipo de investigacion:')
                personal=Investigador(cuil,apellido,nombre,sueldo,antiguedad,None,None,None,area,tipo)
            elif numero==3:
                print('********Cargar Personal de Apoyo**********')
                cuil=input('-Ingrese el cuil:')
                apellido=input('-Ingrese el apellido:')
                nombre=input('-Ingrese el nombre:')
                sueldo=self.cargarNumeroEntero('-Ingrese el sueldo:')
                antiguedad=self.cargarNumeroEntero('-Ingrese la antiguedad:')
                categoria=self.cargarNumeroEntero('-Ingrese la categoria(1-10,11-20,21-22):')
                personal=Apoyo(cuil,apellido,nombre,sueldo,antiguedad,None,None,None,None,None,categoria)
            elif numero==4:
                print('********Cargar Docente Investigador**********')
                cuil=input('-Ingrese el cuil:')
                apellido=input('-Ingrese el apellido:')
                nombre=input('-Ingrese el nombre:')
                sueldo=self.cargarNumeroEntero('-Ingrese el sueldo:')
                antiguedad=self.cargarNumeroEntero('-Ingrese la antiguedad:')
                carrera=input('-Ingrese la carrera:')
                cargo=input('-Ingrese el cargo(simple-semiexclusivo-exclusivo):')
                catedra=input('-Ingrese la catedra:')
                area=input('Ingrese el area de investigacion:')
                tipo=input('Ingrese el tipo de investigacion:')
                importe=self.cargarNumeroEntero('Ingrese el importe:')
                categoria=input('-Ingrese la categoria:')
                personal=DocenteInvestigador(cuil,apellido,nombre,sueldo,antiguedad,carrera,cargo,catedra,area,tipo,importe,categoria)
            agente=personal
        else:
            print('numero incorrecto')
        return agente
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')