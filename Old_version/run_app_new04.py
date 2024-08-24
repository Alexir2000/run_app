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
        if os.path.exists(path):
            print(f"Найдено виртуальное окружение в {path}")
            python_executable = os.path.join(path, 'Scripts', 'python.exe')
            if os.path.exists(python_executable):
                return path, python_executable

    raise FileNotFoundError("Не найдено виртуальное окружение в 'app/venv' или 'app/.venv'")


def get_venv_python_version(venv_path):
    try:
        version_output = subprocess.check_output([os.path.join(venv_path, 'Scripts', 'python.exe'), '--version'],
                                                 text=True)
        return version_output.strip().split()[1]
    except subprocess.CalledProcessError:
        raise RuntimeError("Не удалось получить версию Python из виртуального окружения.")


def compare_versions(system_version, venv_version):
    if system_version == venv_version:
        print(f"Версии Python совпадают: {system_version}")
    else:
        print(
            f"Версии Python не совпадают. Системная версия: {system_version}, версия в виртуальном окружении: {venv_version}")


def activate_venv_and_run():
    if not is_venv_active():
        # Получаем путь к интерпретатору Python внутри виртуального окружения
        venv_path, python_executable = get_venv_path()

        # Получаем версию Python в системе и в виртуальном окружении
        system_version = subprocess.check_output(['python', '--version'], text=True).strip().split()[1]
        venv_version = get_venv_python_version(venv_path)

        # Сравниваем версии
        compare_versions(system_version, venv_version)
        input("Нажмите Enter для продолжения...")

        # Запускаем основной скрипт, используя интерпретатор из виртуального окружения
        subprocess.call([python_executable, 'app/main.py'])
    else:
        subprocess.call([sys.executable, 'app/main.py'])


if __name__ == "__main__":
    if is_python_installed():
        activate_venv_and_run()
