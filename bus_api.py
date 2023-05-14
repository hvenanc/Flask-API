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

@app.route('/linha/<int:codigo>', methods = ['GET'])
def linha(codigo):

    cod_linha = []

    for linha in linhas:
        cod_linha.append(linha['codigo'])

    if codigo in cod_linha:
        pos = cod_linha.index(codigo)
        response = linhas[pos]
        return jsonify(response)
    else:
        return jsonify({'Status':'Linha não cadastrada!'})
    
@app.route('/linhas',methods = ['GET'])
def obter_linhas():
    return jsonify(linhas)
            
                
if __name__ == '__main__':
    app.run(debug=True)
            