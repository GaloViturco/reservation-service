from flask import Blueprint
from controllers.agendar_cita_controller import agendar_cita
from controllers.ver_citas_controller import ver_citas  # Nuevo controlador

agendar_cita_bp = Blueprint('agendar_cita_bp', __name__)

@agendar_cita_bp.route('/agendar-cita', methods=['POST'])
def agendar():
    return agendar_cita()

@agendar_cita_bp.route('/view-appointments', methods=['GET'])
def view_appointments():
    return ver_citas()  # Nuevo endpoint para ver las citas
