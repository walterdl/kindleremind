
def get_header(text):
    author_start = text.rindex('(')
    author_end = text.rindex(')')

    return {
        'title': text[:author_start].strip(),
        'author': text[author_start + 1:author_end].strip()
    }
