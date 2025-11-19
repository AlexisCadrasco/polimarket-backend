# polimarket-backend
PoliMarket – Sistema Modular de Negocio
PoliMarket es un sistema de información empresarial compuesto por cinco módulos independientes:

Recursos Humanos (RRHH)

Ventas

Bodega

Proveedores

Entregas

Cada módulo funciona como un componente autónomo, con su propia lógica y base de datos, y se comunica con los demás mediante APIs REST, garantizando un diseño desacoplado, escalable y orientado a servicios.

🟩 Objetivo del Proyecto

Este repositorio contiene la implementación del backend del módulo de Recursos Humanos (RRHH) y un componente mínimo del módulo Ventas, desarrollados como parte de la arquitectura distribuida de PoliMarket.

El principal objetivo es implementar los servicios esenciales que permiten:

Registrar empleados y vendedores

Autorizar vendedores para que puedan operar en otros módulos

Permitir que Ventas consulte a RRHH para validar autorización

Exponer APIs REST documentadas en Swagger/OpenAPI

Conectarse a una base de datos transaccional (MySQL)

Estos módulos forman parte del ecosistema general de PoliMarket, cumpliendo con los requisitos funcionales exigidos en la actividad académica.

🟦 Módulo Implementado: Recursos Humanos (RRHH)

El backend implementa las funcionalidades principales del área de RRHH:

✔ Registrar empleados
✔ Registrar vendedores
✔ Autorizar vendedores
✔ Consultar información completa del vendedor
✔ Registrar administradores de RRHH

El módulo expone una API completa con endpoints REST que pueden ser consumidos por cualquier otro módulo del sistema, como Ventas o Entregas.

🟧 Integración con Ventas

Además del módulo RRHH, se implementa parcialmente un cliente/consumidor desde el módulo Ventas, que interactúa con RRHH para:

✔ Validar si un vendedor está autorizado
✔ Consumir los endpoints REST de RRHH

Esto demuestra la comunicación entre componentes descrita en la arquitectura del sistema PoliMarket.

🟩 Tecnologías Utilizadas

Flask (Python) — framework principal de la API

Flask-SQLAlchemy — ORM para persistencia

MySQL — base de datos transaccional

Gunicorn / Nginx — despliegue en producción

Swagger / OpenAPI — documentación de la API

Git y GitHub — control de versiones

🟦 Arquitectura del Proyecto

El proyecto está organizado en una estructura modular:

/rrhh
   controllers.py
   models.py
   repository.py
   service.py
/app.py
/swagger.yaml
/requirements.txt


Siguiendo principios de:

Clean Architecture

DDD (Domain Driven Design)

Separación por capas

Interfaces y componentes desacoplados

🟧 Estado Actual del Proyecto

Módulo RRHH → ✔ 100% funcional

Módulo Ventas → ✔ Cliente parcial implementado

Módulos Bodega, Proveedores y Entregas → Solo modelados en diagramas

🟩 Propósito Académico

Este proyecto forma parte de la Actividad Evaluativa Sumativa 2, demostrando:

Construcción de APIs REST

Uso de componentes de negocio y cliente

Modelado UML (clases, componentes y casos de uso)

Integración entre módulos de una arquitectura distribuida

Despliegue en servidor Linux usando Nginx + Gunicorn
