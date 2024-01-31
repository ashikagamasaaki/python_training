from abc import ABC, abstractmethod

class Document:
    def __init__(self, content: str):
        self.content = content

class IPrinter(ABC):
    @abstractmethod
    def print_document(self, document: Document) -> None:
        pass

class ICopy(ABC):
    @abstractmethod
    def copy_document(self, document: Document) -> None:
        pass

class MultifuncPrinter(IPrinter, ICopy):
    def print_document(self, document: Document) -> None:
        print(f'プリントを開始します。')
    
    def copy_document(self, document: Document) -> None:
        print(f'コピーを開始します。')


class PrintClient:
    def __init__(self, printer: IPrinter):
        self.printer = printer
    
    def execute(self, document: Document):
        self.printer.print_document(document)


class CopyClient:
    def __init__(self, copier: ICopy):
        self.copier = copier
    
    def execute(self, document: Document):
        self.copier.copy_document(document)
        

doc = Document('テストプリント、コピー')


multi_printer = MultifuncPrinter()
printer_client = PrintClient(multi_printer)
printer_client.execute(doc)