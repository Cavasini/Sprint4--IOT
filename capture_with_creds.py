import cv2
import os
import json
from getpass import getpass
 
FACES_DIR = "faces"
USERS_FILE = "users.json"
HAAR = "haarcascade_frontalface_default.xml"

os.makedirs(FACES_DIR, exist_ok=True)

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

def capture_images(person_name, n_images=20):
    person_dir = os.path.join(FACES_DIR, person_name)
    os.makedirs(person_dir, exist_ok=True)

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(HAAR)
    count = 0

    print(f"[i] Capturando para '{person_name}'. Pressione 'q' para sair cedo.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y+h, x:x+w]
            path = os.path.join(person_dir, f"{count}.jpg")
            cv2.imwrite(path, face_img)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, f"{count}/{n_images}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
            if count >= n_images:
                break

        cv2.imshow("Captura Faces - Press q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord("q") or count >= n_images:
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"[i] Capturadas {count} imagens para {person_name} em {person_dir}")

if __name__ == "__main__":
    users = load_users()
    name = input("Nome da pessoa (ex: Lana): ").strip()
    if not name:
        print("Nome inválido.")
        raise SystemExit

    capture_images(name, n_images=20)

    email = input("Email da pessoa: ").strip()
    senha = getpass("Senha (não aparecerá enquanto digita): ").strip()

    confirm = input(f"Salvar credenciais para {name}? (s/n): ").strip().lower()
    if confirm == "s":
        users[name] = {"email": email, "password": senha}
        save_users(users)
        print(f"[✓] Credenciais salvas em {USERS_FILE}")
    else:
        print("Não salvou as credenciais.")