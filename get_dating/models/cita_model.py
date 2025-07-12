from utils.db import get_connection

class CitaModel:
    @staticmethod
    def obtener_citas(cliente_email):
        conn, cursor = get_connection()
        cursor.execute("SELECT fecha, hora FROM citas WHERE cliente_email=?", (cliente_email,))
        citas = cursor.fetchall()
        return [{"fecha": cita[0], "hora": cita[1]} for cita in citas]
