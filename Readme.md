# **ESTRUCTURA**
my_flask_app/
│
├── app/
│   ├── __init__.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── user_controller.py
│   │   └── ... (otros controladores)
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   └── ... (otras entidades)
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── user_repository.py
│   │   │   └── ... (otros repositorios)
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── user_service.py
│   │   │   └── ... (otros servicios)
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── ... (otras plantillas)
│   ├── static/
│   │   ├── css/
│   │   │   └── ... (archivos CSS)
│   │   ├── js/
│   │   │   └── ... (archivos JavaScript)
│   │   └── img/
│   │       └── ... (imágenes)
│   ├── viewmodels/
│   │   ├── __init__.py
│   │   ├── user_viewmodel.py
│   │   └── ... (otros viewmodels)
│   ├── config.py
│   ├── routes.py
│   └── extensions.py
│
├── tests/
│   ├── __init__.py
│   ├── test_user.py
│   └── ... (otros tests)
│
├── migrations/
│   └── ... (archivos de migración)
│
├── venv/
│   └── ... (entorno virtual)
│
├── .env
├── .gitignore
├── requirements.txt
├── run.py
└── README.md

 python3 --version
 pip3 install virtualenv

pip install -r requirements.txt
 source venv/bin/activate

  flask run
  export FLASK_APP=main.py

pip install flask flask-sqlalchemy flask-migrate pymysql
dotenv