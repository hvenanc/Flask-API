from flask import Flask, jsonify,json,request

app = Flask(__name__)

@app.route('/soma', methods = ['POST'])
def soma():
    dados = json.loads(request.data)
    lista = list(dados['valores'])
    total = sum(lista)
    return jsonify({'soma': total})

@app.route('/media', methods=['POST'])
def media():
    dados = json.loads(request.data)
    lista = list(dados['valores'])
    total = sum(lista)/len(lista)
    return jsonify({'Media': total})

@app.route('/aluno/<int:matricula>/<nome>',methods = ['GET'])
def aluno(matricula,nome):
    return jsonify({'matricula': matricula, 'nome': nome})

if __name__ == '__main__':
    app.run(debug=True)
