# Scrapy-паук для парсинга данных с tmsearch.uspto.gov

Этот проект представляет собой Scrapy-паук для парсинга данных с сайта `tmsearch.uspto.gov`, который используется для поиска торговых марок в США.

## Установка

1. Убедитесь, что у вас установлен Scrapy. Если нет, установите его:

   ```bash
   pip install scrapy
   ```

2. Установите Selenium для работы с браузером (если требуется):

   ```bash
   pip install selenium
   ```

3. Убедитесь, что у вас установлен веб-драйвер для Selenium (например, ChromeDriver для Google Chrome).

## Запуск

1. Перейдите в директорию проекта:

   ```bash
   cd scripts/Domain
   ```

2. Запустите паука:
   ```bash
   scrapy crawl a
   ```

## Описание проекта

Паук `QuotesSpider` (названный "a") отправляет запрос на указанный URL и сохраняет HTML-страницу в файл. В проекте также закомментирован пример использования Selenium для автоматизации браузера.

## Настройки

Настройки проекта находятся в файле `whois/settings.py`. Вы можете изменить параметры, такие как задержки между запросами, количество одновременных запросов и т.д.
