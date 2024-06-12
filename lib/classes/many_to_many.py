class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not (5 <= len(title) <= 50):
            raise ValueError("Title length must be between 5 and 50 characters inclusive")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title attribute is immutable")

    @title.deleter
    def title(self):
        raise AttributeError("Title attribute cannot be deleted")



        
class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify the name attribute")

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))


  

class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        self._contributors = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify the name attribute")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        raise AttributeError("Cannot modify the category attribute")

    def add_article(self, article):
        self._articles.append(article)

    def articles(self):
        return self._articles

    def add_contributor(self, author):
        self._contributors.append(author)

    def contributors(self):
        return self._contributors

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return [article.author for article in self._articles]



