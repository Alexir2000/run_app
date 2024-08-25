# Основной файл run_app.py
#  версия: 1.1.0

import os
import subprocess
import sys
import shutil
from run_app_library import (install_venv, check_python_installation,
                             get_venv_python_home, check_python_home_exists, info_install_python)

# В проекте приложения, перед запуском
# выполнить команду: pip freeze > requirements.txt

# Задайте значение переменной app_path:
# "" - если папка с окружением и скрипт находятся в корне;
# "app" - если папка с окружением и скрипт находятся в подпапке app.

app_path = ""
# app_path = "app" # закомментируйте эту строку, если папка с окружением и скрипт находятся в корне
#  и раскомментируйте строку выше, если папка с окружением и скрипт находятся в подпапке app

# Установка пути к текущей папке
current_directory = ""

def is_venv_active():
    if os.environ.get('VIRTUAL_ENV'):
        return True
    return False

def get_full_path(relative_path):
    """Формирует полный путь в зависимости от значения app_path"""
    return os.path.join(current_directory, app_path, relative_path)

def get_venv_path():
    possible_paths = [
        get_full_path('venv'),
        get_full_path('.venv')
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

def main():

    # 1. Проверка установки Python
    if not check_python_installation():
        print("Python не установлен. Установите его и повторите попытку.\n")
        info_install_python()
        input(" \n Нажмите Enter для завершения работы...")
        return

    venv_path = get_venv_path()

    # 2. Проверка наличия виртуального окружения
    if not venv_path:
        confirm = input("Виртуальное окружение с библиотеками для приложения не найдено. \n Хотите установить новое? (y/n): ")
        if confirm.lower() == 'y':
            install_venv(current_directory, app_path)
            input("\n Новое окружение с библиотеками установлено. Нажмите Enter для продолжения работы...\n")
            venv_path = get_venv_path()
        else:
            input("Установка отменена. Нажмите Enter для завершения работы...")
            return
    else:
        python_home = get_venv_python_home(venv_path)
        if not check_python_home_exists(python_home):
            confirm = input("Версия Python указанная в настройках приложения не найдена в системе. \n "
                            "Нужно переустановить библиотеки приложения для текущей версии Python. \n "
                            "Хотите удалить старое виртуальное окружение с библиотеками "
                            "и установить новое? (y/n): ")
            if confirm.lower() == 'y':
                shutil.rmtree(venv_path)  # Удаление папки виртуального окружения с содержимым
                input(f"Старое окружение с библиотеками удалено. \n"
                      f"Нажмите Enter для установки нового окружения с библиотеками ...")
                install_venv(current_directory, app_path)
                input("\n Новое окружение с библиотеками установлено. Нажмите Enter для продолжения работы...\n")
            else:
                input("Установка отменена. Нажмите Enter для завершения работы...")
                return

    # 4. Проверка активации виртуального окружения
    if is_venv_active():
        input("Виртуальное окружение уже активно.\n "
              "Возможно программа запущена из другого виртуального окружения.\n "
              "Программа может работать некуорректно.\n "
              " Нажмите Enter для завершения работы...")
        return

    # 5. Активация виртуального окружения и запуск приложения
    subprocess.call([os.path.join(venv_path, 'Scripts', 'python.exe'), get_full_path('main.py')])
    # input("Нажмите Enter для завершения работы...")


if __name__ == "__main__":
    main()
