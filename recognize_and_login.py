import cv2
import os
import json
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
 
FACES_DIR = "faces"
USERS_FILE = "users.json"
HAAR = "haarcascade_frontalface_default.xml"
CONFIDENCE_THRESHOLD = 80
LOGIN_URL = "https://v0-investimento-perfil.vercel.app/login"

#Seletores de campos e botão
EMAIL_SELECTORS = ["input[name='email']", "input[type='email']"]
PASSWORD_SELECTORS = ["input[name='password']", "input[type='password']"]
SUBMIT_SELECTORS = ["button[type='submit']", "button"]

with open(USERS_FILE, "r", encoding="utf-8") as f:
    users = json.load(f)

#LBPH
recognizer = cv2.face.LBPHFaceRecognizer_create()
images, labels, label_map, curr = [], [], {}, 0
for person in sorted(os.listdir(FACES_DIR)):
    pdir = os.path.join(FACES_DIR, person)
    if not os.path.isdir(pdir):
        continue
    label_map[curr] = person
    for fname in sorted(os.listdir(pdir)):
        if fname.lower().endswith((".jpg", ".png", ".jpeg")):
            img = cv2.imread(os.path.join(pdir, fname), cv2.IMREAD_GRAYSCALE)
            if img is not None:
                images.append(img)
                labels.append(curr)
    curr += 1

recognizer.train(images, np.array(labels))
face_cascade = cv2.CascadeClassifier(HAAR)

#Abre navegador **detach** para não fechar
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get(LOGIN_URL)
time.sleep(1.5)  # espera carregar

#Loop de reconhecimento
cap = cv2.VideoCapture(0)
recognition_done = False  # flag para parar reconhecimento depois de logar

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        try:
            label, confidence = recognizer.predict(roi)
        except:
            label, confidence = None, 999

        if label is not None and confidence < CONFIDENCE_THRESHOLD:
            name = label_map.get(label, f"Pessoa_{label}")
            if users.get(name):
                print(f"[i] Reconheceu {name}. Preenchendo login...")
                # Preenche email e senha
                email_elem = None
                pwd_elem = None
                for sel in EMAIL_SELECTORS:
                    try: email_elem = driver.find_element(By.CSS_SELECTOR, sel); break
                    except: pass
                for sel in PASSWORD_SELECTORS:
                    try: pwd_elem = driver.find_element(By.CSS_SELECTOR, sel); break
                    except: pass
                if email_elem: email_elem.send_keys(users[name]["email"])
                if pwd_elem: pwd_elem.send_keys(users[name]["password"])
                # clica botão
                for sel in SUBMIT_SELECTORS:
                    try:
                        btn = driver.find_element(By.CSS_SELECTOR, sel)
                        btn.click()
                        break
                    except: pass
                recognition_done = True  # para de reconhecer
                break
        else:
            cv2.putText(frame, "Desconhecido", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("Reconhecimento -> AutoLogin", frame)
    if cv2.waitKey(1) & 0xFF == ord("q") or recognition_done:
        break

#para a câmera, mas mantém navegador aberto
cap.release()
cv2.destroyAllWindows()
print("[i] Reconhecimento finalizado, site aberto.")
