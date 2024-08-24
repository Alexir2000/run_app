import os
import subprocess
import sys

def is_venv_active():
    return os.environ.get('VIRTUAL_ENV') is not None

def get_venv_path():
    # Определяем пути к возможным местам виртуального окружения
    possible_paths = ['app/venv', 'app/.venv']

    for path in possible_paths:
        python_executable = os.path.join(path, 'Scripts', 'python.exe')
        if os.path.exists(python_executable):
            return python_executable

    raise FileNotFoundError("Не найден Python интерпретатор в 'app/venv' или 'app/.venv'")

def activate_venv_and_run():
    if not is_venv_active():
        # Получаем путь к интерпретатору Python внутри виртуального окружения
        python_executable = get_venv_path()

        # Запускаем основной скрипт используя интерпретатор из виртуального окружения
        subprocess.call([python_executable, 'app/main.py'])
    else:
        subprocess.call([sys.executable, 'app/main.py'])

activate_venv_and_run()
