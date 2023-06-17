from backend.models import *
from django.db import connection
from http import HTTPStatus


class DAOPropiedad :
    def get_propiedad (id):
        try:
            return Propiedad.objects.get(id_propiedad = id)
        except Propiedad.DoesNotExist:
            raise None
        
    def get_tipo_propiedad(id):
        try :
            return TipoPropiedad.objects.get(id_tipo_propiedad = id)
        except TipoPropiedad.DoesNotExist:
            raise None
        
    def get_comuna (id):
        try :
            return Comuna.objects.get(id_comuna = id)
        except Comuna.DoesNotExist:
            raise None

    def get_detalle_propiedades():
        with connection.cursor() as cursor:
            try :
                cursor.execute("""
                SELECT
    	            t1.id_propiedad id_propiedad,
    	            t1.valor_propiedad valor_propiedad,
    	            t1.es_arriendo es_arriendo,
                    t1.es_venta es_venta,
    	            t2.nombre_tipo_propiedad nombre_tipo_propiedad,
    	            t3.nombre_comuna nombre_comuna,
    	            t4.nombre_region nombre_region
                FROM
    	            backend_propiedad t1 inner join backend_tipopropiedad t2
    	            on (t1.id_tipo_propiedad_id = t2.id_tipo_propiedad)
    	            inner join backend_comuna t3
    	            on (t1.id_comuna_id = t3.id_comuna)
    	            inner join backend_region t4
    	            on (t3.id_region_id = t4.id_region)
                """)
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
    # , valor_desde, valor_hasta, es_arriendo, es_venta
    def get_propiedades_filtradas (id_comuna) :
        resultados = []
        with connection.cursor() as cursor:
            try :
                cursor.execute("""
                SELECT
    	            COUNT(*)
                FROM
    	            backend_propiedad t1 inner join backend_tipopropiedad t2
    	            on (t1.id_tipo_propiedad_id = t2.id_tipo_propiedad)
    	            inner join backend_comuna t3
    	            on (t1.id_comuna_id = t3.id_comuna)
    	            inner join backend_region t4
    	            on (t3.id_region_id = t4.id_region)
                WHERE
                    t1.id_comuna_id = %s
                """, [id_comuna])
                count = cursor.fetchone()
                num_filas = count[0]

                cursor.execute("""
                SELECT
    	            t1.id_propiedad id_propiedad,
    	            t1.valor_propiedad valor_propiedad,
    	            t1.es_arriendo es_arriendo,
                    t1.es_venta es_venta,
    	            t2.nombre_tipo_propiedad nombre_tipo_propiedad,
    	            t3.nombre_comuna nombre_comuna,
    	            t4.nombre_region nombre_region
                FROM
    	            backend_propiedad t1 inner join backend_tipopropiedad t2
    	            on (t1.id_tipo_propiedad_id = t2.id_tipo_propiedad)
    	            inner join backend_comuna t3
    	            on (t1.id_comuna_id = t3.id_comuna)
    	            inner join backend_region t4
    	            on (t3.id_region_id = t4.id_region)
                WHERE
                    t1.id_comuna_id = %s
                """, [id_comuna])

                if num_filas > 0 :
                    if num_filas > 1 :
                        resultados = cursor.fetchall()
                    else :
                        resultados = cursor.fetchone()
            except Exception as e :
                print(f"Error desconocido: {str(e)}")
        
        if resultados is not None :
            nombres_columnas = [desc[0] for desc in cursor.description]
            data = dict(zip(nombres_columnas, resultados))
            return (data)
        else :
            return HTTPStatus.NOT_FOUND

    def post_registrar_propiedad(r_vp, r_arriendo, r_venta, r_tpropiedad, r_idcomuna, r_mtotales, r_mutiles, r_cantdorm, r_cantbanos, r_mascotas, r_bodega, r_estacionamiento):
        try :
            tipo_propiedad = DAOPropiedad.get_tipo_propiedad(r_tpropiedad)
            comuna = DAOPropiedad.get_comuna(r_idcomuna)
            reg_propiedad = Propiedad(
                valor_propiedad = r_vp, 
                es_arriendo = r_arriendo, 
                es_venta = r_venta, 
                id_tipo_propiedad = tipo_propiedad, 
                id_comuna = comuna, 
                esta_habilitado = True)
            reg_propiedad.save()
            reg_caracteristicas = CaracteristicasPropiedad(
                id_propiedad_id = reg_propiedad.id_propiedad,
                metros_totales = r_mtotales, 
                metros_utiles = r_mutiles, 
                cant_dormitorios = r_cantdorm, 
                cant_banos = r_cantbanos, 
                permite_mascotas = r_mascotas, 
                tiene_bodega = r_bodega, 
                tiene_estacionamiento = r_estacionamiento)
            reg_caracteristicas.save()
        except Exception as e :
            print(f"Error desconocido: {str(e)}")
            return False
        return True