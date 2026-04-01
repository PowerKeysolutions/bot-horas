from flask import Flask, render_template, request, make_response
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Configuración de Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

def conectar():
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name('credenciales.json', scope)
        client = gspread.authorize(creds)
        return client.open("BOT HORAS").sheet1
    except Exception as e:
        print(f"ERROR DE CONEXION: {e}")
        return None

sheet = conectar()

@app.after_request
def add_header(response):
    # Esto obliga al navegador a no guardar NADA en memoria
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    if not sheet:
        return "Error: No hay conexión con el Excel."
    
    fila = [
        request.form.get('fecha'),
        request.form.get('nombre'),
        request.form.get('horas'),
        request.form.get('trabajo')
    ]
    
    try:
        sheet.append_row(fila)
        return "<h1>¡Datos guardados con éxito!</h1><a href='/'>Volver</a>"
    except Exception as e:
        return f"<h1>Error al guardar: {e}</h1>"

if __name__ == '__main__':
    print(">>> SERVIDOR INICIADO EN EL PUERTO 5555")
    app.run(debug=True, port=5555)