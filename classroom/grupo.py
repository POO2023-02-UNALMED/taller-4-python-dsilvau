from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[], grado="Grado 12"):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        Grupo.grado = grado

        

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs:
            x = Asignatura(kwargs[x])
            self._asignaturas.append(x)

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = list(self.listadoAlumnos) + lista

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"
        

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
