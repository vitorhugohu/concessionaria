# 🚗 Concessionária API — Automobiles Management System

API RESTful completa para gerenciamento e cadastro de veículos em uma concessionária, desenvolvida com **Django REST Framework**, banco de dados **PostgreSQL** e totalmente containerizada utilizando **Docker** e **Docker Compose**.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Framework Web:** Django 5.2
* **API Toolkit:** Django REST Framework (DRF) 3.18
* **Banco de Dados:** PostgreSQL 15 (Alpine)
* **Containerização:** Docker & Docker Compose
* **Driver DB:** Psycopg2-binary
* **Variáveis de Ambiente:** Python-Decouple / Python-Dotenv

---

## 📐 Arquitetura e Estrutura do Projeto

O projeto utiliza o padrão MVT/MVC do Django modularizado por aplicações:

```text
automobiles/
├── core/                   # Configurações globais do Django (settings, urls, wsgi)
├── management/             # Aplicação principal de gerenciamento
│   ├── migrations/         # Histórico de migrações do banco de dados
│   ├── admin.py            # Configuração do Django Admin para a entidade Vehicle
│   ├── models.py           # Definição dos modelos de dados (Vehicle)
│   ├── serializers.py      # Serializadores para tradução e validação de JSON
│   ├── urls.py             # Mapeamento de rotas e endpoints do app
│   └── views.py            # Regras de negócio da API (Class-Based Views / Generics)
├── docker-compose.yml      # Orquestração dos serviços (Django Web + PostgreSQL DB)
├── Dockerfile              # Imagem base da aplicação Python
├── requirements.txt        # Dependências do projeto
└── manage.py               # Script de gerenciamento do Django
