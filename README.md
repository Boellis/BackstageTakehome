# Number Difference Service

This Django REST API returns the difference between:
1. The square of the sum of the first 'n' natural numbers.
2. The sum of the squares of the first 'n' natural numbers.

## Requirements
- Python 3.10+
- Django 4.2+

## Setup
- Inside your terminal, navigate to a folder you want to download the project in. Once there, run the following commands:
```bash
git clone https://github.com/Boellis/BackstageTakehome.git
cd BackstageTakehome
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
## Usage
- Visit: http://localhost:8000/difference?number=10

## Example Response
{
  "datetime": "2025-04-30T17:05:23.123456Z",
  "value": 2640,
  "number": 10,
  "occurrences": 3,
  "last_datetime": "2025-04-30T17:04:00.000000Z"
}
