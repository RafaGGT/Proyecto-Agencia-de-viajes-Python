# ✈️ Proyecto Agencia de Viajes - Python

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)
![MVC](https://img.shields.io/badge/Architecture-MVC-success?style=for-the-badge)
![OOP](https://img.shields.io/badge/OOP-Object%20Oriented-blueviolet?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

## 📖 Descripción

Sistema de gestión para una **Agencia de Viajes** desarrollado en **Python** siguiendo el patrón **Modelo-Vista-Controlador (MVC)**.

La aplicación permite administrar usuarios, destinos turísticos, paquetes de viaje y reservas mediante una interfaz de consola conectada a una base de datos MySQL.

---

## 🚀 Funcionalidades

* Registro de usuarios.
* Inicio de sesión.
* Administración de usuarios.
* Gestión de destinos turísticos.
* Gestión de paquetes turísticos.
* Creación y administración de reservas.
* Persistencia de datos mediante MySQL.
* Arquitectura organizada en MVC.

---

## 🛠 Tecnologías

* Python 3.12+
* MySQL
* SQL
* Programación Orientada a Objetos
* Arquitectura MVC

---

## 📂 Estructura del proyecto

```text
Proyecto-Agencia-de-viajes-Python/

│── app.py
│── bdagencia.sql
│
├── controlador/
│
├── modelo/
│
├── servicio/
│
└── vista/
```

---

## ⚙️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/Proyecto-Agencia-de-viajes-Python.git
```

### 2. Entrar al proyecto

```bash
cd Proyecto-Agencia-de-viajes-Python
```

### 3. Crear un entorno virtual (opcional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install pwinput mysql-connector-python
```

---

## 🗄 Base de datos

Importar el archivo:

```text
bdagencia.sql
```

Posteriormente configurar los datos de conexión en el archivo correspondiente dentro del módulo **servicio**.

---

## ▶️ Ejecutar

```bash
python app.py
```

---

## 🏛 Arquitectura

El proyecto utiliza el patrón **MVC**:

* **Modelo:** representa las entidades del dominio.
* **Vista:** interacción mediante consola.
* **Controlador:** coordina la lógica entre vista y modelo.
* **Servicio:** encapsula la conexión con la base de datos.

---

## 📌 Características

* Código organizado por responsabilidades.
* Programación Orientada a Objetos.
* Persistencia con MySQL.
* Interfaz de consola.
* Gestión de usuarios y reservas.
* Fácil de extender.

---

## 👨‍💻 Autores
**Lucas Fuentes**
**Rafael Gallegos**

GitHub:
https://github.com/LFP2002/
https://github.com/RafaGGT/
