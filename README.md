# 👋 Приветсвие

Привет. Данная статья посвещена Django на Python. Это как разобранная документация всего важного. озможно, именно тут будут находится различные примеры.

### 📃 Справка о Django
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

# 💻 Проект django_curse
Сначала создадим проект на django. Для этого пишем в терминале `django-admin startproject name_project`, где `name_project` - имя вашего проекта. 

### Manage.py
 Это скрипт для выполнения команд из командной строки. Будет нам помогать запускать виртуальный сервси и многое другое. Сам код создан по-умолчанию и мы его не трогаем.

 ### __init__.py

 Пустой файл, но в будущем можем записывать характеристики для обработки при запуске

 ### asgi.py и wsgi.py

 Это два похожих друг на друга файла. Используются для подключения к серверу, но `asgi` можно назвать более новым стандартом. Мы будем работать косвенно. Они нужны.

### ⚙️ settings.py

Это очень важный файл, содержащий все настройки django-проекта.

```
BASE_DIR = Path(__file__).resolve().parent.parent
```

`BASE_DIR` записывает полный путь к проекту.

```
SECRET_KEY = 'django-insecure-vdst@^bhmn@n+u2*q#9z#^mz^xxko+(-vcit*f36$d!f_8@@tk'```

`SECRET_KEY` — секретный ключ проекта. Его не стоит передавать никому лишнему, иначе проект можно легко взломать. Сейчас я его показываю, поскольку это pet-проект (тренировочный).


```
DEBUG = True``` 

`DEBUG` позволяет регулировать показ ошибок на самом сайте. `True` — все ошибки показываются на сайте.

```
ALLOWED_HOSTS = []

```

Указываем те `host` или доменные имена, на которые будет разрешено опубликовать данный сайт.

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

`INSTALLED_APPS` — список установленных технологий (приложений) для проекта.

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

`MIDDLEWARE` — записано промежуточное ПО, обеспечивающее безопасность, работу с сессиями и т. д.

### urls.py

Этот файл, по сути, позволяет отслеживать разлчные url-адреса. Например:

```
urlpatterns = [
    path('admin/', admin.site.urls),
]

```

То есть при переходе по url-адресу `/admin` бдует открыватся приложение `admin.site.urls` (панель администратора)


`ROOT_URLCONF = 'django_curse.urls'` — основной файл `urls`.
Тут мы указываем настройки базы данных для соединения.

### Первый запуск
---

Чтобы запустить, мы переходим в терминал, где переходим с помощью `cd` в проект на Django. В моём случае это `django_curse`, значит переход выполняется командой `cd django_curse`. Затем там мы обращаемся к питону, к файлу `manage.py` и запускаем: `python manage.py runserver`, где получим сообщение:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 16, 2025 - 18:56:54
Django version 5.2.1, using settings 'django_curse.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
```

Красная ошибка — это нормально. В дальнейшем мы будем делать миграции. А сейчас кликаем на ссылку `http://127.0.0.1:8000/` либо копируем и вставляем в браузер. Мы получим страницу по умолчанию.

### Остановка сервера
---

После работы всегда лучше останавливать сервер. Для этого в терминале нажимаем на связку клавиш `ctrl + c`.


# 🧑‍💻Добавление приложения

Теперь рассмотрим то, как добавить приложение внутри Django-проекта. Но что это такое?

`Приложение внутри Django-проекта` — это отдельная категория сайта. Например, у нас есть сайт и там есть форум. Так вот, форум можно выделить как отдельное приложение. Или же так можно сделать с регистраций. Количество приложений не важно. Но желательно не пихать всё в одну категорию по теме/функции. Например, основная часть сайта может быть как приложение main.

### Создание
---

Чтобы создать приложение, пишем в терминале `python manage.py startapp main`. Только не забывайте перед этим зайти в папку проекта. После создания приложения переходим в папку с таким же названием, как у проекта. Там открываем файл `settings.py` и в `INSTALL_APP` региструем приложение. В качестве значения пишем просто названия нового приложения. Например, `main`. И будет выглядеть так:

