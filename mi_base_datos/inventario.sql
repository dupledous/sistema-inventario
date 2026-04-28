

CREATE TABLE Productos (
    producto_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    descripcion TEXT,
    precio REAL,
    stock  INTEGER,
    fecha_de_creacion TEXT);

CREATE TABLE Clientes(
    cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    email TEXT,
    direccion TEXT);

PRAGMA foreign_key = ON;
CREATE TABLE Ventas(
    ventas_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INT ,
    fecha TEXT,
    total REAL,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(cliente_id)
    );

PRAGMA foreign_key = ON;
CREATE Table Detalle_venta(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ventas_id INT,
    producto_id INT,
    cantidad INT,
    subtotal REAL,
    FOREIGN KEY (ventas_id) REFERENCES Ventas(ventas_id),
    FOREIGN KEY (producto_id) REFERENCES Productos(producto_id));

INSERT INTO Productos (nombre,descripcion,precio,stock,fecha_de_creacion)
 VALUES("Martillo","para clavar o golpear",5000,12,'2025-10-07'),
("Taladores","para perforar agujeros o atornillar",5000,12,'2025-10-07'),
("Cuteres","para cortar con precision",8000,12,'2025-10-07'),
("Destornilladores","para apretar o aflojar tornillo",2000,12,'2025-10-07'),
("Alicate","para sujetar, cortar o doblar materiales",5000,12,'2025-10-07');
 

INSERT INTO Clientes(nombre,email,direccion) 
VALUES("Pierre Jean","pierre@gmail.com","isluga 6836"),
("Pie Jeanette","pie_jeanette@gmail.com","isluga 6846"),
("Pierr0 Jean","pierr0@gmail.com","isluga 6836");


INSERT INTO Ventas(cliente_id,fecha,total)
VALUES(1,'2025-10-07',15000),
(2,'2025-10-07',15000);



INSERT INTO Detalle_venta(ventas_id,producto_id,cantidad,subtotal) VALUES
(1,1,3,15000),
(2,2,3,15000);

SELECT * FROM Productos;
SELECT v.ventas_id ,c.nombre FROM Ventas v JOIN Clientes C ON c.cliente_id = v.cliente_id;
SELECT d.id,d.ventas_id,p.nombre,p.precio,d.cantidad,v.total,v.fecha FROM Detalle_venta d JOIN Ventas v ON d.ventas_id = v.ventas_id
JOIN Productos p on d.producto_id = p.producto_id;


