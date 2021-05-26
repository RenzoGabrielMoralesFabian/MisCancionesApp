from src.miscancionesapp.modelo.album import Album, Medio
from src.miscancionesapp.modelo.cancion import Cancion
from src.miscancionesapp.modelo.interprete import Interprete
from src.miscancionesapp.modelo.declarative_base import engine, Base, session

class Coleccion():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_album(self, titulo, anio, descripcion, medio):
        busqueda = session.query(Album).filter(Album.titulo == titulo).all()
        if len(busqueda) == 0:
            album = Album(titulo=titulo, ano=anio, descripcion=descripcion, medio=medio)
            session.add(album)
            session.commit()
            return True
        else:
            return False

    def editar_album(self, album_id, titulo, anio, descripcion, medio):
        busqueda = session.query(Album).filter(Album.titulo == titulo, Album.id != album_id).all()
        if len(busqueda) == 0:
            album = session.query(Album).filter(Album.id == album_id).first()
            album.titulo = titulo
            album.ano = anio
            album.descripcion = descripcion
            album.medio = medio
            session.commit()
            return True
        else:
            return False

    def dar_album_por_id(self, album_id):
        return session.query(Album).get(album_id).__dict__

    def agregar_cancion(self, titulo, minutos, segundos, compositor) :
        busqueda = session.query(Cancion).filter(Cancion.titulo == titulo).all()
        if len(busqueda) == 0:
            cancion = Cancion(titulo=titulo, minutos=minutos, segundos=segundos, compositor=compositor)
            session.add(cancion)
            session.commit()
            return True
        else:
            return False

    def editar_cancion (self, cancion_id, titulo, minutos, segundos, compositor) :
        busqueda = session.query (Cancion).filter (Cancion.titulo == titulo, Cancion.id != cancion_id).all ( )
        if len (busqueda) == 0 :
            cancion = session.query (Cancion).filter (Cancion.id == cancion_id).first ( )
            cancion.titulo = titulo
            cancion.minutos = minutos
            cancion.segundos = segundos
            cancion.segundos = compositor
            session.commit ( )
            return True
        else :
            return False