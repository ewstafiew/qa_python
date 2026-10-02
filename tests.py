import pytest

from main import BooksCollector

class TestBooksCollector:

    # add_new_book

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_genre_is_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Супермен')

        assert collector.get_book_genre('Супермен') == ''

    @pytest.mark.parametrize('name', ['А' * 41,'',])
    def test_add_new_book_invalid_name_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert name not in collector.get_books_genre()

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Оно')

        assert collector.get_book_genre('Оно') == 'Ужасы'

    # set_book_genre

    @pytest.mark.parametrize('name, genre', [
        ('Оно', 'Ужасы'),
        ('Дюна', 'Фантастика'),
        ('Карлсон', 'Мультфильмы'),
    ])
    def test_set_book_genre_sets_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] == genre

    def test_set_book_genre_invalid_genre_keeps_empty(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Триллер')

        assert collector.books_genre['Оно'] == ''

    # get_book_genre

    @pytest.mark.parametrize('name, genre', [
        ('Оно', 'Ужасы'),
        ('Дюна', 'Фантастика'),
        ('Карлсон', 'Мультфильмы'),
    ])
    def test_get_book_genre_returns_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_returns_empty_for_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Супермен')

        assert collector.get_book_genre('Супермен') == ''

    def test_get_book_genre_returns_none_for_unknown_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Несуществующая') is None

    # get_books_with_specific_genre

    def test_get_books_with_specific_genre_returns_only_matching(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Сияние')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert set(collector.get_books_with_specific_genre('Ужасы')) == {'Оно', 'Сияние'}
        assert collector.get_books_with_specific_genre('Комедии') == []

    # get_books_genre

    def test_get_books_genre_returns_full_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_genre() == {'Оно': 'Ужасы', 'Дюна': ''}

    # get_books_for_children

    def test_books_with_age_rating_not_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Карлсон')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Карлсон', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Карлсон']

    def test_book_without_genre_not_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')

        assert collector.get_books_for_children() == []

    # add_book_in_favorites

    def test_add_book_in_favorites_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Оно')

        assert collector.get_list_of_favorites_books() == ['Оно']

    def test_add_unknown_book_in_favorites_does_nothing(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая')

        assert collector.get_list_of_favorites_books() == []

    # delete_book_from_favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Оно')

        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_delete_missing_book_from_favorites_does_not_raise(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites('Оно')

        assert collector.get_list_of_favorites_books() == []

    # get_list_of_favorites_books

    def test_get_list_of_favorites_books_returns_all(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Оно', 'Дюна']