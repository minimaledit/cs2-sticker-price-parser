import json

def sort_stickers_by_id():
    try:
        # Читаем исходный файл
        with open('all_stickers_with_prices.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Получаем список стикеров
        stickers = data.get('data', [])
        
        # Сортируем стикеры по ID (преобразуем ID в число для корректной сортировки)
        sorted_stickers = sorted(stickers, key=lambda x: int(x['id']))
        
        # Сохраняем отсортированный результат
        with open('all_stickers_with_prices_sorted.json', 'w', encoding='utf-8') as f:
            json.dump({'data': sorted_stickers}, f, ensure_ascii=False, indent=4)
        
        print(f"\nГотово! Отсортировано {len(sorted_stickers)} стикеров")
        print("Результат сохранен в all_stickers_with_prices_sorted.json")
        
    except Exception as e:
        print(f"Ошибка при сортировке: {str(e)}")

if __name__ == "__main__":
    sort_stickers_by_id() 