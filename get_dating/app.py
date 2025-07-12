from flask import Flask
from flask_cors import CORS
from routes.agendar_cita_routes import agendar_cita_bp
from routes.ver_citas_routes import ver_citas_bp  

app = Flask(__name__)
CORS(app)

# Registrar los blueprints
app.register_blueprint(agendar_cita_bp)  # Rutas de agendar cita
app.register_blueprint(ver_citas_bp)  # Nuevas rutas de ver citas

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
