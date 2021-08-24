from sanic import Sanic, Request
from sanic import response
from sanic.exceptions import SanicException

from WordsCountPersistent import persist_counts, get_word_statistics
from WordsCounter import count_words_in_text, count_words_in_file, count_words_in_url

app = Sanic("words count api")


@app.route("/word_counter", methods=['GET', 'POST'])
def word_counter(request: Request):
    if request.method == 'GET':
        txt = request.args.get('txt', None)
        file = request.args.get('file', None)
        url = request.args.get('url', None)
    else:
        txt = request.body.decode()
    if txt:
        count = count_words_in_text(txt)
    elif file:
        count = count_words_in_file(file)
    elif url:
        count = count_words_in_url(url)
    else:
        raise SanicException("Missing parameter txt or file or url", status_code=501)
    persist_counts(count)
    return response.empty(200)


@app.route("/word_statistics", methods=['GET'])
def word_statistics(request: Request):
    word = request.args.get('word', None)
    if not word:
        raise SanicException("Missing word", status_code=501)
    count = get_word_statistics(word)
    return response.text(str(count))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
