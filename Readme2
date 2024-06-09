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
