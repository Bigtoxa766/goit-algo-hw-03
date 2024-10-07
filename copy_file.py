
import os
import shutil
import argparse

# Функція для копіювання файлів рекурсивно
def copy_files_recursively(src_dir, dest_dir):
    try:
        # Перебираємо всі елементи у вихідній директорії
        for item in os.listdir(src_dir):
            src_item_path = os.path.join(src_dir, item)
            
            # Якщо це директорія, викликаємо функцію рекурсивно
            if os.path.isdir(src_item_path):
                copy_files_recursively(src_item_path, dest_dir)
            else:
                # Отримуємо розширення файлу
                file_extension = os.path.splitext(item)[1][1:].lower()
                
                # Якщо розширення відсутнє, використовуємо "unknown"
                if not file_extension:
                    file_extension = "unknown"
                
                # Створюємо піддиректорію в директорії призначення
                dest_subdir = os.path.join(dest_dir, file_extension)
                os.makedirs(dest_subdir, exist_ok=True)
                
                # Копіюємо файл у відповідну піддиректорію
                dest_item_path = os.path.join(dest_subdir, item)
                shutil.copy2(src_item_path, dest_item_path)
                print(f"Копіюється файл {src_item_path} до {dest_item_path}")
    
    except Exception as e:
        print(f"Виникла помилка при копіюванні файлів: {e}")

# Основна функція для парсингу аргументів і виклику копіювання
def main():
    # Створюємо парсер для аргументів командного рядка
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання файлів із сортуванням за розширеннями.")
    parser.add_argument("source_dir", help="Шлях до вихідної директорії.")
    parser.add_argument("dest_dir", nargs='?', default="dist", help="Шлях до директорії призначення (за замовчуванням dist).")
    
    # Парсимо аргументи
    args = parser.parse_args()
    src_dir = args.source_dir
    dest_dir = args.dest_dir

    # Перевіряємо, чи існує вихідна директорія
    if not os.path.exists(src_dir):
        print(f"Вихідна директорія {src_dir} не існує.")
        return

    # Створюємо директорію призначення, якщо вона не існує
    os.makedirs(dest_dir, exist_ok=True)
    
    # Викликаємо функцію рекурсивного копіювання
    copy_files_recursively(src_dir, dest_dir)

# Точка входу в програму
# Запуск скрипта "python copy_file.py src_dir dest_dir"
if __name__ == "__main__":
    main()
