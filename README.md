Face Login Automático com Reconhecimento Facial

Julia Amorim - RM99609

Lana Leite - RM551143

Matheus Cavasini - RM97722
Este projeto permite que um usuário seja reconhecido pela câmera, e, ao ser identificado, o sistema abre automaticamente o site de login e preenche os campos de e-mail e senha, clicando em "Entrar" — tudo isso sem interação manual.

Estrutura do Projeto
FaceLogin/
├── faces/                     # Fotos dos rostos de cada usuário (armazenadas por nome)
├── capture\_with\_creds.py      # Captura imagens da webcam e associa a um e-mail/senha
├── recognize\_and\_login.py     # Faz o reconhecimento e preenche o login no site
└── README.md                  # Este arquivo



Passo a Passo para Rodar1. Clonar o repositório

git clone https://github.com/seuusuario/FaceLogin.git
cd FaceLogin



2. Instalar dependências
   pip install -r requirements.txt

Se ocorrer erro de permissão, tente:
pip install --user -r requirements.txt

O arquivo requirements.txt deve conter as bibliotecas necessárias:



opencv-python



selenium



numpy



pandas













3. Capturar as imagens faciais
   Execute o script para cadastrar um novo usuário:
   python capture\_with\_creds.py

O sistema vai pedir:



Nome do usuário (ex: “Lana”)



E-mail



Senha



A webcam será ativada e capturará várias imagens (pressione “q” para encerrar).
As imagens serão salvas automaticamente na pasta faces/ e associadas às credenciais do usuário.

4. Rodar o reconhecimento e login automático
   Execute o script principal:
   python recognize\_and\_login.py

Quando o rosto for reconhecido:



O navegador será aberto no site:
https://v0-investimento-perfil.vercel.app/login



Os campos de e-mail e senha serão preenchidos automaticamente.



O botão “Entrar” será clicado.



O programa encerra o reconhecimento, mas o navegador permanece aberto para uso normal.



Explicação Técnica
O projeto utiliza OpenCV para capturar e analisar as imagens e LBPHFaceRecognizer para reconhecer os rostos.
Cada usuário tem seu conjunto de imagens salvas na pasta faces/ e suas credenciais associadas.
Durante a execução do recognize\_and\_login.py:



A câmera é iniciada.



O rosto capturado é comparado com o modelo treinado das imagens em faces/.



Quando há correspondência:



O navegador é aberto via Selenium.



Os campos de email e senha são preenchidos automaticamente.



O botão Entrar é clicado.



O reconhecimento é interrompido após o login bem-sucedido.





Esse comportamento garante segurança e conveniência, simulando um acesso facial inteligente vinculado às credenciais armazenadas localmente.

Requisitos



Python 3.9 ou superior



Webcam funcional



Google Chrome e ChromeDriver compatível



Bibliotecas necessárias:



opencv-python



selenium



numpy



pandas



Observação
Esse projeto está adaptado para Python 3.13 usando apenas OpenCV + LBPHFaceRecognizer, sem dependências externas complexas como dlib ou face\_recognition.Face Login Automático com Reconhecimento Facial
Este projeto permite que um usuário seja reconhecido pela câmera, e, ao ser identificado, o sistema abre automaticamente o site de login e preenche os campos de e-mail e senha, clicando em "Entrar" — tudo isso sem interação manual.

Estrutura do Projeto
FaceLogin/
├── faces/                     # Fotos dos rostos de cada usuário (armazenadas por nome)
├── capture\_with\_creds.py      # Captura imagens da webcam e associa a um e-mail/senha
├── recognize\_and\_login.py     # Faz o reconhecimento e preenche o login no site
└── README.md                  # Este arquivo



Passo a Passo para Rodar1. Clonar o repositório

git clone https://github.com/seuusuario/FaceLogin.git
cd FaceLogin













2. Instalar dependências
   pip install -r requirements.txt

Se ocorrer erro de permissão, tente:
pip install --user -r requirements.txt

O arquivo requirements.txt deve conter as bibliotecas necessárias:



opencv-python



selenium



numpy



pandas



3. Capturar as imagens faciais
   Execute o script para cadastrar um novo usuário:
   python capture\_with\_creds.py

O sistema vai pedir:



Nome do usuário (ex: “Lana”)



E-mail



Senha



A webcam será ativada e capturará várias imagens (pressione “q” para encerrar).
As imagens serão salvas automaticamente na pasta faces/ e associadas às credenciais do usuário.

4. Rodar o reconhecimento e login automático
   Execute o script principal:
   python recognize\_and\_login.py

Quando o rosto for reconhecido:



O navegador será aberto no site:
https://v0-investimento-perfil.vercel.app/login



Os campos de e-mail e senha serão preenchidos automaticamente.



O botão “Entrar” será clicado.



O programa encerra o reconhecimento, mas o navegador permanece aberto para uso normal.



Explicação Técnica
O projeto utiliza OpenCV para capturar e analisar as imagens e LBPHFaceRecognizer para reconhecer os rostos.
Cada usuário tem seu conjunto de imagens salvas na pasta faces/ e suas credenciais associadas.
Durante a execução do recognize\_and\_login.py:



A câmera é iniciada.



O rosto capturado é comparado com o modelo treinado das imagens em faces/.



Quando há correspondência:



O navegador é aberto via Selenium.



Os campos de email e senha são preenchidos automaticamente.



O botão Entrar é clicado.



O reconhecimento é interrompido após o login bem-sucedido.





Esse comportamento garante segurança e conveniência, simulando um acesso facial inteligente vinculado às credenciais armazenadas localmente.

Requisitos



Python 3.9 ou superior



Webcam funcional



Google Chrome e ChromeDriver compatível



Bibliotecas necessárias:



opencv-python



selenium



numpy



pandas



Observação
Esse projeto está adaptado para Python 3.13 usando apenas OpenCV + LBPHFaceRecognizer, sem dependências externas complexas como dlib ou face\_recognition.

