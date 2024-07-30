def all_variants(text):
    n = 0
    n1 = 1

    for i in text:
        n += 1
        n1 += 1

        if n == 1:
            for i in text:
                yield i
        if n == 2:
            for i in text:
                if  n1 < 5:
                    yield i + text[n-1]
                    n = 3
                    n1 += 1
                else: pass

            yield text

x = 0
a = all_variants("abc")
for i in a:
    x += 1
    print(i)