# CS2 Sticker Price Parser

Программа для получения актуальных цен стикеров из CS2 через Steam API.

Для получения итогового файла с отсортированными стикерами и их ценами обращаться в Телеграм (указан в профиле).

## Описание

Этот проект содержит набор скриптов для:
1. Парсинга цен стикеров из Steam Market
2. Объединения результатов парсинга
3. Сортировки стикеров по ID
4. Поиска цен по ID стикера

## Файлы проекта

- `stickers.json` - исходный файл со списком стикеров
- `all_stickers_with_prices_sorted.json` - итоговый файл с отсортированными стикерами и их ценами
- `sticker_price_parser.py` - основной скрипт для получения цен стикеров
- `merge_sticker_files.py` - скрипт для объединения файлов с ценами
- `sort_stickers.py` - скрипт для сортировки стикеров по ID
- `find_price_by_id.py` - скрипт для поиска цены стикера по ID

## Требования

- Python 3.x
- Библиотека requests

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/cs2-sticker-parser.git
cd cs2-sticker-parser
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Использование

1. Получение цен стикеров:
```bash
python sticker_price_parser.py
```

2. Объединение файлов с ценами:
```bash
python merge_sticker_files.py
```

3. Сортировка стикеров по ID:
```bash
python sort_stickers.py
```

4. Поиск цены по ID стикера:
```bash
python find_price_by_id.py
```

## Примечания

- Программа использует Steam API, поэтому могут быть ограничения на количество запросов
  (с нынешней скоростью IP-адресс банился каждые 30 минут, однако достаточно сделать бэкап файла stickers_with_prices.json, сменить IP и дальше в путь!)
- При превышении лимита запросов программа автоматически сохраняет прогресс и может быть запущена снова
- Все цены сохраняются в USD 