```
INSTALLED_APPS = [
    'main', #Добавли новое приложение  main
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

###  Базовая структура
---

`admin.py` — можно настраивать то, какие таблички будут в панели администрации.
`apps.py` — описание локальных настроек для приложения.
`models.py` — в файле мы можем создать класс, на основе которого будет создавать таблица в базе данных.
`tests.py` — в файле прописываются тесты. Например, unit-тесты.
`views.py` — отвечает за методы, которые будут работать при переходе на определенную страницу.

### Отслеживание url
Теперь мы можем отслеживать url-адреса для main. Для этого в папке, где и располагается `settings.py`, открываем файл `urls.py`. И в `urlpatterns` вставляем новый файл в таком формате: `path('url_address', app)`, где `url_address` — это адрес, на который переходим, а `app` — это приложение, на которое мы попадаем при переходе по `url_address`. Чтобы обозначить главную страницу, то `url_address` ставим `''`.

Перед созданием в папке приложения `main` создадим файл `urls.py`, потом возвращаем обратно в файл `django_source/django_course/urls.py` (путь моего примера) самого проекта и импортируем помимо `path` метод `include`.

Затем в `urlpatterns` добавляем:

```
path('', include('main.urls')
```

И будет выглядеть так:

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
```

Ну а в файл `main/urls.py` добавим это:

```
from django.urls import path

urlpatterns = [
    
]
```

Когда пользователь зайдет на главную страницу, у нас будет вызван файл `urls.py`, принадлежащий `django_curse` (именно указан как главный файл в `settings.py` в `ROOT_URLCONF`). И дальше будет вызван `urls.py` из `main`. Дальше мы должны вызвать метод. Чтобы такое сделать, то в этом файле пишем:

`from . import vews`

А в `urlpatterns` пишем `path('', vews.index)`. По сути, `vews.py` работает как обычный питоновский файл. Мы можем создавать классы, а уже в vews писать функции, которые будут вызвать методы классов. 

`index` пишем без скобок, чтобы мы просто его вызвали. Если будут скобки, то значит сразу начнется его выполнение. `index` — это метод внутри файла `vews.py`.

### Вывод текста на сайт (пример)



Например, `index` будет выводеить текст. Для этого в файле `views.py` импортируем `HttpResponse` из  библиотеки `django.http`. А в функции вовзращаем `HttpResponse('text')`.

Например:

```
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h4>Error 404<h4>')

```

А теперь запустим и проверим. Запуск описан выше.  Все работает.

### Добалвение нового отслеживания

Давай будем отслеживать переход на страницу about. В файле `urls.py` в `main` добавим `path('about', views.about)` и создади функцуию `about` в `views.py`, которая тоже будет выводит текст, но другой.

`main/urls.py`:

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about)
]
```

`main/views.py`:

```
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h4>Error 404<h4>')

def about(request):
    return HttpResponse('<h4>Привет<h4>')
```

Сервер в автоматическом режиме будет обновлятся. И теперь открыв главную страницу в адрес напишем `http://127.0.0.1:8000/about` и увидем наш текст `Привет`.

# 📄Вывод HTML страниц

Теперь мы будем использовать вместо `HttpResponse`, который использовался в предыдущем разделе, метод `render`, который импортирован по умолчанию в файле `views.py` приложения `main`.

И теперь мы можем регулировать то, какой html-шаблон будет отображаться при переходе. В `render` первым аргументом передаём `request`, который по умолчанию должен приниматься функцией, а вторым — название html-шаблона. 

### Создадим html-шаблон
---

Внутри приложения обязательно создаём новую папку `templates`, обязательно только это название!!!

