import os
import subprocess
import sys
import shutil
from run_app_library import install_venv, check_python_installation, get_venv_python_home, check_python_home_exists

# Этот код работает как надо в части создания и удаления/создания виртуального окружения
# только удалить запуск установки виртуального окружения без открытия нового терминала
# и вернуть путь папки на текущую папку

# Установка пути к текущей папке
current_directory = r"F:\My_Program\Видеоконвертер_app_py"

def is_venv_active():
    if os.environ.get('VIRTUAL_ENV'):
        print("Виртуальное окружение уже активно.")
        return True
    return False

def get_venv_path():
    possible_paths = [
        os.path.join(current_directory, 'app', 'venv'),
        os.path.join(current_directory, 'app', '.venv')
    ]
    for path in possible_paths:
        if os.path.exists(path):
            print(f"Найдено виртуальное окружение в {path}")
            return path
    return None

def main():
    # 1. Проверка установки Python
    if not check_python_installation():
        input("Python не установлен. Нажмите Enter для завершения работы...")
        return

    input("Нажмите Enter для продолжения проверки виртуального окружения...")

    venv_path = get_venv_path()

    # 2. Проверка наличия виртуального окружения
    if not venv_path:
        confirm = input("Виртуальное окружение не найдено. Хотите установить новое? (y/n): ")
        if confirm.lower() == 'y':
            input("Нажмите Enter для продолжения и установки нового виртуального окружения...")
            install_venv(current_directory)
        else:
            input("Установка отменена. Нажмите Enter для завершения работы...")
            return
    else:
        python_home = get_venv_python_home(venv_path)
        if not check_python_home_exists(python_home):
            confirm = input("Версия Python не установлена. Хотите удалить старое виртуальное окружение и установить новое? (y/n): ")
            if confirm.lower() == 'y':
                input(f"Удаление виртуального окружения {venv_path}. Нажмите Enter для продолжения...")
                shutil.rmtree(venv_path)  # Удаление папки виртуального окружения с содержимым
                input("Нажмите Enter для продолжения и установки нового виртуального окружения...")
                install_venv(current_directory)
            else:
                input("Установка отменена. Нажмите Enter для завершения работы...")
                return

    # 3. Проверка наличия requirements.txt
    requirements_path = os.path.join(current_directory, 'app', 'requirements.txt')
    if not os.path.exists(requirements_path):
        input("Файл requirements.txt не найден. Нажмите Enter для завершения работы...")
        return

    input("Нажмите Enter для продолжения...")

    # 4. Проверка активации виртуального окружения
    if is_venv_active():
        input("Виртуальное окружение уже активно. Нажмите Enter для завершения работы...")
        return

    # 5. Активация виртуального окружения и запуск приложения
    print("Активация виртуального окружения и запуск приложения...")
    subprocess.call([os.path.join(python_home, 'python.exe'), os.path.join(current_directory, 'app', 'main.py')])

if __name__ == "__main__":
    main()
