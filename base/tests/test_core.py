import unittest
import pathlib
from tempfile import TemporaryDirectory
from unittest.mock import patch

THUMBNAIL_URL = (
    'http://books.google.com/books/content'
    '?id=0gtBw760Y5EC&printsec=frontcover'
    '&img=1&zoom=1&edge=curl&source=gbs_api'
)

class SaveThumbnailsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory()
        
    def tearDown(self):
        self.tmp.cleanup()
        
    # def test_save_thumbnails(self):
    #     from booksearch.core import Book
    #     book = Book({'id': '', 'volumeInfo': {
    #         'imageLinks': {
    #             'thumbnail': THUMBNAIL_URL
    #         }
    #     }})
        
    #     filename = book.save_thumbnails(self.tmp.name)[0]
    #     self.assertTrue(pathlib.Path(filename).exists())
    
    @patch('booksearch.core.get_data')
    def test_save_thumbnails(self, mock_get_data):
        from booksearch.core import Book
        
        data_path = pathlib.Path('__file__').with_name('data')
        
        print('★★★★★★★★★★★★★★★★★', data_path)
        
        mock_get_data.return_value = (
            'tests/data/uWhmDwAAQBAJ_smallThumbnail.jpeg'
        ).read_bytes()
        
        book = Book({'id': '', 'volumeInfo': {
            'imageLinks': {
                'thumbnail': THUMBNAIL_URL
            }
        }})
        
        filename = book.save_thumbnails(self.tmp.name)[0]
        mock_get_data.assert_called_with(THUMBNAIL_URL)
        
        self.assertEqual(data, filename, read_bytes())