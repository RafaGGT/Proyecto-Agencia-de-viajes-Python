CREATE DATABASE bdagencia;
USE bdagencia;

-- ROLES
CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL
);

-- USUARIOS
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    apellidos VARCHAR(120) NOT NULL,
    nickname VARCHAR(120) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    clave VARCHAR(255) NOT NULL,
    telefono VARCHAR(30),
    rol_id INT,
    FOREIGN KEY (rol_id)
        REFERENCES roles(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- DESTINOS
CREATE TABLE destinos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    actividades TEXT,
    costo_base DECIMAL(10,2)
);

-- PAQUETES TURÍSTICOS
CREATE TABLE paquetes_turisticos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    destino_id INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    precio_total DECIMAL(10,2) NOT NULL,
    disponible BOOLEAN NOT NULL DEFAULT TRUE,

    FOREIGN KEY (destino_id)
        REFERENCES destinos(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- ESTADO
CREATE TABLE estado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL
);

-- RESERVAS
CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    paquete_id INT NOT NULL,
    estado_id INT NOT NULL,
    fecha_reserva DATETIME NOT NULL,

    FOREIGN KEY (usuario_id)
        REFERENCES usuarios(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (paquete_id)
        REFERENCES paquetes_turisticos(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (estado_id)
        REFERENCES estado(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- USUARIO ADMINISTRADOR
CREATE USER 'viajes_admin'@'%' IDENTIFIED BY '123*';
GRANT ALL PRIVILEGES ON bdagencia.* TO 'viajes_admin'@'%';
FLUSH PRIVILEGES;
