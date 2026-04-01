from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Conexión con Google
def conectar():
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credenciales.json', scope)
        client = gspread.authorize(creds)
        return client.open("BOT HORAS").sheet1
    except Exception as e:
        print(f"Error: {e}")
        return None

# Conectamos una vez al iniciar
sheet = conectar()

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    # 1. Recogemos los datos del formulario (incluido cliente)
    nombre = request.form.get('nombre')
    fecha = request.form.get('fecha')
    horas = request.form.get('horas')
    trabajo = request.form.get('trabajo')
    cliente = request.form.get('cliente') # <--- NUEVO

    try:
        # 2. Los enviamos al Excel en orden: Fecha, Nombre, Horas, Trabajo, Cliente
        # Esto rellena las columnas A, B, C, D y E
        sheet.append_row([fecha, nombre, horas, trabajo, cliente])
        return "<h1>✅ ¡Datos guardados!</h1><br><a href='/'>Hacer otro registro</a>"
    except Exception as e:
        return f"<h1>❌ Error al guardar: {e}</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=4321)