from flask import Flask, request, send_from_directory
import teste11 as t
import VB10 as vb

app = Flask("TesteForm")

@app.route("/")
def Home():
    return send_from_directory("","Home.html")

@app.route("/index")
def Index():
    return send_from_directory("",'Index2.html')
    
@app.route("/home")
def Home2():
    return send_from_directory("","Home.html")

@app.route("/preview")
def Preview():
    return send_from_directory("",'Preview.html')

@app.route("/frame")
def Frame():

    res = open("Resolucao.txt", "r")
    freq = open("Frequencia.txt", "r")
    tam = open("Tamanho.txt", "r")
    estilo = open("Estilo.txt", "r")

    vb.Comunicacao(estilo.read(), 'imagem.png', int(freq.read()), int(res.read()), tam.read(), 1)

    return send_from_directory("",'Preview.html')

@app.route("/desenhar")
def Desenhar():

    res = open("Resolucao.txt", "r")
    freq = open("Frequencia.txt", "r")
    tam = open("Tamanho.txt", "r")
    estilo = open("Estilo.txt", "r")

    vb.Comunicacao(estilo.read(), 'imagem.png', int(freq.read()), int(res.read()), tam.read(), 0)

    return send_from_directory("",'Preview.html')

@app.route("/FormAction", methods=['POST'])
def hello_world():
    
    print('')
    print('Frequencia:', request.form["freq"])
    print('Resolucao: ', request.form["res"])
    print('Tamanho:   ', request.form["tamanho"])
    print('Estilo:    ', request.form["estilo"])

    with open('Frequencia.txt', 'w') as f:
        f.write(request.form["freq"])
    with open('Resolucao.txt', 'w') as f:
        f.write(request.form["res"])
    with open('Tamanho.txt', 'w') as f:
        f.write(request.form["tamanho"])
    with open('Estilo.txt', 'w') as f:
        f.write(request.form["estilo"])

    f = request.files["file"]
    f.save('imagem.png')
    
    t.Estilo(request.form["estilo"], 'imagem.png', int(request.form["freq"]), int(request.form["res"]), request.form["tamanho"])

    return send_from_directory("","Preview.html")
