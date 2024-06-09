# API de Agendamento de Comunicação

Esta é uma API para agendamento de envios de comunicação.

## Endpoints

### Agendamento de Envio de Comunicação

- **URL:** `/agendamento`
- **Método:** `POST`
- **Descrição:** Agendar um envio de comunicação.
- **Parâmetros:**
  - `data_hora` (string): Data e hora para o envio (formato: YYYY-MM-DD HH:MM:SS).
  - `destinatario` (string): Destinatário da mensagem.
  - `mensagem` (string): Mensagem a ser entregue.
  - `formato_comunicacao` (string): Formato da comunicação (email, sms, push, whatsapp).
- **Resposta de Sucesso:** 
  - **Código:** 201 Created
  - **Conteúdo:** `{"message": "Comunicação agendada com sucesso!"}`
- **Exemplo de Uso com cURL:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"data_hora":"2024-06-10 09:00:00","destinatario":"exemplo@gmail.com","mensagem":"Olá, mundo!","formato_comunicacao":"email"}' http://localhost:5000/agendamento
Consulta do Envio de Comunicação e Cancelamento
URL: /agendamento/<id>
Método:
GET: Consultar o status de um agendamento.
DELETE: Cancelar um agendamento.
Descrição: Consultar o status de um agendamento ou cancelar um agendamento.
Parâmetros:
id (integer): ID do agendamento.
Resposta de Sucesso (Consulta):
Código: 200 OK
Conteúdo: Detalhes do agendamento (JSON).
Resposta de Sucesso (Cancelamento):
Código: 200 OK
Conteúdo: {"message": "Agendamento cancelado com sucesso!"}
Exemplo de Uso com cURL (Consulta):
curl -X GET http://localhost:5000/agendamento/1
Exemplo de Uso com cURL (Cancelamento):
curl -X DELETE http://localhost:5000/agendamento/1

Instalação
Clone o repositório:
git clone https://github.com/wendel914/Projeto_LuizaLabs2.git
cd Projeto_LuizaLabs2




