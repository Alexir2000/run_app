# Run App

[![Русский](https://img.shields.io/badge/language-Русский-blue.svg)](README.md)
[![English](https://img.shields.io/badge/language-English-red.svg)](README_EN.md)

The English version of this README can be found [here](README_EN.md).

**Run App** — это универсальная утилита, которая делает выполнение Python-скриптов таким же простым, как запуск любого другого 
приложения на вашем компьютере. С помощью этой программы вы можете превратить свои Python-скрипты в полноценные приложения, 
которые запускаются одним кликом, без необходимости ручной активации виртуального окружения или установки Python на вашу систему.

Утилита НЕ требует превращения скриптов на python в исполняемые файлы. 

Никакие модификации кода python-приложений не требуются. Достаточно просто перекопировать код необходимого приложения 
в отдельную папку и можно запускать код как полноценное Windows или MacOS приложение.

[Подробнее о Run App](README_Folder/about_run_app.md)

[Исполняемый файл утилиты Run App для Windows можно скачать отсюда](https://disk.yandex.ru/d/PbwuS2Vo3z7qKw)


### Run App: Новые горизонты для разработки прикладных приложений на Python

Представьте себе мир, где разработка прикладных программ для персональных компьютеров на Python не ограничена 
необходимостью компиляции кода в исполняемые файлы. Где изменения в коде можно вносить в реальном времени, 
не беспокоясь о длительных процессах упаковки и сборки. **Run App** открывает новые возможности для использования 
Python как полноценного инструмента для разработки приложений на ПК.

Подход с использованием утилиты является наиболее простым, так как **не требует запуска приложения через 
командную строку и настройки виртуального окружения.** 

**Run App** по сути является надстройкой над приложением, которая **запускается, например, по ярлыку на рабочем столе**, 
и активирует основное приложение. 

**Свобода от компиляции**: Одним из главных преимуществ **Run App** является возможность запускать Python-программы 
без необходимости компиляции их в .exe файлы. Это означает, что вы можете легко вносить изменения в код, 
добавлять новый функционал, исправлять баги, и программа может тут же запускаться пользователем на этом компьютере 
или просто обновляться через репозиторий на другом компьютере. Не нужно тратить время на перекомпиляцию или упаковку
приложения каждый раз, когда вы хотите что-то изменить. Этот подход особенно ценен на этапах начальной поддержки 
и тестирования, когда частые изменения неизбежны.

Теперь вам не нужно разбираться в сложных настройках компиляции или беспокоиться о совместимости различных 
версий библиотек при создании исполняемых файлов. Достаточно скопировать ваш проект на новый компьютер, 
и он будет готов к запуску с минимальными усилиями. Все, что нужно, — это установленный Python.

**Подходит для любых задач**: **Run App** идеально подходит для широкого спектра задач: от небольших утилит и 
автоматизированных скриптов до сложных приложений с графическим интерфейсом. Она позволяет быстро разворачивать, 
 и распространять приложения, не отвлекаясь на технические детали компиляции. 
Если ваше приложение требует регулярных обновлений и модификаций, **Run App** станет вашим незаменимым инструментом.

**Минус только один**: исходный код приложения всегда на виду, он открыт и любой, кто имеет доступ к папке с приложением,
может его изменить или поправить. Если Вам необходимо сохранить исходный код приложения закрытым,
то это утилита Вам не подойдет.

## Область применения

**Run App** — это утилита, предназначенная для использования на персональных компьютерах, чтобы создавать и 
запускать Python-приложения без необходимости вникать в особенности запуска и работы с Python или настраивать 
виртуальные окружения на каждом устройстве. Она не предназначена для работы на серверах или для удаленной установки,
но идеально подходит для широкого круга задач, выполняемых на локальных машинах.

**Run App** по сути является надстройкой над приложением, которая запускается, например, по ярлыку на рабочем столе, 
и активирует основное приложение. 

Утилита НЕ требует превращения скриптов на python в исполняемые файлы.

**Run App** значительно упрощает работу с Python-приложениями на персональных компьютерах, делая их доступными 
для более широкого круга пользователей, независимо от их технической подготовки. Утилита позволяет быстро и 
удобно запускать Python-скрипты в виде полноценных приложений, обеспечивая их стабильную работу без необходимости вникать 
в особенности  работы с Python и настройки окружений.


### Примеры использования

1. **Автоматизация задач на рабочем месте**:
    - Создание скриптов для автоматизированного управления документами и таблицами, размещенными в облачных сервисах, 
   таких как Google Drive или OneDrive. Эти скрипты могут автоматически загружать, изменять или обновлять файлы,
   выполняя задачи по расписанию или при необходимости.

2. **Парсинг сайтов**:
    - Вы можете создать парсер, который будет собирать данные с различных веб-сайтов, например, для мониторинга цен, 
   сбора новостей или анализа конкурентов. Такой парсер можно запускать с любого компьютера или даже с флешки, 
   обеспечивая мобильность и независимость от конкретной рабочей станции.

3. **Управление локальными данными**:
    - Запуск утилиты для автоматизированного резервного копирования важных данных, управления файлами и папками на 
   локальном диске или облаке, синхронизации данных между устройствами и многого другого.

4. **Специализированные задачи для профессионалов**:
    - Разработка утилит для инженеров, аналитиков, дизайнеров и других профессионалов, которые требуют выполнения 
   специфических действий с определенными данными или приложениями, например, для автоматизации обработки данных, 
   генерации отчетов, преобразования файлов в различные форматы и многое другое.

5. **Работа с базами данных**:
    - Утилита может быть использована для создания локальных приложений, которые подключаются к удаленным базам данных,
   выполняют анализ данных, генерируют отчеты или импортируют/экспортируют данные.

6. **Образовательные проекты**:
    - Идеально подходит для студентов и преподавателей, которым нужно демонстрировать или тестировать 
   Python-код без необходимости настраивать среду Python на каждом компьютере. 
   Это упрощает процесс распространения и использования учебных материалов.

7. **Переносимые приложения**:
    - Создание приложений, которые можно запускать с внешнего носителя, например, с USB-флешки. 
   Это позволяет легко перемещать приложение между разными компьютерами. 
   Требуется только наличие установленного python на компьютере.


## Почему это полезно?

Многие разработчики сталкиваются с проблемой запуска своих Python-приложений на компьютерах, 
где затруднительно настроить виртуальное окружение и среду Python, или где его версия не совпадает с той, 
которая требуется приложению. **Run App** решает эту проблему, предлагая инструмент, 
который не только запускает Ваш скрипт как независимое приложение, но и автоматически настраивает виртуальное окружение, 
устанавливает необходимые зависимости и гарантирует, что Ваше приложение будет работать стабильно и без проблем.

Эта утилита полезна для:
- **Разработчиков**, которым нужно предоставить свои скрипты клиентам или коллегам, не знакомым с настройкой Python и запуском кода.
- **Системных администраторов**, которым важно, чтобы приложения запускались корректно на любой машине без дополнительных настроек.
- **Обучения и тестирования**, когда важно быстро запускать скрипты на разных системах с минимальными требованиями.

## Особенности

- **Выполнение Python-скриптов как приложений**: Используйте свои Python-скрипты как исполняемые файлы без необходимости 
   их компилировать или модифицировать, которые можно запускать прямо с рабочего стола.
  - **Автоматическая настройка виртуального окружения**: Программа автоматически создаёт виртуальное окружение в каталоге `app`,
   если оно ещё не создано.
- **Управление зависимостями**: Программа устанавливает все необходимые зависимости, указанные в файле `requirements.txt`, 
  в виртуальное окружение.
- **Кроссплатформенная совместимость**: Утилита Единожды компилируется в EXE-файл и работает на Windows и macOS, 
   обеспечивая единообразие выполнения скриптов на разных операционных системах.
- **Run App** по сути является надстройкой над приложением, которая запускается, например, по ярлыку на рабочем столе, 
и активирует основное приложение. 

## Как это работает

Утилита один раз компилируется в EXE-файл и подходит для запуска любых проектов. 

Предназначена для выполнения Python-скрипта с именем `main.py`, который должен находиться в подпапке `app`. 

Другие файлы и папки проекта также должны находится в подпапке `app` (в версии run_app) либо как обычно, в папке проекта( в версии run_app_project). В этом случае файл утилиты должет находится так же в корневой папке проекта. Версия утилиты и способ ее использования задается при ее компилляции.

Для установки всех необходимых зависимостей требуется также файл `requirements.txt` в той же папке в которой находятся файлы и папки проекта.

### Пример структуры проекта версии run_app:

your_project/

├── app/

│   ├── main.py

│   ├── requirements.txt

└── run_app.exe

В этой структуре ( в версии run_app):
   - **`your_project`**: Папка с Вашим проектом-приложением, которое будет запускаться как независимое приложение
   - **`app/`**: Папка, содержащая основное приложение.
  - **`app/main.py`**: Основной скрипт Python Вашего проекта, который будет выполняться.
  - **`app/requirements.txt`**: Файл с зависимостями, которые необходимо установить для работы скрипта.
- **`run_app.exe`**: Исполняемый файл, который запускает Ваше приложение.

В версии run_app_project файл утилиты run-app просто должен находится в коревой папке проекта.

### Дополнительные рекомендации

Для удобства вы можете переименовать `run_app.exe` в название вашего приложения. Например, 
если ваше приложение называется "Video Converter", вы можете переименовать файл в `VideoConverter.exe`. 
Затем вы можете создать ярлык на рабочем столе или в меню «Пуск» и запускать приложение так же, 
как и любое другое стандартное приложение. Это делает использование вашего Python-скрипта более удобным 
для конечного пользователя, скрывая технические детали работы с Python.

[Инструкция по установке настройке и использованию доступна здесь](README_Folder/Instructions.md)


### Что делать, если Python не установлен на компьютере, на котором нужно запустить приложение

Если Python не установлен на вашей системе, программа предложит вам инструкции по его установке, 
а также предоставит ссылки на скачивание подходящих версий для Windows и macOS.

**Рекомендации по выбору версии Python**:
- Желательно устанавливать Python версии не ниже 3.10.11 для стабильной работы.
- Избегайте установки самых новых версий Python, так как они могут содержать ошибки. Лучше выбрать 
  последнюю стабильную версию из предыдущей линейки (например, 3.11 вместо 3.12).


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