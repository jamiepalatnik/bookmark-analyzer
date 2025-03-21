import project


def test_convert_html():
    htmlfile = "test-files/bookmarks_test.html"
    newtxtfile = "test-files/analyzed_bookmarks_test.txt"
    assert (
        project.convert_html(htmlfile, newtxtfile)
        == "test-files/analyzed_bookmarks_test.txt"
    )


def test_abc_sort():
    txtfile = "test-files/bookmarks_test.txt"
    assert project.abc_sort(txtfile) == [
        "https://cs50.harvard.edu/python/2022/",
        "https://cs50.harvard.edu/python/2022/",
        "https://docs.pytest.org/en/stable/",
        "https://docs.python.org/3/",
        "https://www.google.com/",
    ]


def test_write_to_new_file():
    txtfile = "test-files/bookmarks_test.txt"
    newtxtfile = "test-files/analyzed_bookmarks_test.txt"
    assert (
        project.convert_html(txtfile, newtxtfile)
        == "test-files/analyzed_bookmarks_test.txt"
    )
