## Installation:
---
1. Create virtualenv
2. git clone https://github.com/hellpirat/newsportal.git
3. pip install -r requirements.txt
4. Settings your Database in local_settings.py
5. manage.py migrate
6. manage.py sitetreeload --mode=replace treedump.json
7. manage.py loaddata Categories.json
8. django-admin runserver
