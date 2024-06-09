from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# Configuração do Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/dbluiza'  # URI do banco de dados
db = SQLAlchemy(app)  # Objeto de conexão com o banco de dados
ma = Marshmallow(app)  # Objeto para serialização/desserialização de dados

# Modelo de dados para agendamento
class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime)
    destinatario = db.Column(db.String(255))
    mensagem = db.Column(db.Text)
    formato_comunicacao = db.Column(db.String(20))
    status = db.Column(db.String(20))

# Schema para serialização do modelo de dados
class AgendamentoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Agendamento
        load_instance = True

# Rota para agendamento de envio de comunicação
@app.route('/agendamento', methods=['POST'])
def agendar_comunicacao():
    """
    Endpoint para agendar o envio de comunicação.

    Recebe uma solicitação JSON com os campos necessários:
    - data_hora: Data e hora para o envio
    - destinatario: Destinatário da mensagem
    - mensagem: Mensagem a ser entregue
    - formato_comunicacao: Formato da comunicação (email, sms, push, whatsapp)

    Retorna uma mensagem de sucesso após agendar a comunicação.
    """
    data = request.json
    novo_agendamento = Agendamento(
        data_hora=data['data_hora'],
        destinatario=data['destinatario'],
        mensagem=data['mensagem'],
        formato_comunicacao=data['formato_comunicacao'],
        status='Pendente'
    )
    db.session.add(novo_agendamento)
    db.session.commit()
    return jsonify({"message": "Comunicação agendada com sucesso!"}), 201

# Rota para consultar o status do agendamento de envio de comunicação
@app.route('/agendamento/<int:id>', methods=['GET'])
def consultar_agendamento(id):
    """
    Endpoint para consultar o status do agendamento de envio de comunicação.

    Recebe o ID do agendamento como parâmetro na URL.

    Retorna os detalhes do agendamento correspondente.
    """
    agendamento = Agendamento.query.get_or_404(id)
    agendamento_schema = AgendamentoSchema()
    return jsonify(agendamento_schema.dump(agendamento)), 200

# Rota para cancelar um agendamento de envio de comunicação
@app.route('/agendamento/<int:id>', methods=['DELETE'])
def cancelar_agendamento(id):
    """
    Endpoint para cancelar um agendamento de envio de comunicação.

    Recebe o ID do agendamento como parâmetro na URL.

    Retorna uma mensagem de sucesso após cancelar o agendamento.
    """
    agendamento = Agendamento.query.get_or_404(id)
    db.session.delete(agendamento)
    db.session.commit()
    return jsonify({"message": "Agendamento cancelado com sucesso!"}), 200

if __name__ == "__main__":
    app.run(debug=True)  # Inicia o servidor Flask em modo de depuração
