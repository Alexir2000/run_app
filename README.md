# Run App

[![Русский](https://img.shields.io/badge/language-Русский-blue.svg)](README.md)
[![English](https://img.shields.io/badge/language-English-red.svg)](README_EN.md)

The English version of this README can be found [here](README_EN.md).

**Run App** — это универсальная утилита, которая делает выполнение Python-скриптов таким же простым, как запуск любого другого приложения на вашем компьютере. С помощью этой программы вы можете превратить свои Python-скрипты в полноценные приложения, которые запускаются одним кликом, без необходимости ручной активации виртуального окружения или установки Python на вашу систему.

## Почему это полезно?

Многие разработчики сталкиваются с проблемой запуска своих Python-приложений на компьютерах, где Python может быть не установлен, 
или где его версия не совпадает с той, которая требуется приложению. **Run App** решает эту проблему, предлагая инструмент, 
который не только создает исполняемый файл для вашего скрипта, но и автоматически настраивает виртуальное окружение, 
устанавливает необходимые зависимости и гарантирует, что ваше приложение будет работать стабильно и без проблем.

Эта утилита полезна для:
- **Разработчиков**, которым нужно предоставить свои скрипты клиентам или коллегам, не знакомым с установкой и настройкой Python.
- **Системных администраторов**, которым важно, чтобы приложения запускались корректно на любой машине без дополнительных настроек.
- **Обучения и тестирования**, когда важно быстро запускать скрипты на разных системах с минимальными требованиями.

## Особенности

- **Выполнение Python-скриптов как приложений**: Преобразуйте свои Python-скрипты в исполняемые файлы, которые можно запускать прямо с рабочего стола.
- **Автоматическая настройка виртуального окружения**: Программа автоматически создаёт виртуальное окружение в каталоге `app`, если оно ещё не создано.
- **Управление зависимостями**: Программа устанавливает все необходимые зависимости, указанные в файле `requirements.txt`, в виртуальное окружение.
- **Кроссплатформенная совместимость**: Работает на Windows и macOS, обеспечивая единообразие выполнения скриптов на разных операционных системах.

## Как это работает

Программа предназначена для выполнения Python-скрипта с именем `main.py`, который должен находиться в подкаталоге `app`. Для установки всех необходимых зависимостей требуется также файл `requirements.txt` в той же директории.

### Пример структуры проекта:

your_project/

├── app/

│   ├── main.py

│   ├── requirements.txt

└── run_app.exe

В этой структуре:

- **`app/`**: Директория, содержащая основное приложение.
  - **`main.py`**: Основной скрипт Python, который будет выполняться.
  - **`requirements.txt`**: Файл с зависимостями, которые необходимо установить для работы скрипта.
- **`run_app.exe`**: Исполняемый файл, который запускает приложение.

### Дополнительные рекомендации

Для удобства вы можете переименовать `run_app.exe` в название вашего приложения. Например, 
если ваше приложение называется "Video Converter", вы можете переименовать файл в `VideoConverter.exe`. 
Затем вы можете создать ярлык на рабочем столе или в меню «Пуск» и запускать приложение так же, 
как и любое другое стандартное приложение. Это делает использование вашего Python-скрипта более удобным 
для конечного пользователя, скрывая технические детали работы с Python.


### Инструкция по использованию

1. **Подготовка**:
   - Создайте папку для Вашего будущего автономного приложения 
   - скопируйте туда утилиту run_app.exe
   - Создайте подпапку app
   - Разместите весь ваш проект в каталоге `app`. Важно, чтобы стартовый файл вашего проекта, который должен запускаться первым, 
   назывался `main.py`. Это условие необходимо для корректной работы программы. Все остальные файлы и директории вашего проекта также должны быть в папке `app`.
   - Перед размещением проекта в папке `app` необходимо создать файл `requirements.txt`, 
   который будет содержать список всех используемых библиотек и их версий. Для этого в среде разработки или в командной строке выполните следующую команду:

   - bash
   - pip freeze > requirements.txt

   - Эта команда создаст файл `requirements.txt` с актуальным списком зависимостей, что позволит программе 
   автоматически установить все необходимые библиотеки в виртуальное окружение при запуске.
   
2. **Запуск**:
   - Переименуйте `run_app.exe` в любое удобное для вас имя, например, в название вашего приложения. 
   Это поможет вам и другим пользователям легко идентифицировать приложение.
   
3. **Выполнение**:
   - Запустите получившийся исполняемый файл. Программа автоматически проверит наличие Python на вашем компьютере, 
   создаст виртуальное окружение, установит все необходимые зависимости из `requirements.txt` и запустит ваш скрипт `main.py`.

### Важно

Программа поддерживает запуск любого проекта, который может работать в виртуальном окружении. 
Однако запуск фреймворков, таких как Django, Flask, FastAPI и других, которые требуют дополнительных настроек 
и запускаются не с помощью скрипта `main.py`, будет реализован в следующих версиях этой утилиты.

## Настройка Утилиты

В этом разделе описывается, как настроить утилиту **Run App** и создать исполняемый файл (`.exe`) 
с помощью `PyInstaller`. Следуйте этим шагам, чтобы подготовить и запустить ваш Python-проект в виде самостоятельного приложения.

### Шаг 1: Установка PyInstaller

Для начала, вам необходимо установить `PyInstaller`, если он еще не установлен. Это можно сделать с помощью команды:

pip install pyinstaller


### Шаг 2: Создание исполняемого файла (exe)

Используйте `PyInstaller`, чтобы создать исполняемый файл для вашего приложения. В командной строке перейдите 
в каталог, где находится ваш файл `run_app.py`, и выполните следующую команду:

pyinstaller --onefile run_app.py


Эта команда создаст исполняемый файл в папке `dist`, который можно переименовать и использовать для запуска вашего приложения.

### Шаг 3: Настройка исполняемого файла

После создания исполняемого файла, переместите его в корневую папку вашего будущего автономного приложения. 
Вы можете переименовать файл его в удобное для вас имя, например, в название вашего приложения. 
создайте папку app и перекопироуйте туда ваш проект-приложение на pithon. Основной файл запуска проекта должен называться main.py.

Не забудьте создать и  переписать в папку app файл requirements.txt

Теперь вы можете запускать ваш проект с помощью утилиты run_app.

### Шаг 4: Тестирование

Запустите созданный исполняемый файл и убедитесь, что приложение работает корректно. Программа автоматически 
создаст виртуальное окружение, установит все зависимости и запустит скрипт `main.py`.

Теперь ваше Python-приложение готово к использованию в виде самостоятельного приложения, 
которое можно запускать на любой машине без необходимости дополнительной настройки.


### Что делать, если Python не установлен на компьютере, на котором нужно запустить приложение

Если Python не установлен на вашей системе, программа предложит вам инструкции по его установке, 
а также предоставит ссылки на скачивание подходящих версий для Windows и macOS.

**Рекомендации по выбору версии Python**:
- Желательно устанавливать Python версии не ниже 3.10.11 для стабильной работы.
- Избегайте установки самых новых версий Python, так как они могут содержать ошибки. Лучше выбрать 
- последнюю стабильную версию из предыдущей линейки (например, 3.11 вместо 3.12).


## Ссылки для скачивания Python

### Python для Windows:
- **Страница загрузок**: [Python Releases for Windows](https://www.python.org/downloads/windows/)
- **Python 3.12.5**: [Скачать](https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe)
- **Python 3.11.8**: [Скачать](https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe)
- **Python 3.10.11**: [Скачать](https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe)

### Python для macOS:
- **Страница загрузок**: [Python Releases for macOS](https://www.python.org/downloads/macos/)
- **Python 3.12.5**: [Скачать](https://www.python.org/ftp/python/3.12.5/python-3.12.5-macos11.pkg)
- **Python 3.11.9**: [Скачать](https://www.python.org/ftp/python/3.11.9/python-3.11.9-macos11.pkg)
- **Python 3.10.11**: [Скачать](https://www.python.org/ftp/python/3.10.11/python-3.10.11-macos11.pkg)

## Лицензия

Этот проект распространяется под [лицензией MIT](LICENSE).