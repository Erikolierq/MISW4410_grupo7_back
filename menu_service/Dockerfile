FROM python:3.14.3-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar e instalar dependencias desde requirements.txt
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto de la aplicación Flask (ajusta si usas otro)
EXPOSE 3004

# Comando para ejecutar tu aplicación Flask
CMD ["python", "app.py"]
