import json

def find_price_by_id(sticker_id):
    try:
        # Чтение файла с ценами
        with open('all_stickers_with_prices_sorted.json', 'r', encoding='utf-8') as f:
            stickers_data = json.load(f)
        
        # Поиск стикера по ID
        for sticker in stickers_data['data']:
            if sticker['id'] == sticker_id:
                return {
                    'name': sticker['name'],
                    'lowest_price': sticker['lowest_price'],
                    'median_price': sticker['median_price'],
                    'volume': sticker['volume']
                }
        
        return None  # Если стикер не найден
    
    except Exception as e:
        print(f"Ошибка при поиске цены: {str(e)}")
        return None

# Пример использования
if __name__ == "__main__":
    sticker_id = input("Введите ID стикера: ")
    result = find_price_by_id(sticker_id)
    
    if result:
        print(f"\nИнформация о стикере:")
        print(f"Название: {result['name']}")
        print(f"Минимальная цена: {result['lowest_price']}")
        print(f"Медианная цена: {result['median_price']}")
        print(f"Объем продаж: {result['volume']}")
    else:
        print("Стикер с таким ID не найден") 