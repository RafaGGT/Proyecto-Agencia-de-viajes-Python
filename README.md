# 🧳 Agencia de Viajes - Python

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![License](https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Estado-En%20desarrollo-yellow?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interfaz-CLI-lightgrey?style=for-the-badge)

Sistema de gestión para una agencia de viajes desarrollado en **Python**, con arquitectura en capas (MVC) y persistencia en **MySQL**. Permite administrar destinos, paquetes turísticos, usuarios y reservas desde una interfaz de consola.

## 📋 Tabla de contenidos

- [Características](#-características)
- [Arquitectura del proyecto](#-arquitectura-del-proyecto)
- [Requisitos previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración de la base de datos](#-configuración-de-la-base-de-datos)
- [Uso](#-uso)
- [Estructura de carpetas](#-estructura-de-carpetas)
- [Tecnologías utilizadas](#-tecnologías-utilizadas)

## ✨ Características

- **Gestión de usuarios**: registro, inicio de sesión, roles (administrador/cliente), cambio de contraseña, edición de datos personales y eliminación de cuenta.
- **Seguridad**: contraseñas hasheadas con `bcrypt` e ingreso oculto por consola con `pwinput`.
- **Gestión de destinos**: alta, listado, edición y eliminación.
- **Gestión de paquetes turísticos**: creación asociada a un destino y rango de fechas, listado, cambio de disponibilidad y eliminación.
- **Gestión de reservas**: los clientes pueden reservar paquetes y consultar su historial; los administradores pueden ver todas las reservas del sistema.
- **Menús diferenciados** según el rol del usuario autenticado (administrador o cliente).

## 🏗 Arquitectura del proyecto

El proyecto sigue el patrón **MVC (Modelo - Vista - Controlador)**, con una capa adicional de **servicios** encargada del acceso a datos:

```
Vista (Menu) → Controlador → Servicio → Modelo → Base de datos (MySQL)
```

- **`vista/`**: interfaz de usuario por consola.
- **`controlador/`**: orquesta la lógica entre la vista y los servicios.
- **`servicio/`**: contiene la lógica de acceso a datos y las consultas SQL.
- **`modelo/`**: representa las entidades del dominio (Usuario, Destino, PaqueteTuristico, Reserva).

## ⚙️ Requisitos previos

- Python 3.12 o superior
- MySQL Server 8.0 o superior
- pip

## 📦 Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/<tu-usuario>/Proyecto-Agencia-de-viajes-Python.git
   cd Proyecto-Agencia-de-viajes-Python
   ```

2. (Opcional pero recomendado) Crea un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install mysql-connector-python bcrypt pwinput
   ```

## 🗄 Configuración de la base de datos

1. Crea la base de datos y las tablas ejecutando el script incluido (`bdagencia.sql`) en tu servidor MySQL:

   ```bash
   mysql -u root -p < bdagencia.sql
   ```

   Este script crea la base de datos `bdagencia` junto con las tablas `roles`, `usuarios`, `destinos`, `paquetes_turisticos`, `estado` y `reservas`.

2. Crea un usuario de MySQL con permisos sobre la base de datos (o usa uno existente) y actualiza las credenciales en `servicio/Conexion.py`:

   ```python
   class Conexion:
       def __init__(self, user="viajes_admin", password="123*", database="bdagencia", host="localhost", port=3306):
           ...
   ```

   > ⚠️ Se recomienda no dejar credenciales sensibles escritas en el código fuente; considera moverlas a variables de entorno.

## ▶️ Uso

Ejecuta la aplicación desde la raíz del proyecto:

```bash
python app.py
```

Al iniciar, se generan automáticamente los roles y datos base necesarios (roles `admin` y `cliente`). Desde el menú principal podrás:

1. **Iniciar sesión** con un usuario existente.
2. **Registrar un nuevo usuario** (rol cliente por defecto).
3. **Salir** del programa.

Según el rol del usuario autenticado, accederás a:

- **Panel administrador**: gestión de destinos, gestión de paquetes turísticos y revisión de todas las reservas.
- **Panel cliente**: consulta de paquetes disponibles, creación de reservas, historial de reservas propias y ajustes de cuenta.

## 📁 Estructura de carpetas

```
Proyecto-Agencia-de-viajes-Python/
├── app.py                     # Punto de entrada de la aplicación
├── bdagencia.sql               # Script de creación de la base de datos
├── controlador/                 # Controladores (lógica intermedia)
│   ├── UsuarioController.py
│   ├── DestinoController.py
│   ├── PaqueteController.py
│   └── ReservaController.py
├── modelo/                      # Entidades del dominio
│   ├── Usuario.py
│   ├── Destino.py
│   ├── PaqueteTuristico.py
│   └── Reserva.py
├── servicio/                    # Acceso a datos y conexión a MySQL
│   ├── Conexion.py
│   ├── UsuarioService.py
│   ├── RolService.py
│   ├── DestinoService.py
│   ├── PaqueteService.py
│   └── ReservaService.py
└── vista/                       # Interfaz de consola
    └── Menu.py
```

## 🛠 Tecnologías utilizadas

- **Python** — lógica de negocio y orquestación general.
- **MySQL** — persistencia de datos.
- **mysql-connector-python** — conexión entre Python y MySQL.
- **bcrypt** — hasheo seguro de contraseñas.
- **pwinput** — entrada de contraseñas oculta en consola.

---

## 👨‍💻 Autores
 
| Nombre | GitHub |
|--------|--------|
| Lucas  | [@LFP2002](https://github.com/LFP2002) |
| Rafa   | [@RafaGGT](https://github.com/RafaGGT) |

---

Proyecto desarrollado con fines educativos como práctica de arquitectura en capas y persistencia de datos en Python.
