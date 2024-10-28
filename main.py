import os
import sys

def get_config_file_path():
    """Возвращает путь к файлу конфигурации рядом с .exe или в папке AppData."""
    # Способ 1: Сохранение рядом с .exe
    if getattr(sys, 'frozen', False):  # Если программа скомпилирована в .exe
        # Рядом с .exe файлом
        return os.path.join(os.path.dirname(sys.executable), 'path_config.txt')
    
    # Способ 2: Сохранение в AppData (раскомментируйте, если хотите использовать AppData)
    # appdata_dir = os.getenv('APPDATA')  # Например, C:\Users\<User>\AppData\Roaming
    # config_dir = os.path.join(appdata_dir, 'MyApp')  # Папка вашего приложения
    # os.makedirs(config_dir, exist_ok=True)  # Создаем папку, если она не существует
    # return os.path.join(config_dir, 'path_config.txt')

    # Если программа запускается как .py файл, сохраняем в текущей папке
    return 'path_config.txt'

CONFIG_FILE = get_config_file_path()

def save_path(base_folder):
    """Сохраняет путь в файл конфигурации."""
    with open(CONFIG_FILE, 'w') as file:
        file.write(base_folder)

def load_path():
    """Загружает путь из файла конфигурации, если он существует."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            return file.read().strip()
    return None

def check_path(base_folder):
    required_folders = ['citadel_attributes', 'citadel_heroes', 'citadel_mods']
    for folder in required_folders:
        folder_path = os.path.join(base_folder, folder)
        if not os.path.isdir(folder_path):
            print(f"Папка {folder} не найдена в указанном пути: {base_folder}")
            return False
    return True

# Загружаем сохранённый путь или запрашиваем его у пользователя
base_folder = load_path()
if base_folder is None or not check_path(base_folder):
    base_folder = input('Enter Path to localization: ')
    if not check_path(base_folder):
        print("Указанный путь неверен. Пожалуйста, проверьте путь и попробуйте снова.")
        input('Press any button to close')
        exit(1)
    save_path(base_folder)  # Сохраняем введённый пользователем путь

# Пути к папкам localization\citadel_attributes, localization\citadel_heroes и localization\citadel_mods
attributes_folder = os.path.join(base_folder, 'citadel_attributes')
heroes_folder = os.path.join(base_folder, 'citadel_heroes')
mods_folder = os.path.join(base_folder, 'citadel_mods')

attributes_english = 'citadel_attributes_english.txt'
attributes_russian = 'citadel_attributes_russian.txt'
heroes_english = 'citadel_heroes_english.txt'
heroes_russian = 'citadel_heroes_russian.txt'
mods_english = 'citadel_mods_english.txt'
mods_russian = 'citadel_mods_russian.txt'

def process_files(folder, english_file, russian_file):
    english_path = os.path.join(folder, english_file)
    russian_path = os.path.join(folder, russian_file)

    # Проверка наличия русского файла
    if not os.path.exists(russian_path):
        print(f"Файл {russian_file} не найден. Все уже в порядке.")
        return

    # Удаление английского файла
    if os.path.exists(english_path):
        os.remove(english_path)
        print(f"Удалён файл: {english_file}")

    # Переименование русского файла
    os.rename(russian_path, english_path)
    print(f"Переименован {russian_file} в {english_file}")

# Работа с папками
process_files(attributes_folder, attributes_english, attributes_russian)
process_files(heroes_folder, heroes_english, heroes_russian)
process_files(mods_folder, mods_english, mods_russian)

input('Press any button to close')
