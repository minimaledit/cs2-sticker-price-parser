import json
import requests
import time
import urllib.parse

def get_sticker_price(sticker_name):
    # Формируем правильный формат имени стикера для запроса
    market_hash_name = f"Sticker | {sticker_name}"
    encoded_name = urllib.parse.quote(market_hash_name)
    
    # API endpoint для получения цен стикеров
    url = f"https://steamcommunity.com/market/priceoverview/?currency=USD&appid=730&market_hash_name={encoded_name}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success'):
                return {
                    'lowest_price': data.get('lowest_price', 'N/A'),
                    'median_price': data.get('median_price', 'N/A'),
                    'volume': data.get('volume', 'N/A')
                }
        elif response.status_code == 429:
            print("Превышен лимит запросов. Ожидание 33 секунд...")
            time.sleep(33)
            return '429'  # Возвращаем специальный код ошибки
        else:
            print(f"Ошибка HTTP: {response.status_code}")
            return {'lowest_price': 'N/A', 'median_price': 'N/A', 'volume': 'N/A'}
    except Exception as e:
        print(f"Ошибка при получении цены для {sticker_name}: {str(e)}")
        return {'lowest_price': 'N/A', 'median_price': 'N/A', 'volume': 'N/A'}

def save_progress(stickers_data, processed_stickers):
    # Сохранение результата в файл
    with open('stickers_with_prices.json', 'w', encoding='utf-8') as f:
        json.dump({'data': processed_stickers}, f, ensure_ascii=False, indent=4)
    print("\nПрогресс сохранен в stickers_with_prices.json")

def main():
    # Чтение исходного файла
    with open('stickers.json', 'r', encoding='utf-8') as f:
        stickers_data = json.load(f)
    
    error_count = 0  # Счетчик ошибок 429
    processed_stickers = []  # Список обработанных стикеров
    
    # Добавление цен к каждому стикеру
    for sticker in stickers_data['data'][:]:  # Используем копию списка для итерации
        sticker_name = sticker['name']
        result = get_sticker_price(sticker_name)
        
        # Проверяем, является ли результат ошибкой 429
        if result == '429':
            error_count += 1
            if error_count >= 3:
                print("\nПолучено 3 ошибки 429 подряд. Сохранение прогресса...")
                save_progress(stickers_data, processed_stickers)
                return
            continue  # Пропускаем текущий стикер и пробуем следующий
        
        # Если это не ошибка 429, обновляем данные стикера
        sticker.update(result)
        processed_stickers.append(sticker)  # Добавляем в список обработанных
        
        # Вывод информации о стикере в консоль
        print(f"\nСтикер: {sticker_name}")
        print(f"ID: {sticker['id']}")
        print(f"Минимальная цена: {result['lowest_price']}")
        print(f"Медианная цена: {result['median_price']}")
        print(f"Объем продаж: {result['volume']}")
        
        # Удаляем обработанный стикер из исходного файла
        stickers_data['data'].remove(sticker)
        with open('stickers.json', 'w', encoding='utf-8') as f:
            json.dump(stickers_data, f, ensure_ascii=False, indent=4)
        
        # Сбрасываем счетчик ошибок при успешном запросе
        error_count = 0
        
        # Задержка между запросами
        time.sleep(2.5)
    
    # Финальное сохранение
    save_progress(stickers_data, processed_stickers)
    print("\nГотово! Все стикеры обработаны.")

if __name__ == "__main__":
    main() 