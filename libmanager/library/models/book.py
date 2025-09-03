
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Book:
    """책 정보를 표현하는 데이터 클래스"""
    book_count = 0

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        Book.book_count += 1

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.year})"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Book":
        return cls(data["title"], data["author"], data["year"])
