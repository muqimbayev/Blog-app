# Django Blog ilovasi
Bu Djangoda RestAPI dan foydalanib blog app uchun api yaratishga mo'ljallangan.
### O'rnatish
1. Repozitoriyani clone qiling:

```
git clone git@github.com:muqimbayev/Blog-app.git
```
2. Virtual muhitni o'rnatish:
```
pip install pipenv
```
3. Virtual muhitni ishga tushirish:
```
pipenv shell
```
4. Qo'shimcha kerakli modullarni o'rnatish:
```
pipenv install -r  Blog-app/requirements.txt
```
5. Ma'lumotlar bazasini migratsiya qilish va yaratish:
```
python manage.py makemigrations
python manage.py migrate
```
6. Ilovaning ishga tushirilishi:
```
python manage.py runserver
```
7. Brauzeringizda http://127.0.0.1:8000/ manziliga kirib, ilovaning ishlashini  tekshirish mumkin. API larni ko'rish uchun http://127.0.0.1:8000/swagger manziliga o'ting.

## Muallif
Muallif: Qobiljon Muqimbayev
