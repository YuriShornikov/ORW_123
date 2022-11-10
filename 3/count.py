
class Open_file:
    def __init__(self, top, count_full):
        self.top = top
        self.count_full = count_full


lst = ['1.txt', '2.txt', '3.txt']
for doc in lst:
    def open_file(doc):
        with open(doc, 'rt', encoding='utf-8') as file:
            counts = {}
            doc_list = {}
            r = file.read()
            doc_list.update({doc: r})
            count = r.count('\n') + 1
            counts.update({count: doc_list})
            # print(counts)
            sorted_counts = sorted(counts.items())
            print(sorted_counts)
            # counts = [doc]
            # r = file.read()
            # count = r.count('\n') + 1
            # counts.append(count)
            # counts.append(r)
            # print(counts)

            # print(count)
            # print(r)


    open_file(doc)
# with open('1.txt', 'rt', encoding='utf-8') as file:
#
#     r = file.read()
#
#     count = r.count('\n')
#
#
#     print(count)
#     print(r)
