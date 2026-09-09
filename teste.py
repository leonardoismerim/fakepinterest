from fakepinterest import app, database
from fakepinterest.models import Foto

with app.app_context():
    # Para apagar TODAS as fotos:
    database.session.query(Foto).delete()
    
    # Ou para apagar uma foto específica pelo ID:
    # foto = Foto.query.get(id_da_foto)
    # database.session.delete(foto)
    
    database.session.commit()