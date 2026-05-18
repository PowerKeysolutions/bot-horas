# bot-horas

Herramienta interna para que el equipo de **PowerKey** registre sus horas de trabajo directamente en Google Sheets desde cualquier dispositivo — sin instalar nada, solo abriendo un enlace.

---

## ¿Cómo funciona?

```
Técnico (móvil/PC)          Servidor local              Google Sheets
────────────────────         ──────────────────          ──────────────
Abre enlace ngrok     →      Flask :4321               → "BOT HORAS"
Rellena formulario    →      POST /registrar           → nueva fila
                             [fecha, nombre, horas,
                              trabajo, cliente]
```

El servidor corre en local y se expone al exterior con **ngrok** para que cualquier técnico pueda registrar desde su móvil o portátil sin estar en la misma red.

---

## Campos del formulario

| Campo | Descripción |
|-------|-------------|
| Fecha | Fecha del trabajo |
| Nombre | Técnico que registra |
| Horas | Horas trabajadas |
| Trabajo | Descripción de la tarea |
| Cliente | Cliente al que corresponde |

Los datos se añaden como nueva fila en la hoja de cálculo **"BOT HORAS"** de Google Drive.

---

## Requisitos

- Python 3.8+
- Cuenta de servicio Google Cloud con acceso a la hoja de cálculo
- ngrok instalado (para compartir externamente)

---

## Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/PowerKeysolutions/bot-horas.git
cd bot-horas

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Añadir credenciales de Google
# Descarga el JSON de tu cuenta de servicio Google Cloud
# y guárdalo como: credenciales.json (en la raíz del proyecto)
```

### Configurar la cuenta de servicio Google

1. Ir a [Google Cloud Console](https://console.cloud.google.com/)
2. Crear un proyecto → activar **Google Sheets API** y **Google Drive API**
3. Crear una **cuenta de servicio** → descargar el JSON → renombrarlo a `credenciales.json`
4. Compartir la hoja **"BOT HORAS"** con el email de la cuenta de servicio (editor)

---

## Uso

### Opción 1 — Script automático (Windows)

Doble clic en `iniciar_bot.bat`. Abre el servidor y ngrok automáticamente.

### Opción 2 — Manual

```bash
# Terminal 1 — iniciar servidor
python servidor_final.py
# → Running on http://127.0.0.1:4321

# Terminal 2 — exponer con ngrok
ngrok http 4321
# → Forwarding: https://xxxx.ngrok-free.app
```

Comparte el enlace `https://xxxx.ngrok-free.app` con el equipo. Funciona desde cualquier red.

---

## Estructura del proyecto

```
bot-horas/
├── servidor_final.py      # Servidor principal (Flask :4321)
├── app.py                 # Versión anterior (sin campo cliente)
├── templates/
│   └── formulario.html    # Formulario web
├── iniciar_bot.bat        # Script arranque automático (Windows)
├── requirements.txt       # Dependencias Python
└── credenciales.json      # ← NO subir a Git (está en .gitignore)
```

---

## Seguridad

- `credenciales.json` está en `.gitignore` — **nunca subir al repositorio**
- El enlace ngrok es temporal y cambia cada vez que se reinicia
- Para entornos de producción, considerar despliegue en servidor con HTTPS permanente

---

## Tecnologías

- [Flask](https://flask.palletsprojects.com/) — servidor web Python
- [gspread](https://docs.gspread.org/) — cliente Google Sheets
- [oauth2client](https://github.com/googleapis/oauth2client) — autenticación Google
- [ngrok](https://ngrok.com/) — túnel HTTP para acceso externo

---

*Desarrollado por [PowerKey](https://powerkey.es) para uso interno del equipo técnico.*
