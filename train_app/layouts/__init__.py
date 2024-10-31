import os
import importlib

# Получаем имя текущего пакета
package_name = __name__

# Получаем путь к директории пакета
package_dir = os.path.dirname(__file__)

# Список для хранения имен атрибутов, которые будут доступны для импорта
__all__ = []

# Проходим по всем файлам в директории
for filename in os.listdir(package_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        module_name = f"{package_name}.{filename[:-3]}"  # Убираем .py из имени
        module = importlib.import_module(module_name)  # Импортируем модуль

        # Добавляем все классы и функции из модуля в __all__
        for name in dir(module):
            if not name.startswith('_'):  # Игнорируем приватные атрибуты
                __all__.append(name)
                globals()[name] = getattr(module, name)  # Добавляем в глобальное пространство имен

# Теперь все классы и функции из файлов доступны для импорта
