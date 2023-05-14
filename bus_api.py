from flask import Flask, jsonify,request,json

app = Flask(__name__)

linhas = [
    {
        "codigo" : 202,
        "nome" : 'T.I Barro/T.I Macaxeira(VARZEA)',
        "tarifa" : 4.10,
        "ar-condicionado" : False
    },

    {
        "codigo" : 2060,
        "nome" : 'T.I Tancredo Neves/T.I Macaxeira',
        "tarifa" : 4.10,
        "ar-condicionado" : True
    },
]

cod_linha = []

for linha in linhas:
    cod_linha.append(linha['codigo'])

@app.route('/linha/<int:codigo>', methods = ['GET','DELETE','PUT'])
def linha(codigo):

    if request.method == 'GET':
        if codigo in cod_linha:
            pos = cod_linha.index(codigo)
            response = linhas[pos]
            return jsonify(response)
        else:
            return jsonify({'Status':'Linha não cadastrada!'})
        
    elif request.method == 'DELETE':
        if codigo in cod_linha:
            pos = cod_linha.index(codigo)
            linhas.pop(pos)
            return jsonify({'Status':'Linha removida com sucesso!'})
        else:
            return jsonify({'Status':'Linha não cadastrada!'})
        
    elif request.method == 'PUT':
        if codigo in cod_linha:
            pos = cod_linha.index(codigo)
            dados = json.loads(request.data)
            linhas[pos] = dados
            linhas[pos]['codigo'] = codigo
            return jsonify({'Status':'Linha alterada com sucesso'})
        else:
            return jsonify({'Status':'Linha não cadastrada!'})
    
@app.route('/linha',methods = ['GET','POST'])
def obter_linhas():
    if request.method == 'GET':
        return jsonify(linhas)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        cod_linha.append(dados['codigo'])
        linhas.append(dados)
        return jsonify({'Status':'Linha cadastrada com sucesso!'})
            
                
if __name__ == '__main__':
    app.run(debug=True)
            