from backend.models import *
from django.db import connection
from http import HTTPStatus
from rest_framework import status
from backend.jsonresponse import JSONResponse

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
    
    def get_usuario (id):
        try :
            return Usuario.objects.get(id_usuario = id)
        except Usuario.DoesNotExist:
            raise None
        
    def get_estado (id):
        try:
            return Estados.objects.get(id_estado = id)
        except Estados.DoesNotExist:
            raise None

    def get_detalle_propiedades():
        resultados = []
        with connection.cursor() as cursor:
            try :
                cursor.execute("""
                SELECT
    	            COUNT(*)
                FROM
    	            MAESTRO_PROPIEDADES
                WHERE
                    esta_habilitado = 1
                    AND ultimo_estado = 2 
                    """)
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
    	            MAESTRO_PROPIEDADES t1 inner join MAESTRO_TIPO_PROPIEDAD t2
    	            on (t1.id_tipo_propiedad = t2.id_tipo_propiedad)
    	            inner join MAESTRO_COMUNAS t3
    	            on (t1.id_comuna = t3.id_comuna)
    	            inner join MAESTRO_REGIONES t4
    	            on (t3.id_region = t4.id_region)
                WHERE
                    t1.esta_habilitado = 1
                    AND t1.ultimo_estado = 2
                """)
                if num_filas > 0 :
                    if num_filas > 1 :
                        resultados = cursor.fetchall()
                    else :
                        resultados = cursor.fetchone()
                else :
                    return JSONResponse('No se han encontrado registros.')
            except Exception as e :
                print(f"Error desconocido: {str(e)}")
        data = []
        if num_filas == 1 :
            if resultados is not None :
                nombres_columnas = [desc[0] for desc in cursor.description]
                data = dict(zip(nombres_columnas, resultados))
                return (data)
            else :
                return HTTPStatus.NOT_FOUND
        elif num_filas > 1 :
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
                    cursor.execute("""
                    SELECT
	                    t1.id_propiedad id_propiedad,
	                    t1.valor_propiedad valor_propiedad,
	                    t1.es_arriendo es_arriendo,
	                    t1.es_venta es_venta,
	                    t2.nombre_tipo_propiedad nombre_tipo_propiedad,
	                    t3.metros_totales metros_totales,
	                    t3.metros_utiles metros_utiles,
	                    t3.cant_dormitorios cant_dormitorios,
	                    t3.cant_banos cant_banos,
	                    t3.permite_mascotas permite_mascotas,
	                    t3.tiene_bodega tiene_bodega,
	                    t3.tiene_estacionamiento tiene_estacionamiento,
	                    t4.nombre_comuna nombre_comuna,
	                    t5.nombre_region nombre_region
                    FROM
	                    MAESTRO_PROPIEDADES t1 inner join MAESTRO_TIPO_PROPIEDAD t2
	                    on (t1.id_tipo_propiedad = t2.id_tipo_propiedad)
	                    inner join MAESTRO_ASOC_CARACTERISTICAS_PROPIEDAD t3
	                    on (t1.id_propiedad = t3.id_propiedad)
	                    inner join MAESTRO_COMUNAS t4
	                    on (t1.id_comuna = t4.id_comuna)
	                    inner join MAESTRO_REGIONES t5
	                    on (t4.id_region = t5.id_region)
                    WHERE
                        t1.id_propiedad = %s
                        AND t1.esta_habilitado = 1
                        AND t1.ultimo_estado = 2
                    """, [id_propiedad])
                    result = cursor.fetchone()
                except :
                    return HTTPStatus.NOT_FOUND

            if result is not None:
                nombres_columnas = [desc[0] for desc in cursor.description]
                data = dict(zip(nombres_columnas, result))
                return (data)
            else :
                return HTTPStatus.NOT_FOUND

    def get_propiedades_filtradas (id_comuna, desde, hasta, arriendo, venta) :
        resultados = []
        with connection.cursor() as cursor:
            try :
                cursor.execute("""
                SELECT
    	            COUNT(*)
                FROM
    	            MAESTRO_PROPIEDADES
                WHERE
                    id_comuna = %s
                    AND valor_propiedad between %s and %s
                    AND es_arriendo = %s
                    AND es_venta = %s
                    AND esta_habilitado = 1
                    AND ultimo_estado = 2
                """, [id_comuna, desde, hasta, arriendo, venta])
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
    	            MAESTRO_PROPIEDADES t1 inner join MAESTRO_TIPO_PROPIEDAD t2
    	            on (t1.id_tipo_propiedad = t2.id_tipo_propiedad)
    	            inner join MAESTRO_COMUNAS t3
    	            on (t1.id_comuna = t3.id_comuna)
    	            inner join MAESTRO_REGIONES t4
    	            on (t3.id_region = t4.id_region)
                WHERE
                    t1.id_comuna = %s
                    AND t1.valor_propiedad between %s and %s
                    AND t1.es_arriendo = %s
                    AND t1.es_venta = %s
                    AND t1.esta_habilitado = 1
                    AND t1.ultimo_estado = 2
                """, [id_comuna, desde, hasta, arriendo, venta])
                if num_filas > 0 :
                    if num_filas > 1 :
                        resultados = cursor.fetchall()
                    else :
                        resultados = cursor.fetchone()
                else :
                    return JSONResponse('No se han encontrado registros.')
            except Exception as e :
                print(f"Error desconocido: {str(e)}")
        data = []
        if num_filas == 1 :
            if resultados is not None :
                nombres_columnas = [desc[0] for desc in cursor.description]
                data = dict(zip(nombres_columnas, resultados))
                return (data)
            else :
                return HTTPStatus.NOT_FOUND
        elif num_filas > 1 :
            if resultados is not None :
                for fila in resultados:
                    nombres_columnas = [desc[0] for desc in cursor.description]
                    item = dict(zip(nombres_columnas, fila))
                    data.append(item)
                return (data)
            else :
                return HTTPStatus.NOT_FOUND

    def post_registrar_propiedad(r_id_usuario, r_vp, r_arriendo, r_venta, r_tpropiedad, r_idcomuna, r_mtotales, r_mutiles, r_cantdorm, r_cantbanos, r_mascotas, r_bodega, r_estacionamiento):
        try :
            tipo_propiedad = DAOPropiedad.get_tipo_propiedad(r_tpropiedad)
            comuna = DAOPropiedad.get_comuna(r_idcomuna)
            usuario = DAOPropiedad.get_usuario(r_id_usuario)
            estado = DAOPropiedad.get_estado(1)
            reg_propiedad = Propiedad(
                valor_propiedad = r_vp, 
                es_arriendo = r_arriendo, 
                es_venta = r_venta, 
                id_tipo_propiedad = tipo_propiedad, 
                id_comuna = comuna,
                id_usuario = usuario,
                ultimo_estado = estado,
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
    
    def get_propiedades_pendientes(id_usuario):
        resultados = []
        with connection.cursor() as cursor:
            try :
                cursor.execute("""
                SELECT
	                COUNT(*)
                FROM
	                MAESTRO_PROPIEDADES
                WHERE
                    id_usuario = %s
                    AND esta_habilitado = 1
                    AND ultimo_estado = 1
                """, [id_usuario])
                count = cursor.fetchone()
                num_filas = count[0]
                cursor.execute("""
                SELECT
	                t1.id_propiedad id_propiedad,
	                t1.valor_propiedad valor_propiedad,
	                t1.es_arriendo es_arriendo,
	                t1.es_venta es_venta,
	                t2.nombre_tipo_propiedad nombre_tipo_propiedad,
	                t4.nombre_comuna nombre_comuna
                FROM
	                MAESTRO_PROPIEDADES t1 inner join MAESTRO_TIPO_PROPIEDAD t2
	                on (t1.id_tipo_propiedad = t2.id_tipo_propiedad)
	                inner join MAESTRO_ASOC_CARACTERISTICAS_PROPIEDAD t3
	                on (t1.id_propiedad = t3.id_propiedad)
	                inner join MAESTRO_COMUNAS t4
	                on (t1.id_comuna = t4.id_comuna)
	                inner join MAESTRO_REGIONES t5
	                on (t4.id_region = t5.id_region)
                WHERE
                    t1.id_usuario = %s
                    AND t1.esta_habilitado = 1
                    AND t1.ultimo_estado = 1
                """, [id_usuario])
                if num_filas > 0 :
                    if num_filas > 1 :
                        resultados = cursor.fetchall()
                    else :
                        resultados = cursor.fetchone()
                else :
                    return JSONResponse('No se han encontrado registros.')
            except Exception as e :
                print(f"Error desconocido: {str(e)}")
        data = []
        if num_filas == 1 :
            if resultados is not None :
                nombres_columnas = [desc[0] for desc in cursor.description]
                data = dict(zip(nombres_columnas, resultados))
                return (data)
            else :
                return HTTPStatus.NOT_FOUND
        elif num_filas > 1 :
            if resultados is not None :
                for fila in resultados:
                    nombres_columnas = [desc[0] for desc in cursor.description]
                    item = dict(zip(nombres_columnas, fila))
                    data.append(item)
                return (data)
            else :
                return HTTPStatus.NOT_FOUND

    def get_caracteristicas_propiedad_pendiente(id_usuario, id_propiedad):
        if id_propiedad is not None :
            with connection.cursor() as cursor:
                try :
                    cursor.execute("""
                    SELECT
	                    t1.id_propiedad id_propiedad,
	                    t1.valor_propiedad valor_propiedad,
	                    t1.es_arriendo es_arriendo,
	                    t1.es_venta es_venta,
	                    t2.nombre_tipo_propiedad nombre_tipo_propiedad,
	                    t3.metros_totales metros_totales,
	                    t3.metros_utiles metros_utiles,
	                    t3.cant_dormitorios cant_dormitorios,
	                    t3.cant_banos cant_banos,
	                    t3.permite_mascotas permite_mascotas,
	                    t3.tiene_bodega tiene_bodega,
	                    t3.tiene_estacionamiento tiene_estacionamiento,
	                    t4.nombre_comuna nombre_comuna,
	                    t5.nombre_region nombre_region
                    FROM
	                    MAESTRO_PROPIEDADES t1 inner join MAESTRO_TIPO_PROPIEDAD t2
	                    on (t1.id_tipo_propiedad = t2.id_tipo_propiedad)
	                    inner join MAESTRO_ASOC_CARACTERISTICAS_PROPIEDAD t3
	                    on (t1.id_propiedad = t3.id_propiedad)
	                    inner join MAESTRO_COMUNAS t4
	                    on (t1.id_comuna = t4.id_comuna)
	                    inner join MAESTRO_REGIONES t5
	                    on (t4.id_region = t5.id_region)
                    WHERE
                        t1.id_usuario = %s
                        AND t1.id_propiedad = %s
                        AND t1.ultimo_estado = 1
                    """, [id_usuario, id_propiedad])
                    result = cursor.fetchone()
                except :
                    return HTTPStatus.NOT_FOUND

            if result is not None:
                nombres_columnas = [desc[0] for desc in cursor.description]
                data = dict(zip(nombres_columnas, result))
                return (data)
            else :
                return HTTPStatus.NOT_FOUND

    def get_propiedades_validadas(id_usuario):
        resultados = []
        with connection.cursor() as cursor:
            try :
                cursor.execute("""
                SELECT
	                COUNT(*)
                FROM
	                MAESTRO_PROPIEDADES
                WHERE
                    id_usuario = %s
                    AND esta_habilitado = 1
                    AND ultimo_estado = 2
                """, [id_usuario])
                count = cursor.fetchone()
                num_filas = count[0]
                cursor.execute("""
                SELECT
	                t1.id_propiedad id_propiedad,
	                t1.valor_propiedad valor_propiedad,
	                t1.es_arriendo es_arriendo,
	                t1.es_venta es_venta,
	                t2.nombre_tipo_propiedad nombre_tipo_propiedad,
	                t4.nombre_comuna nombre_comuna
                FROM
	                MAESTRO_PROPIEDADES t1 inner join MAESTRO_TIPO_PROPIEDAD t2
	                on (t1.id_tipo_propiedad = t2.id_tipo_propiedad)
	                inner join MAESTRO_ASOC_CARACTERISTICAS_PROPIEDAD t3
	                on (t1.id_propiedad = t3.id_propiedad)
	                inner join MAESTRO_COMUNAS t4
	                on (t1.id_comuna = t4.id_comuna)
	                inner join MAESTRO_REGIONES t5
	                on (t4.id_region = t5.id_region)
                WHERE
                    t1.id_usuario = %s
                    AND t1.esta_habilitado = 1
                    AND t1.ultimo_estado = 2
                """, [id_usuario])
                if num_filas > 0 :
                    if num_filas > 1 :
                        resultados = cursor.fetchall()
                    else :
                        resultados = cursor.fetchone()
                else :
                    return JSONResponse('No se han encontrado registros.')
            except Exception as e :
                print(f"Error desconocido: {str(e)}")
        data = []
        if num_filas == 1 :
            if resultados is not None :
                nombres_columnas = [desc[0] for desc in cursor.description]
                data = dict(zip(nombres_columnas, resultados))
                return (data)
            else :
                return HTTPStatus.NOT_FOUND
        elif num_filas > 1 :
            if resultados is not None :
                for fila in resultados:
                    nombres_columnas = [desc[0] for desc in cursor.description]
                    item = dict(zip(nombres_columnas, fila))
                    data.append(item)
                return (data)
            else :
                return HTTPStatus.NOT_FOUND
            
    def get_caracteristicas_propiedad_validada(id_usuario, id_propiedad):
        if id_propiedad is not None :
            with connection.cursor() as cursor:
                try :
                    cursor.execute("""
                    SELECT
	                    t1.id_propiedad id_propiedad,
	                    t1.valor_propiedad valor_propiedad,
	                    t1.es_arriendo es_arriendo,
	                    t1.es_venta es_venta,
	                    t2.nombre_tipo_propiedad nombre_tipo_propiedad,
	                    t3.metros_totales metros_totales,
	                    t3.metros_utiles metros_utiles,
	                    t3.cant_dormitorios cant_dormitorios,
	                    t3.cant_banos cant_banos,
	                    t3.permite_mascotas permite_mascotas,
	                    t3.tiene_bodega tiene_bodega,
	                    t3.tiene_estacionamiento tiene_estacionamiento,
	                    t4.nombre_comuna nombre_comuna,
	                    t5.nombre_region nombre_region
                    FROM
	                    MAESTRO_PROPIEDADES t1 inner join MAESTRO_TIPO_PROPIEDAD t2
	                    on (t1.id_tipo_propiedad = t2.id_tipo_propiedad)
	                    inner join MAESTRO_ASOC_CARACTERISTICAS_PROPIEDAD t3
	                    on (t1.id_propiedad = t3.id_propiedad)
	                    inner join MAESTRO_COMUNAS t4
	                    on (t1.id_comuna = t4.id_comuna)
	                    inner join MAESTRO_REGIONES t5
	                    on (t4.id_region = t5.id_region)
                    WHERE
                        t1.id_usuario = %s
                        AND t1.id_propiedad = %s
                        AND t1.ultimo_estado = 2
                    """, [id_usuario, id_propiedad])
                    result = cursor.fetchone()
                except :
                    return HTTPStatus.NOT_FOUND

            if result is not None:
                nombres_columnas = [desc[0] for desc in cursor.description]
                data = dict(zip(nombres_columnas, result))
                return (data)
            else :
                return HTTPStatus.NOT_FOUND
    
    def get_propiedades_pendientes_administrador (id_usuario):
        usuario = Usuario.objects.get(id_usuario = id_usuario)
        perfil = PerfilesUsuario.objects.get(id_usuario = usuario.id_usuario)
        if perfil.id_perfil.id_perfil == 2 :
            return 5
        else :
            resultados = []
            with connection.cursor() as cursor:
                try :
                    cursor.execute("""
                    SELECT
	                    COUNT(*)
                    FROM
	                    MAESTRO_PROPIEDADES
                    WHERE
                        ultimo_estado = 1
                    """)
                    count = cursor.fetchone()
                    num_filas = count[0]
                    cursor.execute("""
                    SELECT
	                    t1.id_propiedad id_propiedad,
	                    t1.valor_propiedad valor_propiedad,
	                    t1.es_arriendo es_arriendo,
	                    t1.es_venta es_venta,
                        t7.descripcion_estado descripcion_estado,
	                    t2.nombre_tipo_propiedad nombre_tipo_propiedad,
	                    t3.metros_totales metros_totales,
	                    t3.metros_utiles metros_utiles,
	                    t3.cant_dormitorios cant_dormitorios,
	                    t3.cant_banos cant_banos,
	                    t3.permite_mascotas permite_mascotas,
	                    t3.tiene_bodega tiene_bodega,
	                    t3.tiene_estacionamiento tiene_estacionamiento,
	                    t4.nombre_comuna nombre_comuna,
	                    t5.nombre_region nombre_region,
                        upper(t6.primer_nombre|| ' ' ||t6.segundo_nombre||' ' ||t6.apellido_paterno||' '||t6.apellido_materno) nombre_usuario
                    FROM
	                    MAESTRO_PROPIEDADES t1 inner join MAESTRO_TIPO_PROPIEDAD t2
	                    on (t1.id_tipo_propiedad = t2.id_tipo_propiedad)
	                    inner join MAESTRO_ASOC_CARACTERISTICAS_PROPIEDAD t3
	                    on (t1.id_propiedad = t3.id_propiedad)
	                    inner join MAESTRO_COMUNAS t4
	                    on (t1.id_comuna = t4.id_comuna)
	                    inner join MAESTRO_REGIONES t5
	                    on (t4.id_region = t5.id_region)
                        inner join MAESTRO_USUARIOS t6
                        on (t1.id_usuario = t6.id_usuario)
                        inner join MAESTRO_ESTADOS t7
                        on (t1.ultimo_estado = t7.id_estado)
                    WHERE
                        t1.ultimo_estado = 1
                    """)
                    print
                    if num_filas > 0 :
                        if num_filas > 1 :
                            resultados = cursor.fetchall()
                        else :
                            resultados = cursor.fetchone()
                    else :
                        return JSONResponse('No se han encontrado registros.')
                except Exception as e :
                    print(f"Error desconocido: {str(e)}")
            data = []
            if num_filas == 1 :
                if resultados is not None :
                    nombres_columnas = [desc[0] for desc in cursor.description]
                    data = dict(zip(nombres_columnas, resultados))
                    return (data)
                else :
                    return JSONResponse(HTTPStatus.NOT_FOUND)
            elif num_filas > 1 :
                if resultados is not None :
                    for fila in resultados:
                        nombres_columnas = [desc[0] for desc in cursor.description]
                        item = dict(zip(nombres_columnas, fila))
                        data.append(item)
                    return (data)
                else :
                    return JSONResponse(HTTPStatus.NOT_FOUND)
        
    def get_propiedades_base_administrador (id_usuario) :
        usuario = Usuario.objects.get(id_usuario = id_usuario)
        perfil = PerfilesUsuario.objects.get(id_usuario = usuario.id_usuario)
        if perfil.id_perfil.id_perfil == 2 :
            return 5
        else :
            resultados = []
            with connection.cursor() as cursor:
                try :
                    cursor.execute("""
                    SELECT
	                    COUNT(*)
                    FROM
	                    MAESTRO_PROPIEDADES
                    WHERE
                        ultimo_estado IN (2,3)
                    """)
                    count = cursor.fetchone()
                    num_filas = count[0]
                    cursor.execute("""
                    SELECT
	                    t1.id_propiedad id_propiedad,
	                    t1.valor_propiedad valor_propiedad,
	                    t1.es_arriendo es_arriendo,
	                    t1.es_venta es_venta,
                        t7.descripcion_estado descripcion_estado,
	                    t2.nombre_tipo_propiedad nombre_tipo_propiedad,
	                    t3.metros_totales metros_totales,
	                    t3.metros_utiles metros_utiles,
	                    t3.cant_dormitorios cant_dormitorios,
	                    t3.cant_banos cant_banos,
	                    t3.permite_mascotas permite_mascotas,
	                    t3.tiene_bodega tiene_bodega,
	                    t3.tiene_estacionamiento tiene_estacionamiento,
	                    t4.nombre_comuna nombre_comuna,
	                    t5.nombre_region nombre_region,
                        upper(t6.primer_nombre|| ' ' ||t6.segundo_nombre||' ' ||t6.apellido_paterno||' '||t6.apellido_materno) nombre_usuario
                    FROM
	                    MAESTRO_PROPIEDADES t1 inner join MAESTRO_TIPO_PROPIEDAD t2
	                    on (t1.id_tipo_propiedad = t2.id_tipo_propiedad)
	                    inner join MAESTRO_ASOC_CARACTERISTICAS_PROPIEDAD t3
	                    on (t1.id_propiedad = t3.id_propiedad)
	                    inner join MAESTRO_COMUNAS t4
	                    on (t1.id_comuna = t4.id_comuna)
	                    inner join MAESTRO_REGIONES t5
	                    on (t4.id_region = t5.id_region)
                        inner join MAESTRO_USUARIOS t6
                        on (t1.id_usuario = t6.id_usuario)
                        inner join MAESTRO_ESTADOS t7
                        on (t1.ultimo_estado = t7.id_estado)
                    WHERE
                        t1.ultimo_estado IN (2,3)
                    ORDER BY
                        t1.id_propiedad
                    """)
                    print
                    if num_filas > 0 :
                        if num_filas > 1 :
                            resultados = cursor.fetchall()
                        else :
                            resultados = cursor.fetchone()
                    else :
                        return JSONResponse('No se han encontrado registros.')
                except Exception as e :
                    print(f"Error desconocido: {str(e)}")
            data = []
            if num_filas == 1 :
                if resultados is not None :
                    nombres_columnas = [desc[0] for desc in cursor.description]
                    data = dict(zip(nombres_columnas, resultados))
                    return (data)
                else :
                    return JSONResponse(HTTPStatus.NOT_FOUND)
            elif num_filas > 1 :
                if resultados is not None :
                    for fila in resultados:
                        nombres_columnas = [desc[0] for desc in cursor.description]
                        item = dict(zip(nombres_columnas, fila))
                        data.append(item)
                    return (data)
                else :
                    return JSONResponse(HTTPStatus.NOT_FOUND)

    def get_detalle_propiedad_administrador (id_usuario, id_propiedad) :
            usuario = Usuario.objects.get(id_usuario = id_usuario)
            perfil = PerfilesUsuario.objects.get(id_usuario = usuario.id_usuario)
            if perfil.id_perfil.id_perfil == 2 :
                return 5
            else :
                with connection.cursor() as cursor:
                    try :
                        cursor.execute("""
                        SELECT
    	                    t1.id_propiedad id_propiedad,
    	                    t1.valor_propiedad valor_propiedad,
    	                    t1.es_arriendo es_arriendo,
    	                    t1.es_venta es_venta,
                            t7.descripcion_estado descripcion_estado,
    	                    t2.nombre_tipo_propiedad nombre_tipo_propiedad,
    	                    t3.metros_totales metros_totales,
    	                    t3.metros_utiles metros_utiles,
    	                    t3.cant_dormitorios cant_dormitorios,
    	                    t3.cant_banos cant_banos,
    	                    t3.permite_mascotas permite_mascotas,
    	                    t3.tiene_bodega tiene_bodega,
    	                    t3.tiene_estacionamiento tiene_estacionamiento,
    	                    t4.nombre_comuna nombre_comuna,
    	                    t5.nombre_region nombre_region,
                            upper(t6.primer_nombre|| ' ' ||t6.segundo_nombre||' ' ||t6.apellido_paterno||' '||t6.apellido_materno) nombre_usuario
                        FROM
    	                    MAESTRO_PROPIEDADES t1 inner join MAESTRO_TIPO_PROPIEDAD t2
    	                    on (t1.id_tipo_propiedad = t2.id_tipo_propiedad)
    	                    inner join MAESTRO_ASOC_CARACTERISTICAS_PROPIEDAD t3
    	                    on (t1.id_propiedad = t3.id_propiedad)
    	                    inner join MAESTRO_COMUNAS t4
    	                    on (t1.id_comuna = t4.id_comuna)
    	                    inner join MAESTRO_REGIONES t5
    	                    on (t4.id_region = t5.id_region)
                            inner join MAESTRO_USUARIOS t6
                            on (t1.id_usuario = t6.id_usuario)
                            inner join MAESTRO_ESTADOS t7
                            on (t1.ultimo_estado = t7.id_estado)
                        AND
                            t1.id_propiedad = %s
                        """, [id_propiedad])
                        result = cursor.fetchone()
                    except :
                        return JSONResponse(HTTPStatus.NOT_FOUND)
                if result is not None:
                    nombres_columnas = [desc[0] for desc in cursor.description]
                    data = dict(zip(nombres_columnas, result))
                    return (data)
                else :
                    return JSONResponse(HTTPStatus.NOT_FOUND)

    def put_propiedad_admin (id_usuario, id_propiedad, ultimo_estado, observacion_denegacion) :
            usuario = Usuario.objects.get(id_usuario = id_usuario)
            perfil = PerfilesUsuario.objects.get(id_usuario = usuario.id_usuario)
            if perfil.id_perfil.id_perfil == 2 :
                return 0
            else :
                with connection.cursor() as cursor:
                    try :
                        cursor.execute("""
                        UPDATE
                            MAESTRO_PROPIEDADES
                        SET
                            ultimo_estado = %s,
                            observacion_denegacion = %s
                        WHERE
                            id_propiedad = %s
                        """, [ultimo_estado, observacion_denegacion, id_propiedad])
                        result = cursor.rowcount
                    except :
                        return 0
                if result > 0:
                    return 1
                else :
                    return 0