## 💻 Projeto STAR_WARS_CASE_POD

Repositório para case técnico da Power of Data.<br>
API capaz de gerar dados sobre o Star Wars a partir de parâmetros como:

- Character (personagem) 🌟👨‍🚀 👩‍🚀
- Planet (planeta) 🪐🌌
- Starship (espaçonave) 🚀🌟
- Film (filme) 🎬🌌

## 🛠️ Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/) - Linguagem de programação.
- [AWS S3](https://docs.aws.amazon.com/s3/?icmpid=docs_homepage_featuredsvcs) - Serviço de armazenamento de objetos escalável da Amazon.
- [AWS Lambda](https://docs.aws.amazon.com/lambda/?icmpid=docs_homepage_featuredsvcs) - Serviço serverless para execução de código.
- [AWS API Gateway](https://docs.aws.amazon.com/apigateway/?icmpid=docs_homepage_networking) - Gerenciador de APIs que facilita a criação e publicação .
- [SWAPI](https://swapi.dev/documentation) - API com dados do Star Wars.

## 📝 Conhecimentos extras aplicados
- Testes unitários 🧪
- Criação do CI/CD para automatização do processo de integração e entrega contínua🤖🔄

## 🚀 Como executar

Clone o projeto e acesse a pasta do mesmo.

```bash
$ git clone ...
```

Para iniciá-lo, siga os passos abaixo:

# Windows 10
```bash
# Instalando dependências do projeto
$ python -m venv venv
$ venv/scripts/activate
$ pip install -r requirements.txt

# Rodar o projeto
$ uvicorn app.main:app --reload
```
