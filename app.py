import io

from flask import Flask, render_template, request, make_response
import json
import docxtpl

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/cuestionario_covid')
def survey():
    return render_template('cuestionario_covid.html', nombre="Pablo")


@app.route('/guardar_respuestas', methods=['POST'])
def guardar_respuestas():
    respuestas = request.get_json()
    respuestas_json = json.dumps(respuestas, indent=2)
    f = open("respuestas/respuestas.json", "w")
    f.write(respuestas_json)
    f.close()
    return "OK"


@app.route('/generar_docx')
def generar_docx():
    ruta = "plantillas_docx/plantilla_covid.docx"
    doc = docxtpl.DocxTemplate(ruta)
    respuestas = json.load(open('respuestas/respuestas.json'))
    doc.render(respuestas)
    file_stream = io.BytesIO()
    doc.save(file_stream)
    file_stream.seek(0)
    response = make_response(file_stream)
    response.headers.set('Content-Type', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response.headers.set(
        'Content-Disposition', 'attachment', filename='informe_covid.docx')
    return response


if __name__ == '__main__':
    app.run()
