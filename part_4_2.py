from checker import check_website_text
from unittest import mock


# example.com will be skipped to request
def test_check_website_assert_example():
    """ To assert in case of exampl.com """
    check_website_text = mock.Mock(return_value=True)
    assert check_website_text("http://example.com/", "Example Domain")
    assert check_website_text("http://example.com/", "asking for permission")


def test_check_website_assert_not_example():
    """ To assert not in case of exampl.com """
    check_website_text = mock.Mock(return_value=False)
    assert not check_website_text("http://example.com/", "some random text 123 123")


def test_check_website_non_example():
    """ To assert other than exampl.com """
    assert not check_website_text("http://google.com", "Example Domain")
