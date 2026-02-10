from os import listdir
from os.path import realpath, dirname
from os.path import join

def get_full_path_to_file(filename=None):
    """
    Получить абсолютный путь к файлу в директории templates
    Если файл не существует, создать путь для него
    """

    # Получить путь к директории flat files
    flat_files_dir = dirname(realpath(__file__))

    # Если имя файла не указано, вернуть путь к директории
    if filename is None:
        return flat_files_dir

    # Всегда возвращаем полный путь, даже если файл не существует

    return join(flat_files_dir, filename)
