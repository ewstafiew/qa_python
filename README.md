# BooksCollector — юнит-тесты

Проект содержит класс `BooksCollector` (файл `main.py`), который позволяет
добавлять книги, задавать им жанры и работать со списком избранного.
Для класса написан набор юнит-тестов на `pytest` (файл `tests.py`).

## Что покрыто тестами

Все методы класса `BooksCollector` покрыты тестами.
В файле `tests.py` **15 функций-тестов**, из которых 2 параметризованных.
С учётом параметризации pytest выполняет **18 тестовых прогонов** —
все проходят успешно.

Каждый тест создаёт собственный экземпляр `BooksCollector()`,
поэтому тесты независимы друг от друга.

### `add_new_book`
- `test_add_new_book_add_two_books` — добавление двух книг: словарь
  `books_genre` содержит ровно 2 записи.
- `test_add_new_book_genre_is_empty` — у только что добавленной книги
  жанр пустой (`''`).
- `test_add_new_book_invalid_name_not_added` — параметризованный тест
  (2 набора данных): книга не добавляется, если её название длиннее
  40 символов или является пустой строкой.
- `test_add_new_book_duplicate_not_added` — повторное добавление той же
  книги не перезаписывает её (ранее установленный жанр сохраняется).

### `set_book_genre` / `get_book_genre`
- `test_set_and_get_book_genre` — параметризованный тест (3 набора данных):
  для книг жанров «Ужасы», «Фантастика», «Мультфильмы» установленный жанр
  корректно возвращается методом `get_book_genre`.
- `test_set_book_genre_invalid_genre_keeps_empty` — жанр, которого нет в
  списке доступных (`genre`), не устанавливается — значение остаётся пустым.

### `get_books_with_specific_genre`
- `test_get_books_with_specific_genre_returns_only_matching` — метод
  возвращает только книги нужного жанра; для жанра, которого нет среди
  книг, возвращается пустой список.

### `get_books_genre`
- `test_get_books_genre_returns_full_dict` — метод возвращает полный
  словарь `books_genre` со всеми книгами и их жанрами.

### `get_books_for_children`
- `test_books_with_age_rating_not_for_children` — книги с возрастным
  рейтингом («Ужасы», «Детективы») не попадают в список детских книг.
- `test_book_without_genre_not_for_children` — книга без жанра в список
  детских книг не попадает.

### `add_book_in_favorites`
- `test_add_book_in_favorites_no_duplicates` — книгу можно добавить в
  избранное; повторное добавление не создаёт дубликат.
- `test_add_unknown_book_in_favorites_does_nothing` — книга, которой нет
  в `books_genre`, в избранное не добавляется.

### `delete_book_from_favorites`
- `test_delete_book_from_favorites` — удаление книги из избранного:
  остальные книги в списке сохраняются.
- `test_delete_missing_book_from_favorites_does_not_raise` — удаление
  книги, которой нет в избранном, не вызывает ошибку.

### `get_list_of_favorites_books`
- `test_get_list_of_favorites_books_returns_all` — метод возвращает
  список всех избранных книг в порядке добавления.

## Использованные приёмы pytest

- **Параметризация** (`@pytest.mark.parametrize`) — применена в тестах
  `test_add_new_book_invalid_name_not_added` и `test_set_and_get_book_genre`,
  чтобы избежать дублирования кода при проверке разных наборов данных.
- **Изоляция тестов** — каждый тест создаёт собственный экземпляр
  `BooksCollector()`, что исключает влияние тестов друг на друга.

## Запуск тестов

    pytest -v tests.py

## Результат

    ============================= 18 passed in 0.01s ==============================