from app import app
from flask import render_template
from flask import request



@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/cadastro.html')
def cadastro():
    return render_template('cadastro.html')

@app.route('/finalizar.html')
def finalizar():
    return render_template('finalizar.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/autenticar',methods=['GET'])

        

@app.route('/pagamento')
def pagamento():
    return render_template('pagamento.html')

@app.route('/sair')
def sair():
    return render_template('sair.html')
    
@app.route('/sobre.html')
def sobre():
    return render_template('sobre.html')

    
@app.route('/endereco.html')
def endereco():
    return render_template('endereco.html')