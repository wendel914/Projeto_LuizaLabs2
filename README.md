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

### Consulta do Envio de Comunicação
- **URL:** `/agendamento/<id>`
- **Método:** `GET`
- Descrição: Consultar o status de um agendamento.
- Parâmetros:
  - id (integer): ID do agendamento.
- Resposta de Sucesso:
  - Código: 200 OK
  - **Conteúdo:** `Detalhes do agendamento (JSON).`
  ```bash  
  curl -X GET http://localhost:5000/agendamento/1

### Cancelamento do Envio de Comunicação
- **URL:** `/agendamento/<id>`
- **Método:** `DELETE`
- Descrição: Cancelar um agendamento.
- Parâmetros:
  - id (integer): ID do agendamento.
- Resposta de Sucesso:
  - Código: 200 OK
  - **Conteúdo:** `{"message": "Agendamento cancelado com sucesso!"}`
- Exemplo de Uso com cURL:
  ```bash
  curl -X DELETE http://localhost:5000/agendamento/1

### Instalação e Configuração

### Pré-requisitos

- Python 3.8+
- Docker 26.1.4+
- Docker Compose 1.29.2+

- Para executar este projeto localmente, siga estas etapas:

- 1. Clone o repositório:
  ```bash 
  git clone https://github.com/wendel914/Projeto_LuizaLabs2.git
  cd Projeto_LuizaLabs2

- 2. Instale as dependências:
Certifique-se de ter o Python e o pip instalados em seu sistema. Em seguida, instale as dependências do projeto executando:
  ```bash
  pip install -r requirements.txt

- 3. Configuração do Banco de Dados:
Antes de iniciar o servidor, certifique-se de configurar o banco de dados. Atualize a URI do banco de dados no arquivo app.py com suas credenciais e o nome do banco de dados desejado:
  ```bash
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://seu_usuario:senha@localhost/nome_do_banco'

- 4. Inicialize o Banco de Dados:
Execute o seguinte comando para criar as tabelas no banco de dados:
  ```bash
  python
  from app import db
  db.create_all()
  exit()

- 5. Inicie o Servidor:
Agora, você pode iniciar o servidor Flask executando:
  ```bash
  python app.py

- Após seguir essas etapas, o servidor estará em execução localmente em: 
   ```bash
  http://localhost:5000.


## Utilização do Docker Compose

Este projeto utiliza Docker Compose para facilitar a configuração do ambiente de desenvolvimento. Com o Docker Compose, você pode iniciar facilmente todos os serviços necessários para executar o projeto localmente.

### Pré-requisitos

- Docker: [Instalação do Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Instalação do Docker Compose](https://docs.docker.com/compose/install/)

### Como usar

1. Certifique-se de que o Docker e o Docker Compose estão instalados em sua máquina.
2. No terminal, navegue até o diretório do projeto.
3. Execute o seguinte comando para iniciar os serviços definidos no arquivo docker-compose.yml:

   ```bash
   docker-compose up -d

- Isso iniciará os serviços em segundo plano (modo detached).

4. Para parar e remover os serviços, execute o seguinte comando:
   ```bash
   docker-compose down

- Isso encerrará e removerá os contêineres definidos no arquivo docker-compose.yml.



