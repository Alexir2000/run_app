import os
import subprocess
import sys
import shutil
import requests


def is_venv_active():
    return os.environ.get('VIRTUAL_ENV') is not None


def get_python_version(venv_path):
    python_executable = os.path.join(venv_path, 'Scripts', 'python.exe')
    if not os.path.exists(python_executable):
        raise FileNotFoundError(f"Не найден Python интерпретатор в {python_executable}")

    version_output = subprocess.check_output([python_executable, '--version'], text=True)
    version = version_output.strip().split()[1]  # Предполагается формат 'Python 3.x.x'
    return version


def is_python_installed(version):
    try:
        output = subprocess.check_output(['py', f'-{version}', '--version'], text=True)
        return True
    except subprocess.CalledProcessError:
        return False


def download_and_install_python(version):
    python_installers = {
        '3.10': 'https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe',
        # Добавьте ссылки на другие версии Python, если необходимо
    }

    if version not in python_installers:
        raise ValueError(f"Нет ссылки для автоматической установки Python версии {version}")

    installer_url = python_installers[version]
    installer_path = f"python-{version}-installer.exe"

    # Скачиваем установщик Python
    response = requests.get(installer_url, stream=True)
    with open(installer_path, 'wb') as file:
        shutil.copyfileobj(response.raw, file)

    print(f"Скачан установщик Python версии {version}. Запускаю установку...")

    # Запускаем установщик
    subprocess.run([installer_path, '/quiet', 'InstallAllUsers=1', 'PrependPath=1'])

    # Удаляем установщик после установки
    os.remove(installer_path)


def activate_venv_and_run():
    venv_path = os.path.join('app', 'venv')
    if not is_venv_active():
        python_version = get_python_version(venv_path)

        if not is_python_installed(python_version):
            user_input = input(f"Python версии {python_version} не установлен. Установить? (y/n): ")
            if user_input.lower() == 'y':
                download_and_install_python(python_version)
            else:
                print("Установка Python отменена. Скрипт не будет запущен.")
                sys.exit(1)

        # Путь к интерпретатору Python внутри виртуального окружения
        python_executable = os.path.join(venv_path, 'Scripts', 'python.exe')

        # Запускаем основной скрипт, используя интерпретатор из виртуального окружения
        subprocess.call([python_executable, 'app/main.py'])
    else:
        subprocess.call([sys.executable, 'app/main.py'])


activate_venv_and_run()
