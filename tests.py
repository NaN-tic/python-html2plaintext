#This file is part of html2plaintext. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
'''
Unit test for html2plaintext
'''

import unittest
from html2plaintext import html2plaintext

BODY = (
    ('<h1>Hello World</h1>', True),
)


class Html2PlaintextTest(unittest.TestCase):
    '''
    Test Case for html2plaintext
    '''

    def test_html(self):
        '''
        Test HTML
        '''
        for html, result in BODY:
            if result:
                test = self.assert_
            else:
                test = self.assertFalse
            test(html2plaintext(html))

if __name__ == '__main__':
    unittest.main()
