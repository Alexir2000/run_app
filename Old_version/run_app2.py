import os
import subprocess
import sys

def is_venv_active():
    # Проверяем наличие переменной окружения VIRTUAL_ENV
    return os.environ.get('VIRTUAL_ENV') is not None

def activate_venv_and_run():
    if not is_venv_active():
        # Путь к скрипту активации виртуального окружения
        activate_script = os.path.join('app', 'venv', 'Scripts', 'activate.bat')

        if not os.path.exists(activate_script):
            raise FileNotFoundError("Не найден файл активации виртуального окружения в app/venv/Scripts/activate.bat")

        # Формируем команду для активации виртуального окружения и запуска основного скрипта
        command = f'cmd /k "{activate_script} && python app/main.py"'
        print('Запускаем код с виртуальным окружением')
        subprocess.call(command, shell=True)
    else:
        # Если виртуальное окружение уже активировано, запускаем основной скрипт напрямую
        subprocess.call([sys.executable, 'app/main.py'])

activate_venv_and_run()