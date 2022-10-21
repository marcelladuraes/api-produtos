from flask import Flask, request
app = Flask(__name__)
# http://127.0.0.1:5000/teste/1
@app.route('/teste/1', methods=['POST'])

# {
#   "estoque": [
#    {
#       "id": 1
#       "produto": "Sapato"
#       "preco": "R$:99,99"
#    },
#    {
#       "id": 2
#       "produto": "Bolsa"
#       "preco": "R$:103,89"
#    },
#    {
#       "id": 3
#       "produto": "Camisa"
#       "preco": "R$:49,98"
#    },
#    {
#       "id": 4
#       "produto": "Calça"
#       "preco": "R$:89,72"
#    },
#    {
#       "id": 5
#       "produto": "Blusa"
#       "preco": "R$:97,35"
#    }
# ]
# }

def teste_json():
    objeto_json = request.get_json()
    if objeto_json is not None:
        if 'id' in objeto_json:
            id = objeto_json['id']
        if 'produto' in objeto_json:
            produto = objeto_json['produto']
        if 'preco' in objeto_json:
            preco = objeto_json['preco']

        return '''
            ID: {}
            Produto: {}
            Preco: {}
            '''.format(id,produto,preco)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)