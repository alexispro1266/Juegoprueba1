import webbrowser
import os

html_content = '''
<!DOCTYPE html>
<html>
<head>
    <title>Juego de Preguntas</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; padding: 40px; }
        .card { background: white; padding: 20px; max-width: 500px; margin: auto; border-radius: 10px; box-shadow: 0 0 10px #ccc; }
        .question { font-size: 20px; margin-bottom: 20px; }
        button { margin: 5px; padding: 10px 20px; font-size: 16px; }
        #result { margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <div class="question" id="question">¿Cuál es la capital de Francia?</div>
        <button onclick="checkAnswer('A')">A) Berlín</button>
        <button onclick="checkAnswer('B')">B) París</button>
        <button onclick="checkAnswer('C')">C) Madrid</button>
        <div id="result"></div>
    </div>

    <script>
        function checkAnswer(option) {
            const result = document.getElementById("result");
            if (option === 'B') {
                result.innerHTML = "¡Correcto! 🎉";
                result.style.color = "green";
            } else {
                result.innerHTML = "Incorrecto. Intenta otra vez.";
                result.style.color = "red";
            }
        }
    </script>
</body>
</html>
'''

# Guardar el contenido en un archivo HTML
file_path = os.path.abspath("juego.html")
with open(file_path, "w", encoding="utf-8") as file:
    file.write(html_content)

# Abrir en Google Chrome
chrome_path = webbrowser.get(using='windows-default')  # También puedes personalizar con la ruta completa
chrome_path.open(f"file://{file_path}")


'escribir: python juego.py'

