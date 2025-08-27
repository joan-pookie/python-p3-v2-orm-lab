import pytest
from lib.review import Review

def test_review_content():
    rev = Review(1, "Excellent")
    assert rev.content == "Excellent"