Ну и, как рекомендует документация django, в этой папке создать папку с названием приложения. В моём случае — `main`. Всё просто, django объединяет все папки `templates`, поэтому, чтобы django хорошо ориентировался по приложениям, создаём папку с названием приложения. Уже внутри её создаём html-файл с шаблоном. Например, `index.html`. То есть в моём случае путь до этого файла будет такой: `django_curse/main/templates/main/index.html`.

В команде `render` путь до папки мы пишем относительно папки `templates`, будто мы в ней находимся. То есть у меня это — `main/index.html`. И вся функция в `views.py` будет выглядеть примерно так:

```
def index(request):
    return render(request, 'main/index.html')
```

А в `index.html` напишем мелкий код. Например:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Главная страница</h1>
    <p>Привет, ученик. Подпишись на мой github @roge111</p>
</body>
</html>
```

Но и похожее делать можем для любой функции в
нутри `views.py`. Я так сделал и для функции `about`:

`views.py`

```
def about(request):
    return render(request, 'main/about.html')
```



`about.html`

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Про тебя</title>
</head>
<body>
    <h1>Про тебя</h1>
    <p>Привет</p>
</body>
</html>
```

Заметим, что у нас много что повторяется кроме тегов `title`, `h1` и `p` 

И создадим отдельный файл, как шаблон.

Создадим новый html, например `pattern.html`. Сначала узнаем про шаблонизатор джинджа (я решил именно так написать 😂). Это встроенная конструкция от django. Работает только в html внутри django-проекта. Он позволяет создавать щаблоны. Обозначаем `{%  %}`.

Например, создадим шаблонную секцию:
```
{% block content %}
{% endblock %}
```

Так мы выделяем секцию, где `content` — это название блока, которое должно быть уникальным в пределах файла:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
   {% block content %}

   {% endblock %}
</body>
</html>
```

Теперь зайдем в файл `index.html` и в шаблонизаторе пишем команду `extends`. Мы наследуем от шаблона. То есть: `{% extends 'main/pattern.html' %}`.

Затем дальше пишем в шаблонизаторе следующее название блока. Например, `content`: `{% block content %}`. И помещаем во внутрь html-код, который в дальнейшем будет подставляться в этот блок в шаблоне. Ну и так же закрыть блок, как и в шаблоне. Пример `index.html`:

```
{% extends 'main/pattern.html' %}

{% block title %}
    Главная страница
{% endblock %}

{% block content %}
    <h1>Главная страница</h1>
    <p>Привет, ученик. Подпишись на мой github @roge111</p>
{% endblock %}
```
И пример `about.html`:

```
{% extends 'main/pattern.html' %}

{% block title %}
    Про нас
{% endblock %}

{% block content %}
    <h1>Про нас</h1>
    <p>Про нас</p>
{% endblock %}
```

И после запуска увидим, что ничего не поменялось. И теперь нам не надо копировать один и тот же код писать постоянно. То есть теперь мы можем быстрее редактировать.

# Bootstrap

Установить Bootstrap можно отсюда: https://getbootstrap.com/docs/5.0/getting-started/download/

Но мы сделаем проще. Перейдем на https://www.bootstrapcdn.com/ и скопируем ссылку на css. Дальше в файле `pattern.html` в теге `<head>` пропишем это: `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">`. То есть Bootstrap — это помощник в мире стилей. Он поможет быстрее писать front, что ускоряет разработку сайта. При запуске главной страницы мы увидим, что стили текста поменялись. 

# Создание и подключение css файла

Все статические файлы, куда входят css, мы должны хранить обязательно в папке `static` внутри приложения. Ну и внутри создаем папку с именем приложения. А внутри лучше создать папки `css` для хранения css-файлов, `img` — для хранения картинок и `js` — для хранения файлов javascript.

Дальше работу ты можешь глянуть тут: 


# До встречи
Спасибо тебе за внимание, надеюсь, что было очень полезно.


Также при помощи `include` в шаблонизаторе можем подключать другие html: `{% include 'main/test.html' %}`, но я его не стал добавлять в репозиторий.




