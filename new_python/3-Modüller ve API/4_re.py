# regular expression, string içinde arama, eşleşme, değiştirme gibi işlemleri kolaylaştırır
# kaçış karakterleri ayrı regular expression ayrıdır \n yeni - \b. Regex ararken r kullanmak kaçış karakteri oluşmasını engeller.
import re

print(dir(re))
print("\n" + 20 * '-')

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"
result = re.findall("Python", str)
print(result)
print(len(result))
print("\n" + 20 * '-')

print(re.split(" ", str, 3))
print(re.split("R", str))
print("\n" + 20 * '-')

print(re.sub(" ","-",str))
print(re.sub(r"\s","-",str))
print("\n" + 20 * '-')

# Kelimenin stringde ilk bulunan kısmının verilerini gösterir
result = re.search("Python", str)
print("result tipi: ", type(result))
print("result nesnesi: ", result)
print("Eşleşmenin span'ı: ", result.span())
print("Eşleşmenin başlangıç index'i: ", result.start())
print("Eşleşmenin bitiş index'i: ", result.end())
print("Eşleşen metin: ", result.group())
print("Aranan string: ", result.string)

for match in re.finditer(r'Python', str, re.IGNORECASE):
    print(match.span(), match.group())
print("\n" + 20 * '-')

# [] - Köşeli parantezler arasına yazılan bütün karakterler aranır.

print("[a48c] harflerinden biri: ", re.findall("[a48c]",str))
print("[a-e] aralığındaki karakterler: ", re.findall("[a-e]", str))
print("[0-5] aralığındaki rakamlar: ", re.findall("[0-5]", str))
print("Rakam harici karakterler: ", re.findall("[^0-9]", str))
print("Harf hariç karakterler: ", re.findall("[^a-zA-Z]", str))
print("\n" + 20 * '-')

# . = Her hangi bir tek karakteri belirtir.
print("ortada h.", re.findall(".h.", str))
print("s ile başlar t ile biter.", re.findall("s..t", str))
print("3 karakterli.", re.findall("...", str))
print("P ile başlar n ile biter.", re.findall("P..h.n", str))
print("\n" + 20 * '-')

# ^ ve $ = string belirtilen karakterle başlayıp bitiyor mu?
print("P ile başlıyor: ", re.findall("^P",str))
print("a ile başlıyor: ", re.findall("^a",str))
print("t ile bitiyor: ", re.findall("t$",str))
print("s ile başlayıp t ile biten 4 karakterli: ", re.findall("s..t$",str))
print("saatt ile bitiyor mu: ", re.findall("saatt$",str))
print("\n" + 20 * '-')

# * = Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.
print("a sıfır veya fazla.", re.findall("sa*t",str))
print("a sıfır veya fazla.", re.findall("saa*t",str))
print("a sıfır veya fazla.", re.findall("saaa*t",str))
print("a ve i sıfır veya fazla.", re.findall("saaa*i*t",str))
print("\n" + 20 * '-')

# + = Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.
print("a bir veya fazla.", re.findall("sa+t",str))
print("a bir veya fazla.", re.findall("saa+t",str))
print("a bir veya fazla.", re.findall("saaa+t",str))
print("\n" + 20 * '-')

# ? = Bir karakterin sıfır ya da bir kez olmasını kontrol eder.
print("a sıfır veya bir.", re.findall("sa?t",str))
print("a sıfır veya bir.", re.findall("saa?t",str))
print("a sıfır veya bir.", re.findall("saaa?t",str))
print("a ve y sıfır veya bir.", re.findall("saaa?y?t",str))
print("\n" + 20 * '-')

# {} = Karakter sayısını kontrol eder.
print("a iki kez.", re.findall("a{2}", str))
print("a iki kez.", re.findall("sa{2}", str))
print("a iki veya üç kez.", re.findall("sa{2,3}", str))
print("a iki kez, t ile biter.", re.findall("sa{2}t", str))
print("iki rakam.", re.findall("[0-9]{2}", str))
print("iki-dört rakam.", re.findall("[0-9]{2,4}", str))
print("\n" + 20 * '-')

# | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
print(re.findall("a|b", str))
print("\n" + 20 * '-')

# () - gruplamak için kullanılır.
print(re.findall(r"(P|K)ython", str))
print(re.findall(r"(P|K)ython\sKursu", str))
print(re.findall(r"(Python|Programlama)\s", str))
print(re.findall(r"(Python\sK|Kursu)", str))
# burda Python K daki kullanılır ve diğerinde kullanılmaz!
print("\n" + 20 * '-')

# \ karakteri, özel karakterleri (örneğin $) normal karakter gibi aramamızı sağlar. Yani $ işaretini aramak için \$ kullanılır.
print(re.findall("\$a", "$abc a$ab"))
print("\n" + 20 * '-')

# \A ve \Z= Belirtilen karakter string in başında veya sonunda mı
print(re.findall(r"\APython", "Python Kursu"))
print(re.findall(r"saat\Z", str))
print("\n" + 20 * '-')

# \b: Belirtilen karakter kelimenin başında veya sonunda mı?
print(re.findall(r"\bKursu", "Python Kursu"))
print(re.findall(r"Kursu\b", "Python Kursu"))
# \B: Belirtilen karakter kelimenin başında veya sonunda değil mi?
print(re.findall(r"\Btho", "Python abdon"))
print("\n" + 20 * '-')

# \d = [0-9] ve \D = [^0-9] ile aynı anlama gelir
print(re.findall(r"\d", "abc123de3f"))
print(re.findall(r"\D", "1ab44_50"))
print("\n" + 20 * '-')

# \s = boşluk karakterini ve \S = boşluk karakteri harici
print(re.findall(r"\s", "Python Kursu"))
print(re.findall(r"\S", "Python Kursu"))
print("\n" + 20 * '-')

# \w = Alfabetik karakterler, rakamlar ve alt çizgi karakteri ve \W = bunların tam tersi
print(re.findall(r"\w", "Python_123!"))
print(re.findall(r"\W", "Python_123!"))
print("\n" + 20 * '-')

def check_password(psw):
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmalıdır.")
    elif not re.search("[a-z]", psw):
        raise Exception("parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("parola büyük harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("parola rakam içermelidir.")
    elif not re.search("[_@$]", psw):
        raise Exception("parola alpha numeric karakter içermelidir.")
    elif re.search(r"\s",psw):
        raise Exception("parola boşluk içermemelidir.")
    else:
        print("geçerli parola: {}".format(psw))
password = "1234567aA_"
try:
    check_password(password)
except Exception as ex:
    print(ex)
finally:
    print("validation tamamlandı.")
