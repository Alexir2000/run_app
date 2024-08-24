import os
import subprocess
import sys

def check_python_installation():
    try:
        version_output = subprocess.check_output(['python', '--version'], text=True)
        print(f"Версия Python, установленная в системе: {version_output.strip()}")
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        print("Python не установлен на этой системе.")
        return False


def get_venv_python_home(venv_path):
    config_file = os.path.join(venv_path, 'pyvenv.cfg')
    python_home = None

    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            for line in file:
                if line.startswith('home ='):
                    python_home = line.split('=')[1].strip()

        if python_home:
            print(f"Домашний путь Python в виртуальном окружении: {python_home}")
            return python_home
        else:
            raise ValueError(f"Не удалось получить информацию о домашнем пути Python из {config_file}")
    else:
        raise FileNotFoundError(f"Файл {config_file} не найден в виртуальном окружении")


def get_venv_python_version(venv_path):
    config_file = os.path.join(venv_path, 'pyvenv.cfg')
    python_home = None
    python_version = None

    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            for line in file:
                if line.startswith('home ='):
                    python_home = line.split('=')[1].strip()
                elif line.startswith('version_info ='):
                    python_version = line.split('=')[1].strip()

        if python_home and python_version:
            print(f"Домашний путь Python в виртуальном окружении: {python_home}")
            return python_version, python_home
        else:
            raise ValueError("Не удалось получить информацию о версии Python из pyvenv.cfg")
    else:
        raise FileNotFoundError("Файл pyvenv.cfg не найден в виртуальном окружении")


def check_python_home_exists(python_home):
    if os.path.exists(python_home):
        print(f"Версия Python, указанная в виртуальном окружении, установлена в системе: {python_home}")
        return True
    else:
        print(f"Версия Python, указанная в виртуальном окружении, не найдена по пути: {python_home}")
        return False


def install_venv(current_directory):
    venv_path = os.path.join(current_directory, 'app', '.venv')
    try:
        print(f"Создание нового виртуального окружения в {venv_path}...")
        subprocess.Popen([sys.executable, '-m', 'venv', venv_path], shell=True).wait()

        requirements_path = os.path.join(current_directory, 'app', 'requirements.txt')
        if not os.path.exists(requirements_path):
            raise FileNotFoundError("Файл requirements.txt не найден, невозможно установить зависимости.")

        print("Установка зависимостей из requirements.txt...")
        subprocess.Popen(
            [os.path.join(venv_path, 'Scripts', 'python.exe'), '-m', 'pip', 'install', '-r', requirements_path],
            shell=True).wait()

        print("Виртуальное окружение успешно настроено.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при создании виртуального окружения: {e}")
        raise
