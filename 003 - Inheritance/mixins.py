'''
Mixins are capable of adding features to classes

#1. Shouldn't be extended
#2. Shouldn't be instanciated
'''

# Contain only attributes
class Book():
    def __init__(self, name, content):
        self.name, self.content = name, content

# Contain only methods, but not the needed attributes
class HTMLMixin():
    def render(self):
        return ('<html><title>%s</title><body>%s</body></html>') % (self.name, self.content)

# This is multiple inheritance
class HtmlBook(Book, HTMLMixin):
    pass

html_book = HtmlBook('Alice in wonderland', 'Once upon a time...')
print(html_book.render())