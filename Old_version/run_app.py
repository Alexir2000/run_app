import os
import subprocess
import sys

def is_venv_active():
    return os.environ.get('VIRTUAL_ENV') is not None

def activate_venv_and_run():
    if not is_venv_active():
        # Путь к интерпретатору Python внутри виртуального окружения
        python_executable = os.path.join('app', 'venv', 'Scripts', 'python.exe')

        if not os.path.exists(python_executable):
            raise FileNotFoundError("Не найден Python интерпретатор в app/venv/Scripts/python.exe")

        # Запускаем основной скрипт используя интерпретатор из виртуального окружения
        subprocess.call([python_executable, 'app/main.py'])
    else:
        subprocess.call([sys.executable, 'app/main.py'])

activate_venv_and_run()