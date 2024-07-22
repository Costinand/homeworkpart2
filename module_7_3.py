all_words = {}
find = {}
count = {}

class WordsFinder():

    def __init__(self, *file_names):
        self.file_names = file_names


    def get_all_words(self):

        for i in self.file_names:
            print('')
            text = []
            text_split = []
            all_words.clear()


            with open(i , 'r+', encoding='utf-8') as file:

                for line in file:

                    line_test = line.strip().lower()

                    e = ",", ".", "?", "!", "=", ";", ":", " - "
                    for i in range(len(e)):
                        line_test = line_test.replace(e[i], "")
                    text.append(line_test.split())

                for part in text:
                    for world in part:
                        text_split.append(world)

                    all_words[self.file_names] = text_split

                return all_words

    def find(self, word):

        z = 0
        for w in all_words.values():

            for e in w:
                z += 1
                if word.lower() == e:
                    find[self.file_names] = z
                    return find

    def count(self, word):

        x = 0
        for w in all_words.values():
            for e in w:
                if word.lower() == e:
                    x += 1

            count[self.file_names] = x
            return count

#
finder = WordsFinder('test_file.txt')
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
finder2 = WordsFinder('Rudyard Kipling - If.txt')
finder3 = WordsFinder('Mother Goose - Monday’s Child.txt')
wf = WordsFinder(finder, finder1, finder2, finder3)

print(finder.get_all_words()) # Все слова
print(finder.find('TEXT')) # 3 слово по счёту
print(finder.count('teXT')) # 4 слова teXT в тексте всего

print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

print(finder2.get_all_words())
print(finder2.find('if'))
print(finder2.count('if'))

print(finder3.get_all_words())
print(finder3.find('Child'))
print(finder3.count('Child'))


