# Datapool - Exemplos de uso

Este projeto contém exemplos de uso do Datapool, tais como:

- Insereção de um item único
- Insereção de múltiplos itens
- Consumo de um item único
- Consumo de múltiplos itens

São estruturas básicas para o entendimento do uso do Datapool.

## Para executar localmente
### Requisitos

Para rodar este projeto, você precisará dos seguintes itens:

- Python 3.7 ou Superior
- [Conta na BotCity](https://developers.botcity.dev/)
    - Server:
        - `https://developers.botcity.dev`
    - Login:
        - [`**encontra em Amb. de Desenvolvedor**`](https://developers.botcity.dev/dev)
    - Key:
        - [`**encontra em Amb. de Desenvolvedor**`](https://developers.botcity.dev/dev)
- [Datapool criado no Orquestrador BotCity](https://documentation.botcity.dev/pt/maestro/features/datapool/#criando-um-datapool)
    - Status:
        - `Ativo`
    - Política de consumo:
        - `FIFO`
    - Gatilho:
        - `Nunca`
    - Schema:
        - `nome` (string)
        - `status` (string)
    - (restante dos campos preenchidos conforme quiser)
- ID de uma tarefa criada, com status `Aguardando`

### Crie e ative um ambiente virtual

   Para garantir que as dependências do projeto sejam isoladas de outros projetos Python, é recomendado usar um ambiente virtual.

   - No macOS/Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - No Windows:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

### Instalação de Dependências

Instale as dependências do projeto com o seguinte comando:

```bash
python -m pip install -r requirements.txt
```

### Executa o arquivo principal

```bash
python bot.py
```
