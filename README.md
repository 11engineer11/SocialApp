# SocialApp
Arkadaşlar resimler karışık gelmiş. Aslında hepsine yorum yazmıştım ama buradan da yazayım. 
o Homepost "model" "friends" kısımları "model" ler dir yani bunları sadece class olarak oluşturuyoruz. ardından resimde bulunan cmd ekranı 
olarak gözüken "...manage.py migrate" komutuyla bunlar veritabanı halini alıyor diğer resimlerde bulunan 
fields=[
.
...
...] kısımlı alanlar bunların (fotolarda Friends ve Homepost için ayrı ayrı var) veritabanı halini almış durumudur. gördüğünüz gibi sadece 
migrate komutu ile "NULL" olup olmama durumunu "Foreign Key"leri "Default" değerlerin herbirini kendisi otomatik olarak ayarlamış durumda
ayrıca bunlar bizden bağımsız ayarlanmayıp "Class" larda tanımladığımız şeylere göre "otomatik" oluşuyor. 


diğer resimlerde manzara fotoları vs görüyorsunuz bunlar atılan postlar (oluşturduğum çeşitli userlar tarafından) altta arkadaş ekleme ve en
altta "Post Oluştur" kısmı bulunuyor tıklandığında örneğin "128....../post/create" adres alanına yönlendiriyor bu adres alanların göre nerede 
ne iş yapıldığını anlayabilirsiniz. Arayüz tasarımı bunlara göre yapılabilir. Ayrıca Katıl butonu ve katılımcıların gösterilmesini sağlayacak
eleman veri tabanına eklenecektir.
