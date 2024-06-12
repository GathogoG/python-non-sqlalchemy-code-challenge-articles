import pytest
from classes.many_to_many import Magazine

class TestMagazine:
    """Magazine in many_to_many.py"""

    def test_has_name(self):
        """Magazine is initialized with a name"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")

        assert magazine_1.name == "Vogue"
        assert magazine_2.name == "AD"

    def test_name_is_immutable_string(self):
        """magazine name is of type str and cannot change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")

        with pytest.raises(AttributeError):
            magazine_1.name = "Vogue Italia"

        with pytest.raises(AttributeError):
            magazine_2.name = 2

    def test_has_category(self):
        """Magazine is initialized with a category"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")

        assert magazine_1.category == "Fashion"
        assert magazine_2.category == "Architecture & Design"

    def test_category_is_immutable_string(self):
        """magazine category is of type str and cannot change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")

        with pytest.raises(AttributeError):
            magazine_1.category = "Lifestyle"

        with pytest.raises(AttributeError):
            magazine_2.category = 2

    def test_get_all_magazines(self):
        """Magazine class has all attribute"""
        Magazine.all = []
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture & Design")

        assert len(Magazine.all) == 2
        assert magazine_1 in Magazine.all
        assert magazine_2 in Magazine.all

if __name__ == "__main__":
    pytest.main([__file__])

