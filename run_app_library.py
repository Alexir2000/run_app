import os
import subprocess
import sys


def check_python_installation():
    try:
        subprocess.check_output(['python', '--version'], text=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
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
            return python_home
        else:
            raise ValueError(f"Не удалось получить информацию о домашнем пути Python из {config_file}")
    else:
        raise FileNotFoundError(f"Файл {config_file} не найден в виртуальном окружении")


def check_python_home_exists(python_home):
    return os.path.exists(python_home)


def install_venv(current_directory):
    venv_path = os.path.join(current_directory, 'app', '.venv')
    try:
        print(f"Создание нового виртуального окружения в {venv_path}...")
        subprocess.call(['python', '-m', 'venv', venv_path], shell=True)

        requirements_path = os.path.join(current_directory, 'app', 'requirements.txt')
        if not os.path.exists(requirements_path):
            raise FileNotFoundError("Файл requirements.txt не найден, невозможно установить зависимости.")

        print("Установка зависимостей из requirements.txt...")
        subprocess.call(
            [os.path.join(venv_path, 'Scripts', 'python.exe'), '-m', 'pip', 'install', '-r', requirements_path],
            shell=True
        )
        print("Виртуальное окружение успешно настроено.")

        if os.path.exists(venv_path):
            print(f"Виртуальное окружение успешно создано в {venv_path}.")
        else:
            print("Не удалось создать виртуальное окружение.")
            sys.exit(1)  # Завершаем работу с ошибкой, если окружение не создано

        return venv_path  # Вернуть путь к новому окружению

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ошибка при создании виртуального окружения: {e}")

def info_install_python():
    message = """
    Выберите версию python на странице загрузок
    или перейдите сразу к скачиванию по прямым ссылкам.
    Для стабильной работы желательно устанавливать версию python не ниже 3.10.11
    А так же не устанавливать самую последнюю версию (если иное не рекомендовано дополнительно).
    Например, если доступна к скачиванию линейка версий 3.12.хх,
    то лучше скачивать самую последнюю версию из линейки 3.11.ххх

    Тут представлены прямые ссылки для скачивания последних версий 
    линеек python 3.10, 3.11, 3.12 по состоянию на 06 августа 2024г.

    Python Releases for Windows:
    https://www.python.org/downloads/windows/

    Python 3.12.5 - Aug. 6, 2024
    https://www.python.org/ftp/python/3.12.5/python-3.12.5-amd64.exe

    Python 3.11.8 - Feb. 6, 2024
    https://www.python.org/ftp/python/3.11.8/python-3.11.8-amd64.exe

    Python 3.10.11 - April 5, 2023
    https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe

    >>><<<

    Python Releases for macOS:
    https://www.python.org/downloads/macos/

    Python 3.12.5 - Aug. 6, 2024
    https://www.python.org/ftp/python/3.12.5/python-3.12.5-macos11.pkg

    Python 3.11.9 - April 2, 2024
    https://www.python.org/ftp/python/3.11.9/python-3.11.9-macos11.pkg

    Python 3.10.11 - April 5, 2023
    https://www.python.org/ftp/python/3.10.11/python-3.10.11-macos11.pkg
    """
    print(message)
