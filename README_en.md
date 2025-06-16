[<img src="https://em-content.zobj.net/thumbs/160/openmoji/338/flag-brazil_1f1e7-1f1f7.png" alt="us flag" width="48"/>](./README.md)

# 📂 GDrive Upload - Lambda with Serverless

This project implements an AWS Lambda function in Python, using the Serverless Framework, that enables **file uploads to Google Drive**. The function is publicly exposed via a **Lambda Function URL** and authenticates with Google using a service account.

This project is intended for **educational purposes only** and is not suitable for production use as-is.

---

## ⚙️ Technologies Used

* 🐍 Python 3.12
* ☁️ AWS Lambda
* 🧩 Serverless Framework
* 📁 Google Drive API
* 🔐 Google Service Account
* 🔄 Lambda Function URL (without API Gateway)

---

## 🚀 Features

* Upload of files up to 6MB\*
* Simple header-based authentication (`passwd`)
* Direct upload to a specific folder in Google Drive
* Response with success or error message

\* This example has a limit of 6,291,456 bytes (6 MB) per request.

---

## 📦 Requirements

* Node.js (v16+)
* Python 3.12
* Configured AWS CLI (`aws configure`)
* Google Cloud account and project with Google Drive API enabled
* Service account key (JSON file)

---

## 📄 .env

This project uses a `.env` file to keep sensitive variables out of version control. The **`.env.template`** file is included as a reference.

### Example `.env.template`

```env
GOOGLE_FOLDER_ID=YOUR_GOOGLE_DRIVE_FOLDER_ID
GOOGLE_CREDENTIALS=your-gdrive-integration-b1234567890.json
PASSWORD=4321
```

> ⚠️ Copy `.env.template` to `.env` and fill it in with your actual values before deploying.

---

## 🛠️ Installation

Set up the environment:

```bash
# Clone the repository and use a Python virtual environment to isolate dependencies
python -m venv env

# Install Python dependencies locally
pip install -r requirements.txt

# Install project dependencies with Node.js
npm install
```

---

## 🚀 Deployment

Make sure the Serverless Framework is installed and authenticated.

```bash
# Deploy to AWS (default environment: dev)
serverless deploy

# Or deploy to another stage
serverless deploy --stage prod
```

After deployment, Serverless will display the **public Lambda URL**, which you can use to upload files.

---

## 🧪 Testing

After deploying, you'll see an output like this:

Access the endpoint and try uploading a file. Test with small files under 4MB.

```
✔ Service deployed to stack gdrive-upload-prod (50s)

endpoint: https://l6m5i65g3clkg23t6uivezelvy0fqekg.lambda-url.us-east-1.on.aws/
functions:
  gdrive-upload: gdrive-upload-prod (19 MB)
```

---

## 🔐 Security

* Never share the `.env` file or `.json` credential files.
* Consider storing credentials in AWS SSM or Secrets Manager for production.
* The current authentication (`passwd: 4321`) is a placeholder and should be replaced with a more secure method, defined in the `.env` as `PASSWORD`.
