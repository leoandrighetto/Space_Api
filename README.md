# Space A.P.I

Projeto full-stack com Vue 3 + Vuetify + Vue Router + Pinia no front-end e Flask + Flask-SQLAlchemy + JWT no back-end.

## Estrutura

- `frontend/` - Aplicacao Vue + Vuetify
- `backend/` - API Flask com rotas protegidas e proxy para APIs da NASA

## Funcionalidades

- Tela inicial com apresentacao do projeto e acesso rapido as rotas
- Autenticacao JWT (registro e login)
- Rotas protegidas consumindo imagens espaciais:
  - APOD (Astronomy Picture of the Day)
  - EPIC (Earth Polychromatic Imaging Camera)
  - Mars Rover Photos

## Como rodar

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

Servidor padrao em `http://localhost:5000`.

### Frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

Front-end em `http://localhost:5173`.

## Variaveis de ambiente

Backend (`backend/.env`):

- `SECRET_KEY`
- `JWT_SECRET_KEY`
- `DATABASE_URL`
- `NASA_API_KEY` (use `DEMO_KEY` ou sua chave)
- `NASA_BASE_URL`
- `EPIC_BASE_URL`

Frontend (`frontend/.env`):

- `VITE_API_BASE` (ex: `http://localhost:5000`)

## Endpoints

- `POST /auth/register` - criar usuario
- `POST /auth/login` - login
- `GET /api/apod` - imagem do dia
- `GET /api/epic` - imagem EPIC mais recente
- `GET /api/mars-rover?sol=1000` - fotos do rover
