html_doc = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>
    <h1 id="header">
        Python Kursu
    </h1>
    <div class="grup1">
        <h2 class="title">
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="grup2">
        <h2>
            Modüller
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="grup3">
        <h2>
            Django
        </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <img src="fred.jpg" alt="">
    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link2">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link3">Elsie</a>
</body>
</html>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

# print("soup objesi:", soup)
print("soup objesi tipi:", type(soup))
result1 = soup.prettify()
# print("Tüm HTML (prettify):\n", result1)
print("Tüm HTML (prettify) tipi:", type(result1))
print("\n" + 20 * '-' + "\n")

print("Title etiketi:", soup.title)
print("Head etiketi:", soup.head)
# print("Body etiketi:", soup.body)
print("\n" + 20 * '-' + "\n")

# eğer tek etiket varsa string şeklinde döndürebiliyoruz yoksa none döndürür.
print("Title ismi:", soup.title.name)
print("Title string:", soup.title.string)
print("li etiketleri:", soup.li.string)
print("\n" + 20 * '-' + "\n")

print("h1 etiketi:", soup.h1)
print("İlk h2 etiketi:", soup.h2)
print("h2 ismi:", soup.ul.name)
print("h2 string:", soup.h2.string.strip())
print("h1 string:", soup.h1.string.strip())
print("\n" + 20 * '-' + "\n")

tum_h2 = soup.find_all('h2')
# liste şeklinde tüm h2 etiketleri döner.
print("İlk h2:", tum_h2[0])
print("İkinci h2:", tum_h2[1].string.strip())
print("\n" + 20 * '-' + "\n")

print("İlk div:", soup.div)
print("İkinci div:", soup.find_all('div')[1])
print("İkinci div içindeki tüm li'ler:", soup.find_all('div')[1].ul.find_all('li'))
print("\n" + 20 * '-' + "\n")

print("İlk div'in tüm çocukları:", soup.div.find_all(True))
print("\n" + 20 * '-' + "\n")


print("İlk div'den sonraki 2. kardeş ve bir önceki kardeş:", soup.div.find_next_sibling().find_next_sibling().find_previous_sibling())
print("\n" + 20 * '-' + "\n")

print("Tüm linkler (href):")
for link in soup.find_all('a'):
    print("Link:", link.get('href'))
    # print("Link:", link['href'])
# ikisi de string döner ama get ile aranan değer yoksa none döner!