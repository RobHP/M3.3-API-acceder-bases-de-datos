from flask import Flask, jsonify
import mysql.connector
import json

app = Flask(__name__)

# Cargar configuración desde el archivo config.json
with open('config.json', 'r') as f:
    config = json.load(f)

# Configuración de la conexión a MySQL
conexion = mysql.connector.connect(**config['mysql'])

# Ruta para obtener registros de la tabla "curso"
@app.route('/curso', methods=['GET'])
def obtener_registros_curso():
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM curso")
        registros = cursor.fetchall()
        cursor.close()
        return jsonify(registros), 200
    except mysql.connector.Error as error:
        return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    app.run(debug=config['api']['debug'], port=config['api']['port'])
