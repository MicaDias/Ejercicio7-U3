from Personal import Personal
from Docente import Docente
from Investigador import Investigador
class DocenteInvestigador(Docente,Investigador):
    __importe=0
    __categoriaE=''
    def __init__(self,cuil='',apellido='',nombre='',sueldoBasico=0,antiguedad=0,carrera='',cargo='',catedra='',areaInvestigacion='',tipoInvestigacion='',importe=0,categoriaE=''):
        super(). __init__(cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra,areaInvestigacion,tipoInvestigacion)
        self.__importe=importe
        self.__categoriaE=categoriaE
    def calcularSueldo(self):
        resultado=0
        resultado=Docente.calcularSueldo()+self.__importe
        return resultado
    def getImporte(self):
        return self.__importe
    def getCategoria(self):
        return self.__categoriaE
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(cuil=self.getCuil(),apellido=self.getApellido(),nombre=self.getNombre(),sueldoBasico=self.getSueldo(),
            antiguedad=self.getAntiguedad(),carrera=self.getCarrera(),cargo=self.getCargo(),catedra=self.getCatedra(),areaInvestigacion=self.getArea(),tipoInvestigacion=self.getTipo(),
            importe=self.__importe,categoriaE=self.__categoriaE)
        )
        return d
