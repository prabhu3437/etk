# from __future__ import unicode_literals
# import unittest
# import sys
# sys.path.append('../../')
# from etk.core import Core
# import json
# import codecs
# import time
#
# class TestExtractionsUsingRegex(unittest.TestCase):
#
#     # def setUp(self):
#     #     self.doc = json.load(codecs.open('ground_truth/1_content_extracted.jl'))
#
#     def test_extractor(self):
#         c = Core()
#
#         start_time = time.time()
#         # Load all the dictionaries here
#         print '...loading spaCy'
#         c.load_matchers()
#         end_time = time.time()
#
#         print "Time taken to load all the matchers: {0}".format(end_time - start_time)
#
#         print "\nDate Extractor"
#         date_docs = [
#                     '23/05/2016',
#                     '05/23/2016',
#                     '23-05-2016',
#                     '05-23-2016',
#                     '23 May 2016',
#                     '23rd May 2016',
#                     '23rd May, 2016',
#                     '23rd-05-2016',
#                     'March 25, 2017',
#                     'March 25th, 2017',
#                     'March 25th 2017',
#                     'March 25 2017',
#                     'The meeting is on 23/05/2016',
#                     'Can 05/23/2016 be the date of the meeting?',
#                     'Lyonne was born on 23-05-2016 at 5 in the morning',
#                     'Kramer is here on 05-23-2016',
#                     'Google Inc is planning to make the acquisition on 23 May 2016',
#                     'Romans and others will play this 23rd May 2016',
#                     'Can 23rd May, 2016 be the day the Romans win?',
#                 ]
#
#         for date_doc in date_docs:
#             print date_doc
#             print c.extract_date_spacy(date_doc)
#
#         print "\nDate Extractor"
#         age_docs = [
#                 'start Age : 22 years end',
#                 'start age : 22 yrs end',
#                 'start Age 22-40 end',
#                 'start 22 yrs end',
#                 'start 23yrs end',
#                 'start 22-40 years end',
#                 'start About me 22 end'
#         ]
#
#         for doc in age_docs:
#             print doc
#             print c.extract_age_spacy(doc)
#
# if __name__ == '__main__':
#     unittest.main()
