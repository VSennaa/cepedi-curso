# Trabalho – Curso CEPEDI

## Usage 

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/VSennaa/cepedi-curso.git
cd cepedi-curso/escola
```

---

### 2️⃣ Criar e Ativar Ambiente Virtual

Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
---

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Aplicar Migrações do Banco de Dados

```bash
python manage.py migrate
```

---

### 5️⃣ Criar Superusuário

```bash
python manage.py createsuperuser
```

O terminal irá solicitar:

- Username
- Email (opcional)
- Password
- Confirmação da senha

Após finalizar, o usuário administrador estará criado.

---

### 6️⃣ Executar o Servidor

```bash
python manage.py runserver
```

O sistema estará disponível em:

```
http://127.0.0.1:8000
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/01299b26-7950-49df-8c7d-3b44782ab28c" width="32%" />
  <img src="https://github.com/user-attachments/assets/20a199e0-68c2-43aa-9cbb-e7cec899e34e" width="32%" />
  <img src="https://github.com/user-attachments/assets/66834d59-1cf2-4d59-8918-f56bcc696705" width="32%" />
</p>
---
