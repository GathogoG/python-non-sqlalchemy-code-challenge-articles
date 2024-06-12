import pytest
from classes.many_to_many import Article, Magazine, Author

class TestAuthor:
    """Author in many_to_many.py"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")

        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_is_immutable_string(self):
        """author name is of type str and cannot change"""
        author = Author("Carry Bradshaw")

        with pytest.raises(AttributeError, match="Cannot modify the name attribute"):
            author.name = "ActuallyTopher"

    def test_name_len(self):
        """author name is longer than 0 characters"""
        author = Author("Carry Bradshaw")

        assert len(author.name) > 0

    def test_has_many_articles(self):
        """author has many articles"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = author.add_article(magazine, "How to wear a tutu with style")
        article_2 = author.add_article(magazine, "Dating life in NYC")

        assert len(author.articles()) == 2
        assert article_1 in author.articles()
        assert article_2 in author.articles()

    def test_articles_of_type_articles(self):
        """author articles are of type Article"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = author.add_article(magazine, "How to wear a tutu with style")

        assert isinstance(author.articles()[0], Article)

    def test_has_many_magazines(self):
        """author has many magazines"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_2, "2023 Eccentric Design Trends")

        assert magazine_1 in author.magazines()
        assert magazine_2 in author.magazines()

    def test_magazines_of_type_magazine(self):
        """author magazines are of type Magazine"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        author.add_article(magazine_1, "How to wear a tutu with style")

        assert isinstance(author.magazines()[0], Magazine)

    def test_magazines_are_unique(self):
        """author magazines are unique"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_2, "2023 Eccentric Design Trends")
        author.add_article(magazine_2, "Carrara Marble is so 2020")

        assert len(set(author.magazines())) == len(author.magazines())

    def test_topic_areas(self):
        """returns a list of topic areas for all articles by author"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_2, "Carrara Marble is so 2020")

        actual_topic_areas = author.topic_areas()
        expected_topic_areas = ["Fashion", "Architecture"]
        assert sorted(actual_topic_areas) == sorted(expected_topic_areas)

    def test_topic_areas_are_unique(self):
        """topic areas are unique"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_1, "Dating life in NYC")
        author.add_article(magazine_2, "2023 Eccentric Design Trends")

        assert len(set(author.topic_areas())) == len(author.topic_areas())

if __name__ == "__main__":
    pytest.main([__file__])

