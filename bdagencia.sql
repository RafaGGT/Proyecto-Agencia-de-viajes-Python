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

INSERT INTO estado (nombre) VALUES
('Pendiente'),
('Confirmada'),
('Cancelada');

-- Insertar destinos
INSERT INTO destinos (nombre, descripcion, actividades, costo_base) VALUES
('San Pedro de Atacama', 'Desierto y formaciones rocosas únicas en el norte de Chile.', 'Tour astronómico, visita a los géiseres, trekking', 350.00),
('Torres del Paine', 'Parque nacional con montañas, glaciares y lagos al sur de Chile.', 'Senderismo, navegación, fotografía', 550.00),
('Isla de Pascua', 'Isla polinésica famosa por sus moáis y cultura ancestral.', 'Visita a los moáis, buceo, recorridos arqueológicos', 750.00),
('Valparaíso', 'Ciudad portuaria colorida con cerros y arte urbano.', 'City tour, paseo en ascensores, gastronomía local', 220.00);

-- Insertar paquetes turísticos
INSERT INTO paquetes_turisticos (destino_id, fecha_inicio, fecha_fin, precio_total, disponible) VALUES
(1, '2025-01-10', '2025-01-15', 500.00, TRUE),
(2, '2025-02-05', '2025-02-12', 820.00, TRUE),
(3, '2025-03-01', '2025-03-07', 1100.00, TRUE),
(4, '2025-01-20', '2025-01-22', 300.00, TRUE);