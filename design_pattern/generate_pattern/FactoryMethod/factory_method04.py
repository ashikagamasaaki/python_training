from abc import ABC, abstractmethod

# Product
class Document(ABC):
    def __init__(self):
        self.__file_name = None
        
    @property
    def fileName(self):
        return self.__file_name
    
    @fileName.setter
    def fileName(self, file_name):
        self.__file_name = file_name
    
    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def load(self):
        pass
    
# ConcretProduct
class TextDocument(Document):
    def save(self):
        print(f'Textを保存 ファイル名：{self.fileName}')
        
    def load(self):
        print(f'Textをロード ファイル名：{self.fileName}')
    
    
class PDFDocument(Document):
    def save(self):
        print(f'PDFを保存 ファイル名：{self.fileName}')
        
    def load(self):
        print(f'PDFをロード ファイル名：{self.fileName}')
    
    
class ExcelDocument(Document):
    def save(self):
        print(f'Excelを保存 ファイル名：{self.fileName}')
        
    def load(self):
        print(f'Excelをロード ファイル名：{self.fileName}')
        

# Factory
class DocumentFactory(ABC):
    def __init__(self):
        self._documents:list[Document] = []
    
    def create(self, file_name: str):
        product = self.create_factory(file_name)
        self.register_factory(product)
        return product
        
    @abstractmethod
    def create_factory(self, file_name: str):
        pass
        
    @abstractmethod
    def register_factory(self, product: Document):
        pass
    
# ConcreteFactory
class TextDocumentFactory(DocumentFactory):
    def create_factory(self, file_name: str):
        text_document = TextDocument()
        text_document.fileName = file_name
        return text_document
    
    def register_factory(self, product: Document):
        self._documents.append(product)
        
class PDFDocumentFactory(DocumentFactory):
    def create_factory(self, file_name: str):
        pdf_document = PDFDocument()
        pdf_document.fileName = file_name
        return pdf_document
    
    def register_factory(self, product: Document):
        self._documents.append(product)
        
class ExcelDocumentFactory(DocumentFactory):
    def create_factory(self, file_name: str):
        excel_document = ExcelDocument()
        excel_document.fileName = file_name
        return excel_document
    
    def register_factory(self, product: Document):
        self._documents.append(product)
        

text_factory = TextDocumentFactory()
sample_document = text_factory.create('sample.txt')
develop_document = text_factory.create('develop.txt')

sample_document.save()
develop_document.load()

for document in text_factory._documents:
    print(document.fileName)