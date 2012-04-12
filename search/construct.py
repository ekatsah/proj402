from re import sub
from django.db import connection

def parse_words(doc, content):

    # split and keep the words
    words = [x.lower() for x in sub(r'\W', ' ', content).split() if len(x) > 2]

    terms_count = dict()
    for word in words:
        terms_count[word] = terms_count.get(word, 0) + 1

    cursor = connection.cursor()
    cursor.execute('select max(id) from search_wordentry;')
    id = cursor.fetchone()[0];
    for word, count in terms_count.iteritems():
        # to slow : 
        # WordEntry.objects.create(word=word, document=doc, count=count)
        id += 1
        cursor.execute('insert into search_wordentry values(%d, "%s", %d, %d);' %
                       (id, word, doc.id, count))
    connection.commit_unless_managed()
    cursor.close()

    return len(words)
