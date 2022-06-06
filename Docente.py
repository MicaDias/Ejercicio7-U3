from Personal import Personal
class Docente(Personal):
    __carrera=''
    __cargo=''
    __catedra=''
    def __init__(self,cuil='',apellido='',nombre='',sueldoBasico=0,antiguedad=0,carrera='',cargo='',catedra='',areaInvestigacion='',tipoInvestigacion=''):
        super(). __init__(cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra,areaInvestigacion,tipoInvestigacion)
        self.__carrera=carrera
        self.__cargo=cargo
        self.__catedra=catedra
    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    def calcularSueldo(self):
        resultado=0
        porcentaje=0
        sueldoCargo=0
        if self.__cargo=='simple':
            porcentaje+=10
        elif self.__cargo=='semiexclusivo':
            porcentaje+=20
        elif self.__cargo=='exclusivo':
            porcentaje+=50
        sueldoCargo=(self.getSueldo()*porcentaje)/100
        resultado=self.getSueldo()+self.calcularSueldoPorAnt()+sueldoCargo
        return resultado
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),carrera=self.__carrera,cargo=self.__cargo,catedra=self.__catedra)
        )
        return d