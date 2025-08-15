carparts-app/
├── app/
│   ├── __init__.py
│   ├── main.py              ← FastAPI entry point
│   ├── models.py            ← SQLAlchemy models
│   ├── schemas.py           ← Pydantic request/response models
│   ├── database.py          ← DB connection setup
│   ├── crud.py              ← Business logic
│   └── api/
│       ├── __init__.py
│       └── routes.py        ← All your API routes
├── .env                     ← Secure DB/API keys
├── requirements.txt         ← Python dependencies
└── README.md
