import os
import subprocess
import sys

# Установка пути к текущей папке
current_directory = r"F:\My_Program\Видеоконвертер_app_py"


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


def check_venv_version():
    try:
        venv_path, config_file = get_venv_path()
        venv_version, python_home = get_venv_python_version(venv_path)
        system_version = subprocess.check_output(['python', '--version'], text=True).strip().split()[1]

        print(f"Системная версия Python: {system_version}")
        print(f"Версия Python в виртуальном окружении: {venv_version}")
        compare_versions(system_version, venv_version)

        return True, python_home
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return False, None


def is_venv_active():
    if os.environ.get('VIRTUAL_ENV'):
        print("Виртуальное окружение уже активно.")
        return True
    return False


def get_venv_path():
    # Определяем пути к возможным местам виртуального окружения
    possible_paths = [
        os.path.join(current_directory, 'app', 'venv'),
        os.path.join(current_directory, 'app', '.venv')
    ]

    for path in possible_paths:
        if os.path.exists(path):
            print(f"Найдено виртуальное окружение в {path}")
            config_file = os.path.join(path, 'pyvenv.cfg')
            if os.path.exists(config_file):
                return path, config_file

    raise FileNotFoundError("Не найдено виртуальное окружение в 'app/venv' или 'app/.venv'")


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
            print(f"Версия Python в виртуальном окружении: {python_version}")
            return python_version, python_home
        else:
            raise ValueError("Не удалось получить информацию о версии Python из pyvenv.cfg")
    else:
        raise FileNotFoundError("Файл pyvenv.cfg не найден в виртуальном окружении")


def compare_versions(system_version, venv_version):
    if system_version == venv_version:
        print(f"Версии Python совпадают: {system_version}")
    else:
        print(
            f"Версии Python не совпадают. Системная версия: {system_version}, версия в виртуальном окружении: {venv_version}")


def check_python_home_exists(python_home):
    if os.path.exists(python_home):
        print(f"Версия Python, указанная в виртуальном окружении, установлена в системе: {python_home}")
        return True
    else:
        print(f"Версия Python, указанная в виртуальном окружении, не найдена по пути: {python_home}")
        return False


def main():
    # 1. Проверка установки Python
    if not check_python_installation():
        input("Python не установлен. Нажмите Enter для завершения работы...")
        return

    input("Нажмите Enter для продолжения проверки виртуального окружения...")

    # 2. Проверка версий в виртуальном окружении
    venv_valid, python_home = check_venv_version()
    if not venv_valid:
        input("Ошибка в проверке виртуального окружения. Нажмите Enter для завершения работы...")
        return

    input("Нажмите Enter для продолжения проверки наличия домашней директории Python...")

    # 3. Проверка существования домашней директории Python
    if not check_python_home_exists(python_home):
        input("Нужная версия Python не установлена. Нажмите Enter для завершения работы...")
        return

    input("Нажмите Enter для продолжения проверки активации виртуального окружения...")

    # 4. Проверка активации виртуального окружения
    if is_venv_active():
        input("Виртуальное окружение уже активно. Нажмите Enter для завершения работы...")
        return

    # 5. Логика запуска основного скрипта, если всё в порядке
    # subprocess.call([os.path.join(python_home, 'python.exe'), os.path.join(current_directory, 'app', 'main.py')])


if __name__ == "__main__":
    main()
