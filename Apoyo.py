from Personal import Personal
class Apoyo(Personal):
    __categoria=0
    def __init__(self,cuil='',apellido='',nombre='',sueldoBasico=0,antiguedad=0,carrera='',cargo='',catedra='',areaInvestigacion='',tipoInvestigacion='',categoria=0):
        super(). __init__(cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra,areaInvestigacion,tipoInvestigacion)
        self.__categoria=categoria
    def calcularSueldo(self):
        resultado=0
        porcentaje=0
        sueldoPorCategoria=0
        if self.__categoria>=1 and self.__categoria<11:
            porcentaje+=10
        elif self.__categoria>=11 and self.__categoria<=20:
            porcentaje+=20
        elif self.__categoria==21 or self.__categoria==22:
            porcentaje+=30
        sueldoPorCategoria=(self.getSueldo()*porcentaje)/100
        resultado=self.getSueldo()+self.calcularSueldoPorAnt()+sueldoPorCategoria
        return resultado
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(cuil=self.getCuil(),apellido=self.getApellido(),nombre=self.getNombre(),sueldoBasico=self.getSueldo(),
            antiguedad=self.getAntiguedad(),categoria=self.__categoria)
        )
        return d
    