# API REST de Productos

![Pipeline](https://gitlab.com/pilcajose02/autonomo_1/badges/main/pipeline.svg)

![Coverage](https://gitlab.com/pilcajose02/autonomo_1/badges/main/coverage.svg?job=test_coverage)

API REST desarrollada con Python y FastAPI para registrar y consultar productos.

El proyecto utiliza PostgreSQL para la persistencia de datos y GitLab CI/CD para automatizar la construcción, las pruebas, la medición de cobertura y el despliegue.

## Tecnologías utilizadas

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pytest
- Pytest Coverage
- GitLab CI/CD
- GitHub
- Render

## Flujo CI/CD

```text
GitLab
   |
   v
Build
   |
   v
Tests y Coverage
   |
   v
Push a GitHub main
   |
   v
Despliegue automático en Render