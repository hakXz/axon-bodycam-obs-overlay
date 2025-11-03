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
   bash
   pip install -r requirements.txt
main.py dosyasını çalıştırın:

bash
Copy code
python main.py
Açılan pencereden tarih, model ve diğer ayarları yapın.

OBS’e tarayıcı kaynağı (Browser Source) olarak index.html dosyasını ekleyin.

Dosya Yapısı
arduino
Copy code
axon-bodycam/
│
├── index.html
├── style.css
├── config.js
├── axon_logo.png
├── main.py
├── requirements.txt
└── README.md
Notlar
HTML/CSS dosyaları OBS tarayıcı kaynağına eklenmelidir.

Python kodu sadece tarih ve model bilgilerini düzenlemek için kullanılır.

Fontlar otomatik olarak yüklenecek şekilde ayarlanmıştır.

Yapımcı: haktamar
Amaç: OBS sahnelerinde gerçekçi Axon Bodycam efekti oluşturmak
