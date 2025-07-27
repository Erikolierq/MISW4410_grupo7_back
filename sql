CREATE TABLE public.usuario (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    nombre VARCHAR(50),
    contrasena VARCHAR(150) NOT NULL,
    rol VARCHAR(50)
);

CREATE TABLE public.restaurante (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(128) NOT NULL,
    direccion VARCHAR(256),
    telefono VARCHAR(20),
    correo VARCHAR(128)
);

CREATE TABLE public.ingrediente (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(128) NOT NULL,
    unidad VARCHAR(128) NOT NULL,
    costo NUMERIC NOT NULL,
    calorias NUMERIC NOT NULL,
    sitio VARCHAR(128),
    restaurante INTEGER NOT NULL,
    CONSTRAINT fk_ingrediente_restaurante
      FOREIGN KEY (restaurante)
      REFERENCES restaurante(id)
      ON DELETE CASCADE
);

CREATE TABLE public.receta (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(128) NOT NULL,
    duracion NUMERIC NOT NULL,
    preparacion TEXT NOT NULL,
    porcion VARCHAR(50),
    usuario INTEGER NOT NULL,
    menu INTEGER,
    CONSTRAINT fk_receta_usuario FOREIGN KEY (usuario) REFERENCES public.usuario(id),
    CONSTRAINT fk_receta_menu FOREIGN KEY (menu) REFERENCES public.menu(id) -- referenciada abajo
);

CREATE TABLE public.menu (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(128) NOT NULL,
    fechainicio VARCHAR(20),
    fechafinal VARCHAR(20),
    usuario INTEGER NOT NULL,
    restaurante INTEGER NOT NULL,
    CONSTRAINT fk_menu_usuario FOREIGN KEY (usuario) REFERENCES public.usuario(id),
    CONSTRAINT fk_menu_restaurante FOREIGN KEY (restaurante) REFERENCES public.restaurante(id)
);

-- Como `receta` ya fue creada, ahora se puede crear `menu_receta`
CREATE TABLE public.menu_receta (
    id SERIAL PRIMARY KEY,
    id_menu INTEGER NOT NULL,
    id_receta INTEGER NOT NULL,
    porcion INTEGER,
    CONSTRAINT fk_menu FOREIGN KEY (id_menu) REFERENCES public.menu(id),
    CONSTRAINT fk_receta FOREIGN KEY (id_receta) REFERENCES public.receta(id)
);

CREATE TABLE public.receta_ingrediente (
    id SERIAL PRIMARY KEY,
    cantidad NUMERIC NOT NULL,
    ingrediente INTEGER NOT NULL,
    receta INTEGER NOT NULL,
    CONSTRAINT fk_recetaing_ingrediente FOREIGN KEY (ingrediente) REFERENCES public.ingrediente(id),
    CONSTRAINT fk_recetaing_receta FOREIGN KEY (receta) REFERENCES public.receta(id)
);
