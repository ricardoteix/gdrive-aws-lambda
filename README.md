[<img src="https://em-content.zobj.net/thumbs/120/openmoji/338/flag-united-states_1f1fa-1f1f8.png" alt="us flag" width="48"/>](./README_en.md)

# 📂 GDrive Upload - Lambda com Serverless

Este projeto implementa uma função AWS Lambda em Python, utilizando o Serverless Framework, que permite o **upload de arquivos para o Google Drive**. A função é exposta publicamente via **Lambda Function URL** e autentica com o Google usando credenciais de serviço.

O projeto tem um objetivo **puramente educacional**, não sendo a melhor opção para um projeto real em ambiente produtivo.

---

## ⚙️ Tecnologias Utilizadas

- 🐍 Python 3.12
- ☁️ AWS Lambda
- 🧩 Serverless Framework
- 📁 Google Drive API
- 🔐 Google Service Account
- 🔄 Lambda Function URL (sem API Gateway)

---

## 🚀 Funcionalidades

- Upload de arquivos de até 6MB*
- Autenticação simples via header (`passwd`)
- Upload direto para uma pasta específica no Google Drive
- Retorno com mensagem de sucesso ou erro

* Para este exemplo temos a limitação de 6291456 bytes (6 MB) para a solicitação.

---

## 📦 Requisitos

- Node.js (v16+)
- Python 3.12
- AWS CLI configurado (`aws configure`)
- Conta e projeto no Google Cloud com Google Drive API ativada
- Chave de serviço (JSON)

---

## 📄 .env

Este projeto utiliza um arquivo `.env` para manter variáveis sensíveis fora do controle de versão. O arquivo **`.env.template`** está incluído como referência.

### Exemplo de `.env.template`

```env
GOOGLE_FOLDER_ID=SEU_ID_DA_PASTA_NO_DRIVE
GOOGLE_CREDENTIALS=voce-gdrive-integration-b1234567890.json
PASSWORD=4321
````

> ⚠️ Copie `.env.template` para `.env` e preencha com seus valores reais antes de fazer o deploy.

---

## 🛠️ Instalação

Prepare o ambiente

```bash
# Clone o repositório e use um ambiente virtual do python para isolar suas depedências. 
python -m venv env

# Instale dependências Python localmente
pip install -r requirements.txt

# Instale as dependências do projeto com node
npm install
```

---

## 🚀 Deploy

Cerfifique-se de ter o serverless framework funcionando e autenticado.

```bash

# Deploy para a AWS (ambiente padrão: dev)
serverless deploy

# Ou deploy para outro ambiente
serverless deploy --stage prod
```

Após o deploy, o Serverless irá exibir a **URL pública da Lambda** que poderá ser usada para fazer uploads.

---


## 🧪 Testando

Após o deploy, será apresentado algo como apresentado abaixo.

Acesse o endpoint e realize o upload. Faça testes com arquivos pequenos, menores que 4MB.

```
✔ Service deployed to stack gdrive-upload-prod (50s)

endpoint: https://l6m5i65g3clkg23t6uivezelvy0fqekg.lambda-url.us-east-1.on.aws/
functions:
  gdrive-upload: gdrive-upload-prod (19 MB)
```

---

## 🔐 Segurança

* Nunca compartilhe o `.env` ou arquivos `.json` de credenciais.
* Considere armazenar as credenciais no AWS SSM ou Secrets Manager para produção.
* A autenticação atual (`passwd: 4321`) é apenas um placeholder e deve ser substituída por algo mais seguro e está especificado no `.env` como `PASSWORD`.
