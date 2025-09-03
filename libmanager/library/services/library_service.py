
from __future__ import annotations
from typing import Iterable, List
from library.models.book import Book
from library.services.base_service import BaseService


class LibraryService(BaseService):
    """도서 목록을 메모리에서 관리하는 서비스.
      - 내부 상태를 캡슐화하기 위해 _books(list[Book])를 사용
    """

    def __init__(self) -> None:
        # 내부 리스트 초기화
        self._books = []

    def add_book(self, book: Book) -> None:
        # 책 추가
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        # 제목으로 책 삭제 (없으면 ValueError)
        for i, book in enumerate(self._books):
            if book.title == title:
                del self._books[i]
                return
        raise ValueError()

    def list_books(self) -> Iterable[Book]:
        # 책 목록 반환 (복사본 반환 권장)
        return list(map(lambda book: book, self._books.copy()))

    def find_book(self, title: str) -> Book:
        # 제목으로 책 찾기 (없으면 ValueError)
        for book in self._books:
            if book.title == title:
                return book
        raise ValueError()
