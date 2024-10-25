import os

def check_path(base_folder):
    required_folders = ['citadel_attributes', 'citadel_heroes', 'citadel_mods']
    for folder in required_folders:
        folder_path = os.path.join(base_folder, folder)
        if not os.path.isdir(folder_path):
            print(f"Папка {folder} не найдена в указанном пути: {base_folder}")
            return False
    return True

# Запрашиваем путь к папке localization
base_folder = input('Enter Path to localization: ')

# Проверяем, существуют ли необходимые папки
if not check_path(base_folder):
    print("Указанный путь неверен. Пожалуйста, проверьте путь и попробуйте снова.")
    input('Press any button to close')
    exit(1)

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
    if os.path.exists(russian_path):
        os.rename(russian_path, english_path)
        print(f"Переименован {russian_file} в {english_file}")

# Работа с папкой citadel_attributes
process_files(attributes_folder, attributes_english, attributes_russian)

# Работа с папкой citadel_heroes
process_files(heroes_folder, heroes_english, heroes_russian)

# Работа с папкой citadel_mods
process_files(mods_folder, mods_english, mods_russian)

input('Press any button to close')
