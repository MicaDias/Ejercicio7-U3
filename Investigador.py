from Personal import Personal
class Investigador(Personal):
    __areaInvestigacion=''
    __tipoInvestigacion=''
    def __init__(self,cuil='',apellido='',nombre='',sueldoBasico=0,antiguedad=0,carrera='',cargo='',catedra='',areaInvestigacion='',tipoInvestigacion=''):
        super(). __init__(cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra,areaInvestigacion,tipoInvestigacion)
        self.__areaInvestigacion=areaInvestigacion
        self.__tipoInvestigacion=tipoInvestigacion
    def getArea(self):
        return self.__areaInvestigacion
    def getTipo(self):
        return self.__tipoInvestigacion
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(super().toJSON(),areaInvestigacion=self.__areaInvestigacion,tipoInvestigacion=self.__tipoInvestigacion)
        )
        return d
    def calcularSueldo(self):
        resultado=0
        resultado=self.getSueldo()+self.calcularSueldoPorAnt()
        return resultado
