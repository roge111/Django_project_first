# Django

Привет. Данная статья посвещена Django на Python. Возможно, именно тут будут находится различные примеры.

### Справка о Django
---

`Django` — это фреймворк, предлагающий огромное количество готовых решений для создания веб-сервисов на Python. Конечно, реализовать можно и без него, но так будет гораздо дольше. 

Фреймворк работает на основе MVC (Model, View, Controller), позволяющая разбит файл на одну из трех категорий: `html-шаблоны`, `файлы модели` для работы с базами данных (далее БД) и `файлы контроллера` для связи модели и html-шаблонов. Также сайт, сделанный на Django, будет обладать быстрой подгрузкой и выдерживать большую нагрузку. Данный фреймворк используют: Google, Yandex, YouTube и т.д.

 Изначально требуется изучить синтаксиси Python. Я советую курс от института биоинформатики на stepik: https://stepik.org/course/67/syllabus (бесплатынй)

### Установка Django
В Visual Studio Code или PyCharm создаём новый проект. Я буду рассказывать на примере Visual Studio Code (далее VS Code или VS). Сначала создадим папку в проводнике, которая будет служить в дальнейшем проектом. Затем открываю ее внутри VS Code. `File` -> `Open Folder` и выбираем папку. Далее внизу открываем терминал и вводим команду `pip3 install django` и дожидаемся окончания установки. Проверьте потом `django-admin --version`. 

Если не работает, то сделаем через терминал так: используя `cd` доходим до папки проекта, создаем виртуальную среду `venv` — `python -m venv .venv`, активируем её — `.venv\Scripts\activate.bat`, а потом вводим `pip3 install django`. Минус в том, что придется каждый раз, открывая проект, активировать виртуальную среду.


Если же вы наблюдаете похожее сообщение:

```
 WARNING: The script sqlformat.exe is installed in 'C:\Users\batar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script django-admin.exe is installed in 'C:\Users\batar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

То скопируйте путь `C:\Users\batar\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts` (из моего примера). В кнопке `Пуск` в поиск вбить переменные среды. Будет похожий результат: `Изменение системных переменных сред`. Открываете, там в нижнем углу жмете на кнопку `Переменные среды` -> в окне `Переменные среды для пользователя ...` находите `Path` -> два раза кликаете -> нажимаете `изменить` -> `создать` -> вставляете скопированный путь -> нажимаете `ОК` -> перезагружаете среду разработки (VS Code, PyCharm и т. д.).

# Проект django_curse

### Manage.py
 Это скрипт для выполнения команд из командной строки. Будет нам помогать запускать виртуальный сервси и многое другое. Сам код создан по-умолчанию и мы его не трогаем.

 ### __init__.py

 Пустой файл, но в будущем можем записывать характеристики для обработки при запуске

 ### asgi.py и wsgi.py

 Это два похожих друг на друга файла. Используются для подключения к серверу, но asgi можно назвать более новым стандартом. Мы будем работать косвенно. Они нужны.

 ### settings.py

 Это очень важный файл, соедржащий все настройки django-проекта.


