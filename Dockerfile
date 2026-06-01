# 1. Usar una imagen oficial de Python ligera
FROM python:3.12-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código del proyecto
COPY . .

# 5. Exponer el puerto en el que corre tu app (por ejemplo, el 5000)
EXPOSE 5000

# 6. Comando para arrancar la aplicación
CMD ["python", "app.py"]