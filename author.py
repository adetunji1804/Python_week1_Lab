class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def published(self, title):
        self.books.append(title)

    def __str__(self):
        titles =','.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'

def main():
    author_one = Author("J. T Lewis")
    author_one.published("Lewis & Sons")
    author_one.published("The Creative Writers")
    print(author_one)

main()