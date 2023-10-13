import json
import pathlib


class Config:
    def __init__(self, names=None, config_path=pathlib.Path.cwd(), config_folder='config'):
        """
        Конструктор класса Config.

        :param names: Имя атрибута (список), используется для создания цепочек атрибутов.
        :param config_path: Путь к папке, где находятся конфигурационные файлы (по умолчанию - текущая директория).
        :param config_folder: Название папки, где хранятся конфигурационные файлы (по умолчанию - 'config').
        """
        if names is None:
            self._names = []
        else:
            self._names = names
        self._config_path = config_path
        self._config_folder = config_folder 

    def __getattr__(self, attr):
        """
        Магический метод для доступа к атрибутам объекта Config.

        :param attr: Имя атрибута.
        :return: Возвращает новый объект Config с обновленным списком атрибутов.
        """
        return Config(self._names + [attr])
    
    def __getitem__(self, key):
        """
        Магический метод для доступа к данным в JSON-файле.

        :param key: Ключ для доступа к данным в JSON-файле.
        :return: Значение, связанное с ключом в JSON-файле.
        """
        data = json.loads(open(str(self), "r").read())
        return data[key]

    def __str__(self):
        """
        Магический метод для получения строкового представления объекта Config.

        :return: Строковое представление пути к JSON-файлу.
        """
        return str(pathlib.PurePath(self._config_path, self._config_folder, *self._names)) + '.json'

# Создаем экземпляр объекта класса Config
object = Config()

def __getattr__(name):
    """
    Функция для доступа к атрибутам объекта Config извне класса.

    :param name: Имя атрибута.
    :return: Возвращает новый объект Config с обновленным списком атрибутов.
    """
    return object.__getattr__(name)
