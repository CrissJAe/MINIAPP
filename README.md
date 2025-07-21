# MINIAPP – CRUD de Profesores en Python

Aplicación de consola escrita en Python que permite crear, leer, actualizar y eliminar registros de profesores en una base de datos PostgreSQL.

---

## 🚀 Características

- Crear un nuevo profesor
- Leer todos los profesores registrados
- Actualizar datos de un profesor existente
- Eliminar un profesor por su RUT
- Validaciones de entrada (strings, números, etc.)
- Conexión segura a PostgreSQL usando variables externas

---


## ⚙️ Requisitos

- Python 3.6+
- PostgreSQL instalado y configurado
- pip (instalador de paquetes de Python)

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/MINIAPP.git
cd MINIAPP
```
2. Installa las dependencias:

```bash
pip install -r requirements.txt
```
3. Actualiza el archivo config.py y configura las variables de entorno

DB_NAME = "BASE_DE_DATOS"
DB_USER = "NOMBRE_DE_USUARIO"
DB_PASSWORD = "CONTRASEÑA"
DB_HOST = "localhost"
DB_PORT = "5432"

4. Configura postgres

    Asegúrate que tu base de datos tenga las mismas credenciales ingresadas en config.py