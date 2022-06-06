import abc
from abc import ABC
class Personal(ABC):
    __cuil=''
    __apellido=''
    __nombre=''
    __sueldoBasico=0
    __antiguedad=0
    def __init__(self,cuil='',apellido='',nombre='',sueldoBasico=0,antiguedad=0,carrera='',cargo='',catedra='',areaInvestigacion='',tipoInvestigacion=''):
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__sueldoBasico=sueldoBasico
        self.__antiguedad=antiguedad
    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getAntiguedad(self):
        return self.__antiguedad
    def getSueldo(self):
        return self.__sueldoBasico
    def getNombre(self):
        return self.__nombre
    def mostrarDatos(self):
        print('Cuil:{}, Nombre:{}, Apellido:{}'.format(self.__cuil,self.__nombre,self.__apellido))
    @abc.abstractclassmethod
    def calcularSueldo():
        pass
    def calcularSueldoPorAnt(self):
        resultado=0
        resultado=(self.__sueldoBasico*self.__antiguedad)/100
        return resultado
    def mostrarDatosSueldos(self):
        print('Cuil:{}, Nombre:{}, Apellido:{},Sueldo:{}'.format(self.__cuil,self.__nombre,self.__apellido,self.calcularSueldo()))
    def toJSON(self):
        return dict(cuil=self.__cuil,apellido=self.__apellido,nombre=self.__nombre,sueldoBasico=self.__sueldoBasico,antiguedad=self.__antiguedad)
        
    