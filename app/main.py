from flask import Flask, request
app = Flask(__name__)
produtos = [
    {
       "id": 1,
       "produto": "Sapato",
       "preco": "R$:99,99"
    },
    {
       "id": 2,
       "produto": "Bolsa",
       "preco": "R$:103,89"
    },
    {
       "id": 3,
       "produto": "Camisa",
       "preco": "R$:49,98"
    },
    {
       "id": 4,
       "produto": "Calça",
       "preco": "R$:89,72"
    },
    {
       "id": 5,
       "produto": "Blusa",
       "preco": "R$:97,35"
    }]
# http://127.0.0.1:5000/teste/1
@app.route('/teste/1', methods=['GET'])
def teste_json():
    id = -1
    objeto_json = request.get_json()
    if objeto_json is not None:
        if 'id' in objeto_json:
            id = objeto_json['id']
    resp = {'produto': '', 'preco': None} 
    for produto in produtos: 
        if produto['id'] == id: 
            resp = produto

    return '''
            ID: {}
            Produto: {}
            Preco: {}
            '''.format(resp['id'],resp['produto'],resp['preco'])

if __name__ == '__main__':
    app.run(debug = True, port = 5000)