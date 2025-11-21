CREATE DATABASE IF NOT EXISTS bdagencia;
USE bdagencia;

CREATE TABLE IF NOT EXISTS roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    apellidos VARCHAR(120) NOT NULL,
    nickname VARCHAR(120) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    clave VARCHAR(255) NOT NULL,
    telefono VARCHAR(30),
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);

CREATE TABLE IF NOT EXISTS destinos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    actividades TEXT,
    costo_base DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS paquetes_turisticos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    destino_id INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    precio_total DECIMAL(10,2) NOT NULL,
    disponible BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (destino_id) REFERENCES destinos(id)
);

CREATE TABLE IF NOT EXISTS estado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL
);

CREATE TABLE IF NOT EXISTS reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    paquete_id INT NOT NULL,
    estado_id INT NOT NULL,
    fecha_reserva DATETIME NOT NULL,
    FOREIGN KEY (estado_id) REFERENCES estado(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (paquete_id) REFERENCES paquetes_turisticos(id)
);

-- Usuario de administración para trabajar desde MySQL Workbench con todos los privilegios sobre la base.
CREATE USER IF NOT EXISTS 'viajes_admin'@'%' IDENTIFIED BY '123*';
GRANT ALL PRIVILEGES ON bdagencia.* TO 'viajes_admin'@'%';
FLUSH PRIVILEGES;
