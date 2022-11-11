lst = ['1.txt', '2.txt', '3.txt']
counts = {}
dict_lst = {}
for doc in lst:
    def open_file(doc):
        with open(doc, 'rt', encoding='utf-8') as file:
            r = file.read()
            count = r.count('\n') + 1
            counts.update({doc: count})
            dict_lst.update({doc: r})
    open_file(doc)

x = dict(sorted(counts.items(), key=lambda item: item[1]))

for key, value in x.items():
    for keys, values in dict_lst.items():
        if keys == key:
            print(keys)
            print(counts.setdefault(keys))
            print(values)


