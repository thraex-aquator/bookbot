def count_words(text):
    return len(text.split())

def count_letters(text):
    d = {}
    for w in text.lower().split():
        for c in w:
            if c.isalpha():
                if c not in d:
                    d[c] = 1
                else:
                    d[c] += 1
    return dict(sorted(d.items(), key=lambda i: -i[1]))

with open('books/frankenstein.txt') as f:
    contents = f.read()
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count_words(contents)} words found in the document')
    for key, value in count_letters(contents).items():
        print(f"The '{key}' character was found {value} times")
    print('--- End report ---')
