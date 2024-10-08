# Основной файл run_app.py
# версия   1.2.0

import os
import subprocess
import sys
import shutil
from run_app_library import (install_venv, check_python_installation,
                             get_venv_python_home, check_python_home_exists, info_install_python)

# Установка пути к текущей папке
current_directory = ""
app_path = ""  # Переменная будет определяться в функции set_path()

def is_venv_active():
    if os.environ.get('VIRTUAL_ENV'):
        return True
    return False

def get_venv_path(app_path):
    """Поиск виртуального окружения в заданном app_path"""
    possible_paths = [
        os.path.join(current_directory, app_path, 'venv'),
        os.path.join(current_directory, app_path, '.venv')
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

def set_path():
    """Определяет и задает значение app_path в зависимости от структуры проекта"""
    global app_path

    # Шаг 1: Поиск main.py в текущей папке
    if os.path.exists(os.path.join(current_directory, 'main.py')):
        app_path = ""
    else:
        # Шаг 2: Поиск папки app и файла main.py внутри нее
        app_folder = os.path.join(current_directory, 'app')
        if not os.path.exists(app_folder):
            print("Приложение для запуска нигде не найдено")
            input("Нажмите Enter для завершения работы...")
            sys.exit(1)

        if os.path.exists(os.path.join(app_folder, 'main.py')):
            app_path = "app"
        else:
            print("Приложение для запуска нигде не найдено")
            input("Нажмите Enter для завершения работы...")
            sys.exit(1)

    # Шаг 3: Проверка виртуального окружения и файла requirements.txt
    venv_path = get_venv_path(app_path)
    if not venv_path:
        requirements_path = os.path.join(current_directory, app_path, 'requirements.txt')
        if not os.path.exists(requirements_path):
            print("Виртуальное окружение не найдено, и отсутствует файл requirements.txt для его создания.\n "
                  "Приложение не может быть запущено.")
            input("Нажмите Enter для завершения работы...")
            sys.exit(1)

def get_full_path(relative_path):
    """Формирует полный путь в зависимости от значения app_path"""
    return os.path.join(current_directory, app_path, relative_path)

def main():

    # Определение app_path
    set_path()

    # 1. Проверка установки Python
    if not check_python_installation():
        print("Python не установлен. Установите его и повторите попытку.\n")
        info_install_python()
        input(" \n Нажмите Enter для завершения работы...")
        return

    venv_path = get_venv_path(app_path)

    # 2. Проверка наличия виртуального окружения
    if not venv_path:
        confirm = input("Виртуальное окружение с библиотеками для приложения не найдено. \n Хотите установить новое? (y/n): ")
        if confirm.lower() == 'y':
            install_venv(current_directory, app_path)
            input("\n Новое окружение с библиотеками установлено. Нажмите Enter для продолжения работы...\n")
            venv_path = get_venv_path(app_path)
        else:
            input("Установка отменена. Нажмите Enter для завершения работы...")
            return
    else:
        python_home = get_venv_python_home(venv_path)
        if not check_python_home_exists(python_home):
            confirm = input("Версия Python, указанная в настройках приложения, не найдена в системе. \n "
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
              "Программа может работать некорректно.\n "
              " Нажмите Enter для завершения работы...")
        return

    # 5. Активация виртуального окружения и запуск приложения
    subprocess.call([os.path.join(venv_path, 'Scripts', 'python.exe'), get_full_path('main.py')])
    # input("Нажмите Enter для завершения работы...")


if __name__ == "__main__":
    main()
