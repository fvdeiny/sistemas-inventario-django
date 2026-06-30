# 📦 Sistema de Gestión de Inventario con Django & PostgreSQL

Este es un sistema de backend robusto diseñado para el control, auditoría e integridad de inventarios de componentes y equipos de automatización industrial (como PLCs y sensores). Permite la gestión tanto por interfaces web tradicionales como a través de endpoints de una API REST listos para ser integrados con aplicaciones móviles, interfaces frontend modernas o sistemas SCADA industriales.

## 🛠️ Tecnologías Utilizadas
* **Backend:** Python 3.14 + Django 6.0
* **Base de Datos:** PostgreSQL
* **API REST:** Django REST Framework (DRF)
* **Diseño Frontend:** Bootstrap 5

## 🚀 Características Clave
* **Arquitectura MVT de Django:** Separación limpia de la lógica de datos, control y renderizado.
* **Integridad de Datos en Base de Datos (Postgres):** Reglas de negocio embebidas en el ORM mediante sobreescritura de métodos de validación (`clean()`), previniendo caídas de stock por debajo de cero (números negativos).
* **Formularios Dinámicos con Validaciones Fuertes:** Los operadores pueden registrar ingresos y egresos de stock con manejo limpio de excepciones directo en la interfaz.
* **API RESTful de Producción:** Endpoint expuesto en `/api/productos/` que entrega datos en formato JSON nativo para integraciones externas de sistemas de monitoreo.

