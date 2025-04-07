import json
import os

def merge_sticker_files():
    # Список для хранения всех стикеров
    all_stickers = []
    
    # Перебираем все файлы в текущей директории
    for filename in os.listdir('.'):
        if filename.startswith('stickers_with_prices') and filename.endswith('.json'):
            try:
                # Читаем каждый файл
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Добавляем стикеры из файла в общий список
                    all_stickers.extend(data.get('data', []))
                print(f"Обработан файл: {filename}")
            except Exception as e:
                print(f"Ошибка при обработке файла {filename}: {str(e)}")
    
    # Сохраняем объединенный результат
    with open('all_stickers_with_prices.json', 'w', encoding='utf-8') as f:
        json.dump({'data': all_stickers}, f, ensure_ascii=False, indent=4)
    
    print(f"\nГотово! Всего объединено {len(all_stickers)} стикеров")
    print("Результат сохранен в all_stickers_with_prices.json")

if __name__ == "__main__":
    merge_sticker_files() 