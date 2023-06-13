from backend.models import Propiedad, CaracteristicasPropiedad
from django.db import connection
from http import HTTPStatus

class DAOPropiedad :
    def get_detalle_propiedades():
        with connection.cursor() as cursor:
            try :
                cursor.execute('SELECT * FROM vista_detalle_propiedades')
                resultados = cursor.fetchall()
            except :
                return HTTPStatus.NOT_FOUND
        data = []

        if resultados is not None :
            for fila in resultados:
                nombres_columnas = [desc[0] for desc in cursor.description]
                item = dict(zip(nombres_columnas, fila))
                data.append(item)
            return (data)
        else :
            return HTTPStatus.NOT_FOUND
        
    def get_caracteristicas_propiedad(id_propiedad):
        if id_propiedad is not None :
            with connection.cursor() as cursor:
                try :
                    cursor.execute('SELECT * FROM vista_caracteristicas_propiedades WHERE id_propiedad = %s', [id_propiedad])
                    result = cursor.fetchone()
                except :
                    return HTTPStatus.NOT_FOUND

            if result is not None:
                nombres_columnas = [desc[0] for desc in cursor.description]
                data = dict(zip(nombres_columnas, result))
                return (data)
            else :
                return HTTPStatus.NOT_FOUND