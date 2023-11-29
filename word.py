class Word:
    def __init__(self, id: int, hungarian: str, english: str, danish: str, category: str) -> None:
        self.id = id
        self.hungarian = hungarian
        self.english = english
        self.danish = danish
        self.category = category

    def __repr__(self) -> str:
        return f"Word({self.english} in category {self.category})"

