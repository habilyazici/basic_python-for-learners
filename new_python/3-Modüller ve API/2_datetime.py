print("\n" + 20 * '-' + "\n")
# datetime: Tarih ve saat bilgisini verir (Yıl, ay, gün, saat, dakika, saniye, mikrosaniye)
# timedelta: İki tarih/saat arasında işlem yapmaya yarar.
# timezone: Bir zaman dilimini belirtmek için kullanılır. (örn: UTC, UTC+3)
# import datetime
from datetime import datetime, time, timedelta, timezone
import pytz

simdi = datetime.now()
simdi2 = datetime.today()
# now() ile zaman dilimi değiştirilebilir today() ile değiştirilemez.
print("Şu anki tarih ve saat:", simdi) 
print("Bugünün tarihi ve saati:", simdi2)
print("UTC zamanı:", datetime.now(timezone.utc))
print("Amerika (UTC-3) zamanı:", datetime.now(timezone(timedelta(hours=-3))))
print("Almanya saati:", datetime.now(pytz.timezone("Europe/Berlin")))
print("\n" + 20 * '-' + "\n")

print("Yıl(int):", datetime.now().year)
print("Ay(int):", simdi.month)
print("Gün(int):", simdi.day)
print("Saat(int):", simdi.hour)
print("Dakika(int):", simdi.minute)
print("Saniye(int):", simdi.second)
print("\n" + 20 * '-' + "\n")

print("Ctime ile okunabilir format:", datetime.ctime(simdi))
print("Yıl (string):", datetime.strftime(simdi,'%Y')) # string for time
print("Saat (string):", datetime.strftime(simdi,'%X'))
print("Gün (string):", datetime.strftime(simdi,'%d'))
print("Haftanın günü:", datetime.strftime(simdi,'%A'))
print("Ay ismi:", datetime.strftime(simdi,'%B'))
print("Yıl, ay ve gün ismi:", datetime.strftime(simdi,'%Y %B %A %d'))
print("\n" + 20 * '-' + "\n")

birthday = datetime(1983, 5, 9, 12, 30, 10, 132354)
print("Doğum günü tarihi:", birthday)
print("\n" + 20 * '-' + "\n")

time2 = 'tarih: 15 April 2019 hour 10:12:30 saniye 234234      '
result14 = datetime.strptime(time2, 'tarih: %d %B %Y hour %H:%M:%S saniye %f      ') 
# string parse time, metini datetime nesnesine çevir datetime.now() şeklinde bir nesne
print("Oluşan dt nesnesi: ", result14)
result15 = result14.year
print("Oluşan tarihin yılı:", result15)
print("\n" + 20 * '-' + "\n")

result16 = datetime.timestamp(birthday)
print("1970 den sonra geçen total saniye:", result16)
datetime.fromtimestamp(result16) # saniye to datetime
print("Saniyeden datetime'a çevir:", result17)
result18 = datetime.fromtimestamp(0) 
print("Unix epoch (0) tarihi:", result18)
print("\n" + 20 * '-' + "\n")

result19 = simdi - birthday
print(type(result19))
print("Doğum gününden bugüne geçen süre (timedelta):", result19)
print("Total days:", result19.days)
print("Total hours:", result19.total_seconds() // 3600)
print("Kalan saat:", result19.seconds // 3600)
print("years:", result19.days // 365)
print("months:", (result19.days % 365) // 30)
print("days:", (result19.days % 365) % 30)
print("\n" + 20 * '-' + "\n")

result20 = simdi - timedelta(days = 10)
print("result20 (simdi - timedelta 10 gün):", result20)
print("\n" + 20 * '-' + "\n")

print(simdi - timedelta(days=5, hours=3, minutes=2, seconds=10))
print(simdi + timedelta(days=2*365 + 30 + 10))
print(simdi + timedelta(weeks=1, hours=12, seconds=30))
print(simdi + timedelta(days=366, hours=1, minutes=1, seconds=1))
print(simdi + timedelta(days=-(2*365 + 90 + 7)))