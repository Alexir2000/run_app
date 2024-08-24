import os
import subprocess
import sys

def is_python_installed():
    try:
        version_output = subprocess.check_output(['python', '--version'], text=True)
        print(f"Версия Python, установленная в системе: {version_output.strip()}")
        input("Нажмите Enter для продолжения...")
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        print("Python не установлен на этой системе.")
        input("Нажмите Enter для завершения работы...")
        return False

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

if __name__ == "__main__":
    if is_python_installed():
        activate_venv_and_run()
