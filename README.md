# Music-Akinator-for-Hackathon-
Були використані API сервісів audd.io та youtube

Доброго дня шановний читач!!!
Ми розгорнули цей додаток в сервісі heroku
Щоб скористуватися веб-додатком можете перейти за посиланням http://makinator.herokuapp.com/
Якщо ви бажаєте розгорнути його локально на вашому пристрої завантажте собі даний репозиторій та встановіть бібліотеки з 
requirements.txt
потім, знаходячись в папці з проектом, виконайте команду python manage.py runserver
за адресою 127.0.0.1:8000 ви знайдете запущений проект.
Є деякі особливості локального запуску. Сервіс youtube налаштований так, що за певних налаштувань відео, він відмовляється програвати його на локальних серверах. Тому ви знайдете додаткове посилання під відео.

Невеликий коментар по API
сервіс audd.io дає 300 безкоштовних запитів, якщо запити закінчились, слід отримати новий токен(телеграм бот сервісу audd.io), та змінити старий у файлі getsong.py або оплатити додаткові запити.
