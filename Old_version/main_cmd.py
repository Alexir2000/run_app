import subprocess
import sys
import os
# Это функция которая запускает терминал с текущим виртуальным окружением.
def open_terminal_in_venv():
    # Получаем путь к текущему виртуальному окружению
    venv_path = sys.prefix

    # Определяем, какая операционная система используется
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(venv_path, 'Scripts', 'activate.bat')
        # Запускаем cmd с активацией виртуального окружения
        subprocess.run(['cmd.exe', '/k', activate_script])
    else:  # Unix or MacOS
        activate_script = os.path.join(venv_path, 'bin', 'activate')
        # Запускаем bash с активацией виртуального окружения
        subprocess.run(['bash', '--rcfile', activate_script])


open_terminal_in_venv()