import requests
import random
import json
from exceptions import *

class Quran(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def r_chapter(self):
        try:
        	return self.chapter
        except AttributeError:
            v = [i for i in range(1, 115)]
            self.chapter = random.choice(v)
            return self.chapter

    @property
    def get_all_chapters(self):
        return [i for i in range(1, 115)]

    def chapter_info(self, _id):
        r = requests.get(f'http://staging.quran.com:3000/api/v3/chapters/{_id}')
        return r.json()

    def verses_in_chapter(self, chapter_id):
        r = requests.get(f'http://staging.quran.com:3000/api/v3/chapters/{chapter_id}')
        return r.json()['chapter']['verses_count']

    @property
    def get_random_verse(self):
        chapters = self.get_all_chapters
        ar_verses = []
        en_verses = []
        del chapters[0]
        chapter = random.choice(chapters)
        search = True
        r = requests.get(f'http://staging.quran.com:3000/api/v3/chapters/{chapter}/verses', params = {'language' : 'en'})
        pages = [i for i in range(1, int(r.json()['meta']['total_pages']) + 1)]
        for page in pages:
            req = requests.get(f'http://staging.quran.com:3000/api/v3/chapters/{chapter}/verses', params = {'translations' : 21, 'language' : 'en', 'page' : page, 'text_type' : 'words'})
            for verse in req.json()['verses']:
                ar_verses.append({'text' : verse['text_indopak'], 'number' : verse['verse_number']})
                en_verses.append({'text' : verse['translations'][0]['text'], 'number' : verse['verse_number']})
        del ar_verses[0:1]
        del en_verses[0:1]
        ar_verse = random.choice(ar_verses)
        ar_index = ar_verses.index(ar_verse)
        en_verse = en_verses[ar_index]
        _verses['ar'] = ar_verse
        _verses['en'] = en_verse
        _verses['chapter'] = chapter
        return _verses
    @property   
    def Verse(self):
    	_chapter = getattr(self, "chapter", None)
    	_verse = getattr(self, "verse", None)
    	if _chapter:
    		"""Will Check Chapter and return the error that explains the mistake uses made"""
    		if not isinstance(self.chapter, int):
    			raise TypeError("Chapter has to be an integer")
    		if self.chapter > 114:
    			
    			raise ChapterNotValidError(f"Chapter is too big, it has to be 1 or 114 or in between")
    		
    		elif self.chapter == 0:
    			
    			raise ChapterNotValidError("Chapter can't be zero, it has to be 1 or 114 or in between")
    		
    		elif self.chapter < 0:
    			
    			raise ChapterNotValidError("Chapter can't be negative, it has to be 1 or 114 or in between")
    		
    	else:
    		raise ChapterNotValidError("A chapter must be provided") from None
    	
    	
    	#----Finished checking chapter-----
    	#----Checking Verses----
    	verses = [i for i in range(1, int(self.verses_in_chapter(self.chapter)) + 1)]
    	if _verse:
    		if not isinstance(self.verse, int):
    			raise TypeError("Verse has to be an integer")
    		if self.verse not in verses:
    			raise VerseError(f"Invalid verse, this chapter has {verses[-1]} verses starting from 1")
    	else:
    		raise VerseError("A verse must be provided") from None
    	#----Finished Checking Verses----
    	"""With Having chapter and verse validated, lets get the verse"""
    	req = requests.get(f"http://staging.quran.com:3000/api/v3/chapters/{self.chapter}/verses?recitation=1&translations=21&language=en&text_type=words")
    	total_pages = [i for i in range(1, int(req.json()['meta']['total_pages']) + 1)]
    	for page in total_pages:
    		r = requests.get(f"http://staging.quran.com:3000/api/v3/chapters/{self.chapter}/verses", params = {'language' : "en", 'translations' : 21, 'text_type' : "words", 'page' : page})
    		for verse in r.json()['verses']:
    			if self.verse == verse['verse_number']:
    				verse = {'ar' : verse['text_indopak'], 'en' : verse['translations'][0]['text'], 'verse_number' : verse['verse_number'], 'chapter_id' : verse['chapter_id']}
    				return verse
