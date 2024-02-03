from abstract_factory02 import LinkItem, ListItem, PageItem, Factory


class HtmlPageItem(PageItem):
    def __init__(self, title, author):
        super().__init__(title, author)
        
    def make_html(self):
        output = f'<html>\n<head>\n<title>{self.title}</title>\n</head>\n'
        output += f'<body>\n'
        output += f'<h1>{self.title}</h1>\n'
        output += f'<ul>\n'
        for list_item in self.content:
            output += list_item.make_html()
        output += f'</ul>\n'
        output += f'<hr>\n<address>{self.author}</address>'
        output += f'</body>\n</html>\n'
        return output

class HtmlLinkItem(LinkItem):
    
    def __init__(self, caption, url):
        super().__init__(caption, url)
        
    def make_html(self):
        return f'<li><a href="{self.url}">{self.caption}</a></li>'
    
class HtmlListItem(ListItem):
    def __init__(self, caption):
        super().__init__(caption)
    
    def make_html(self):
        output = '<li>\n'
        output += self.caption + '\n'
        output += '<ul>\n'
        for link_item in self.items:
            output += link_item.make_html()
        output += '</ul>\n'
        output += '</li>\n'
        return output

class HtmlFactory(Factory):
    def create_page_item(self, title, author):
        return HtmlPageItem(title, author)

    def create_link_item(self, caption, url):
        return HtmlLinkItem(caption, url)

    def create_list_item(self, caption):
        return HtmlListItem(caption)
    
    
html_factory = HtmlFactory()
google = html_factory.create_link_item('Google', 'https://google.com')
yahoo = html_factory.create_link_item('Yahoo!', 'https://www.yahoo.co.jp/')
amazon = html_factory.create_link_item('Amazon', 'https://www.amazon.co.jp/')
netflix = html_factory.create_link_item('Amazon', 'https://www.netflix.com/')
wikipedia = html_factory.create_link_item('Wikipedia', 'https://ja.wikipedia.org/')

news_pages = html_factory.create_list_item('検索')
news_pages.add(google)
news_pages.add(yahoo)

other_pages = html_factory.create_list_item('その他のページ')
other_pages.add(amazon)
other_pages.add(netflix)
other_pages.add(wikipedia)

all_page = html_factory.create_page_item('My Page', 'Taro')
all_page.add(news_pages)
all_page.add(other_pages)

all_page.write_html('tmp.html')