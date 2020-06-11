import unittest

from mimetype_description import get_mime_type_description, UnsupportedMimeType, UnsupportedLanguage


class MimeTypeDescriptionCase(unittest.TestCase):

    def test_invalid_mime_type(self):
        self.assertRaises(UnsupportedMimeType, get_mime_type_description, 'application/x-chess')

    def test_invalid_language(self):
        self.assertRaises(UnsupportedLanguage, get_mime_type_description, 'text/x-python', 'es-CO')

    def test_default_language(self):
        self.assertEqual(get_mime_type_description('text/plain'), 'plain text document')

    def test_other_language(self):
        self.assertEqual(get_mime_type_description('text/plain', 'es'), 'documento de texto sencillo')


if __name__ == '__main__':
    unittest.main()
