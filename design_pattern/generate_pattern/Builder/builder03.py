"""
ある文書を表すクラス Document があります。
この文書は、タイトル、本文、およびフッターを持ちます。
しかし、この文書の作成は複雑で、様々な要素を考慮しながら行われます。
DocumentBuilder インターフェースとその具象クラスを使用して、文書の作成を簡素化する DocumentDirector クラスを実装してください。
"""
from abc import ABC, abstractmethod

# Product
class Document:
    def __init__(self):
        self.__title = None
        self.__body = None
        self.__footer = None
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title
    
    @property
    def body(self):
        return self.__body
    
    @body.setter
    def body(self, body):
        self.__body = body
    
    @property
    def footer(self):
        return self.__footer
    
    @footer.setter
    def footer(self, footer):
        self.__footer = footer
    

    def __str__(self):
        return f'Title: {self.__title}\nBody: {self.__body}\nFooter: {self.__footer}'

# Builder(IF)
class IDocumentBuilder(ABC):
    def __init__(self):
        self.document = Document()
    
    @abstractmethod
    def build_title(self, title):
        pass
    
    @abstractmethod
    def build_body(self, body):
        pass
    
    @abstractmethod
    def build_footer(self, footer):
        pass
    
    @abstractmethod
    def get_result(self):
        pass
    

# ConcreteBuilder(実装)
class DocumentBuilder(IDocumentBuilder):
    def __init__(self):
        super().__init__()
    
    def build_title(self, title):
        self.document.title = title
    
    def build_body(self, body):
        self.document.body = body    
    
    def build_footer(self, footer):
        self.document.footer = footer

    def get_result(self):
        return self.document

# Director
class DocumentDirector:
    def __init__(self, builder: IDocumentBuilder):
        self.__builder = builder
        
    def construct_document(self, title, body, footer):
        self.__builder.build_title(title)
        self.__builder.build_body(body)
        self.__builder.build_footer(footer)
        return self.__builder.get_result()
    

builder = DocumentBuilder()
directore = DocumentDirector(builder)
print(directore.construct_document("Builder Pattern", "This is the body of the document.", "© 2022"))
