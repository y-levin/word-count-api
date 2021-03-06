# word-count-api
Usage:
- run pip install -r requirements.txt
- run WordsCountAPI.py (Min. Python 3.7)

1 - get words count from text:
- Using get request - add to the url argument txt= <the_text>
```
http://127.0.0.1:8000/word_counter?txt=hi
```
- Using post request - add to the body the text (raw text)
```
curl -X POST \
  'http://127.0.0.1:8000/word_counter' \
  -H 'cache-control: no-cache' \
  -d hello this is my text
```
2 - get words count from file:
- Using get request - add to the url argument file= <the_file path in the server>
- current project has the file alice29.txt
```
http://127.0.0.1:8000/word_counter?file=alice29.txt
```
3 - get words count from url:
- Using get request - add to the url argument url= <the_url to read>
```
http://127.0.0.1:8000/word_counter?url=https://raw.githubusercontent.com/y-levin/word-count-api/main/alice29.txt
```

3 - get words statistics:
- Using get request - add to the url argument word= <the_word to get statistics>
```
http://127.0.0.1:8000/word_statistics?word=alice
```
