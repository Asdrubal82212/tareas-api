# Tareas API

API REST con Spring Boot para gestionar tareas (CRUD).

## Requisitos
- Java 21
- MySQL

## Configuración
1. Crear la base de datos:
```bash
   mysql -u root -e "CREATE DATABASE tareasdb;"
```
2. Si tu MySQL tiene contraseña, ponla en `src/main/resources/application.properties`.

## Ejecutar
```bash
./mvnw spring-boot:run
```
La API queda en `http://localhost:8080/api/tasks`.

## Endpoints
| Método | URL | Descripción |
|---|---|---|
| GET | /api/tasks | Listar tareas |
| GET | /api/tasks/{id} | Obtener una tarea |
| POST | /api/tasks | Crear tarea |
| PUT | /api/tasks/{id} | Actualizar tarea |
| DELETE | /api/tasks/{id} | Eliminar tarea |
