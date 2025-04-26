import subprocess
import pytest
import pytest_gitpull

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Цей hook працює для будь-якого виклику pytest, навіть із параметрами
    print("Виконується git pull перед тестами...")
    result = subprocess.run(["git", "pull"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("Помилка при виконанні git pull:", result.stderr)
