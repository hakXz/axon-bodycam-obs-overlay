# Axon Bodycam Overlay

Bu proje, OBS üzerinde kullanılabilen basit bir Axon Bodycam arayüzüdür. Gerçek bir bodycam görüntüsüne benzer şekilde tarih, saat ve model bilgilerini ekranda gösterir. Ayrıca küçük bir panel üzerinden tarih, model ve isim gibi bilgileri ayarlayabilirsiniz.

## Özellikler
- Gerçekçi Axon Bodycam görünümü  
- Model seçimi (Axon Body 2, 3, 4)  
- Tarih ve saat ayarlama  
- Kolay arayüz  
- OBS ile uyumlu HTML/CSS/JS altyapısı  

## Kurulum
1. Depoyu bilgisayarınıza indirin veya zip olarak çıkarın.  
2. Python 3 yüklü olduğundan emin olun.  
3. Gerekli kütüphaneleri yükleyin:

   pip install -r requirements.txt
   
   main.py dosyasını çalıştırın:

- python main.py
4. Açılan pencereden tarih, model ve diğer ayarları yapın.

OBS’e tarayıcı kaynağı (Browser Source VEYA Browser) olarak index.html dosyasını ekleyin.

## Notlar
HTML/CSS dosyaları OBS tarayıcı kaynağına eklenmelidir.

Python kodu sadece tarih ve model bilgilerini düzenlemek için kullanılır.

Fontlar otomatik olarak yüklenecek şekilde ayarlanmıştır.

