# PyIslam

PyIslam is a python library that provide easier way to get verses and soon hadith.

This Package uses https://Quran.com api to retrieve verses and some info

# Examples

## Quran

* Get a random verse from quran

```python
from PyIslam import Quran

Q = Quran()
print(Q.get_random_verse)
```
* Get a specific verse
```python
from PyIslam import Quran

Q = Quran(chapter = 5, verse = 10)
print(Q.Verse) # Case Sensitive
```

`Q.Verse` will return a dict in this structure : `{'ar' : '<Arabic Verse>', 'en' : '<English Translation>', 'verse_number' : <Verse Number>, 'chapter_id' : <Chapter ID>`

### Tafsir
Coming soon

## Hadith
Coming Soon

# Installing
  `pip install pyislam`

