from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

## Materia: Automatizacion de Infraestructura II
## Profesor
## Alumno: Marvin Israel Jaramillo Garcia


# --- Contenido del CSS integrado ---
STYLES = """
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            color: #333;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }
        header {
            width: 100%;
            background-color: #2c3e50; /* Azul oscuro */
            color: white;
            padding: 30px 0;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        header h1 {
            margin: 0;
            font-size: 2.2em;
        }
        main {
            flex-grow: 1;
            padding: 40px 20px;
            width: 90%;
            max-width: 700px;
        }
        .card {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            padding: 30px;
            margin-bottom: 25px;
        }
        .card h2 {
            color: #3498db; /* Azul claro */
            border-bottom: 3px solid #ecf0f1;
            padding-bottom: 10px;
            margin-top: 0;
        }
        .card p {
            font-size: 1.1em;
            line-height: 1.6;
            margin: 15px 0;
        }
        .label {
            font-weight: bold;
            color: #2c3e50;
            display: inline-block;
            width: 120px;
        }
        .footer-links {
            text-align: center;
            margin-top: 20px;
        }
        .footer-links a {
            color: #3498db;
            text-decoration: none;
            font-weight: bold;
            padding: 10px 15px;
            border: 1px solid #3498db;
            border-radius: 5px;
            transition: background-color 0.3s, color 0.3s;
        }
        .footer-links a:hover {
            background-color: #3498db;
            color: white;
        }
        footer {
            width: 100%;
            background-color: #333;
            color: #aaa;
            text-align: center;
            padding: 15px 0;
            font-size: 0.9em;
        }
    </style>
"""

# --- Contenido del HTML integrado ---
# Usamos f-string para insertar el CSS y la sintaxis de Jinja2 ({{ }}) para las variables
HTML_TEMPLATE = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Información del Curso - Infraestructura II</title>
        {STYLES}
    </head>
    <body>
        <header>
            <h1>¡Bienvenido a la Automatización de Infraestructura!</h1>
        </header>

        <main>
            <div class="card">
                <h2>Datos del Curso</h2>
                <p><span class="label">Materia:</span> {{ Automatización de Infraestructura II }}</p>
                <p><span class="label">Profesor:</span> {{ Froylan Alonso Perez Alanis }}</p>
                <p><span class="label">Alumno:</span> {{ Marvin Israel Jaramillo Garcia }}</p>
            </div>
            
            <div class="footer-links">
                <a href="/health">Ver estado de salud (JSON)</a>
            </div>
        </main>

        <footer>
            <p>&copy; 2025 - {{ alumno }}</p>
        </footer>
    </body>
    </html>
"""

# ----------------------------------------------------------------------

## Rutas de la Aplicación

@app.route("/")
def home():
    """Renderiza la página principal usando la plantilla HTML integrada."""
    
    # Datos a pasar a la plantilla
    context = {
        "materia": "Automatización de Infraestructura II",
        "profesor": "Froylan Alonso Perez Alanis",
        "alumno": "Marvin Israel Jaramillo Garcia"
    }
    
    # Usamos render_template_string para procesar el string HTML
    return render_template_string(HTML_TEMPLATE, **context)

@app.route("/health")
def health():
    """Ruta para verificar el estado de salud de la aplicación (Health Check)."""
    return jsonify(status="ok")

# ----------------------------------------------------------------------

## Ejecución del Servidor

if __name__ == "__main__":
    # Obtiene el puerto del entorno o usa 5000 por defecto
    port = int(os.environ.get("PORT", 5000))
    
    # Ejecuta el servidor en 0.0.0.0 para ser accesible externamente
    app.run(host="0.0.0.0", port=port, debug=True)