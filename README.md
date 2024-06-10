# Skincare Application

Welcome to the Skincare Application! This project is designed to provide comprehensive skincare product information and management capabilities. Below, you'll find detailed instructions on how to set up, run, and use the application.

## Project Overview

This application leverages a unique dataset sourced from a related skincare application. It includes models for brands, lines, products, and ingredients, and offers several endpoints for retrieving and managing product data. Key features include:

- Filtering products based on criteria such as cruelty-free and vegan status.
- Analyzing common ingredients in products from different countries.
- Viewing detailed information about individual products and their ingredients.
- Adding, updating, and deleting products based on specific criteria.

## Live Application

You can access the live application [here](https://true-glassy-app-msz3f.ondigitalocean.app/).

## Development Environment

- **Operating System**: Linux
- **Python Version**: 3.10.13
- **Packages and Versions**:
  - `asgiref==3.8.1`
  - `Django==3.0.3`
  - `django-browser-reload`
  - `python-decouple==3.8`
  - `sqlparse==0.5.0`
  - `djangorestframework==3.11.1`
  - `drf-yasg==1.21.7`
  - `factory_boy==3.0.1`
  - `gunicorn==22.0.0`

## Installation Instructions

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Collect Static Files

```bash
python manage.py collectstatic
```

## Usage Instructions

### Running the Application

```bash
python manage.py runserver
```

### Logging into Django Admin

- **Username:** ahmedshaban
- **Password:** 248655

### Importing Data

```bash
python manage.py populate_products data/SUNSCREEN.csv data/TREATMENT.csv
```
