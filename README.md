# 🤖 Face Login Automático com Reconhecimento Facial

![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-green.svg)
![Selenium](https://img.shields.io/badge/Selenium-success.svg)

> Este projeto permite que um usuário seja reconhecido pela câmera e, ao ser identificado, o sistema abre automaticamente um site, preenche os campos de e-mail e senha e clica em "Entrar" — tudo sem interação manual.

## 👥 Autores

* **Julia Amorim** - RM99609
* **Lana Leite** - RM551143
* **Matheus Cavasini** - RM97722

## ✨ Funcionalidades

* **Cadastro de Usuário:** Captura imagens da webcam e as associa a credenciais (e-mail/senha).
* **Reconhecimento Facial:** Utiliza o `LBPHFaceRecognizer` do OpenCV para identificar rostos conhecidos.
* **Login Automático:** Usa Selenium para abrir o Chrome, navegar até o site-alvo e preencher o formulário de login.

## 🛠️ Tecnologias Utilizadas

* **Python 3.9+**
* **OpenCV** (para captura e reconhecimento de imagem)
* **Selenium** (para automação web)
* **Numpy**
* **Pandas** (para gerenciamento de credenciais)

## 📁 Estrutura do Projeto

```bash
FaceLogin/
├── faces/                       # Fotos dos rostos de cada usuário (armazenadas por nome)
├── capture\_with\_creds.py      # Captura imagens da webcam e associa a um e-mail/senha
├── recognize\_and\_login.py     # Faz o reconhecimento e preenche o login no site
└── README.md                    # Este arquivo
```

## 🚀 Como Rodar

Siga este passo a passo para configurar e executar o projeto.

### 1. Pré-requisitos

Antes de começar, garanta que você tenha:

1.  **Python 3.9** ou superior.
2.  Uma **Webcam** funcional.
3.  **Google Chrome** instalado.
4.  **ChromeDriver** compatível com sua versão do Google Chrome.

> ⚠️ **Importante: Configurando o ChromeDriver**
>
> 1.  Verifique a versão do seu Google Chrome (vá em `chrome://settings/help`).
> 2.  Baixe o `ChromeDriver` correspondente à sua versão em: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
> 3.  **Extraia** o arquivo `.zip` e coloque o executável (`chromedriver.exe` no Windows ou `chromedriver` no Linux/Mac) **na mesma pasta** onde estão os scripts Python (`.py`) do projeto.

### 2. Clonar o Repositório

```bash
git clone [https://github.com/seuusuario/FaceLogin.git](https://github.com/seuusuario/FaceLogin.git)
cd FaceLogin
```

### 3. Instalar Dependências

```bash
Instalar dependências pip install -r requirements.txt
```

Se ocorrer erro de permissão, tente: pip install --user -r requirements.txt

O arquivo requirements.txt deve conter as bibliotecas necessárias:

```txt
opencv-python
selenium
numpy
pandas
```

### 4. Cadastrar Usuários (Captura Facial)

Execute o script de captura para cadastrar um novo usuário.

```bash
python capture_with_creds.py
```
O sistema solicitará no terminal:
```txt
- Nome do usuário (ex: "Lana")
- E-mail
- Senha
```

A webcam será ativada e capturará várias imagens **(pressione “q” para encerrar)**. As imagens serão salvas automaticamente na pasta faces/ e associadas às credenciais do usuário.

### 5. Executar o Login Automático

Execute o script principal de reconhecimento:

```bash
python recognize_and_login.py
```

Posicione seu rosto na frente da câmera. Quando você for reconhecido:
1. O navegador Google Chrome será aberto no site: https://v0-investimento-perfil.vercel.app/login.
2. Os campos de e-mail e senha serão preenchidos automaticamente.
3. O botão "Entrar" será clicado.

O script de reconhecimento será encerrado após o login bem-sucedido, mas o navegador permanecerá aberto para uso.


## ⚙️ Explicação Técnica

O projeto utiliza **OpenCV** para capturar e analisar as imagens e o `LBPHFaceRecognizer` (Local Binary Patterns Histograms) para treinar um modelo e reconhecer os rostos.

1.  **`capture_with_creds.py`**: Salva as fotos do usuário na pasta `faces/` e armazena as credenciais (e-mail, senha) associadas ao nome do usuário, provavelmente em um arquivo CSV ou JSON gerenciado pelo **Pandas**.
2.  **`recognize_and_login.py`**:
    * Inicia a câmera.
    * Treina o `LBPHFaceRecognizer` com todas as imagens da pasta `faces/`.
    * Compara o rosto detectado em tempo real com o modelo treinado.
    * Ao encontrar uma correspondência confiável, ele recupera as credenciais corretas.
    * Inicia o **Selenium** para abrir o Chrome, navegar até o site-alvo, injetar as credenciais nos campos do formulário e submetê-lo.

> ℹ️ **Observação**
>
> Este projeto está adaptado para Python 3.13 (e compatível com versões anteriores) usando apenas OpenCV + LBPHFaceRecognizer, sem dependências externas complexas como dlib ou face_recognition, tornando a instalação mais simples.





