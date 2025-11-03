# Axon Bodycam Overlay

Bu proje, OBS üzerinde kullanılabilen basit bir Axon Bodycam arayüzüdür. 
Gerçek bir bodycam görüntüsüne benzer şekilde tarih, saat ve model bilgilerini ekranda gösterir. 
Ayrıca küçük bir panel üzerinden tarih, model ve isim gibi bilgileri ayarlayabilirsiniz.

---

## Özellikler
- Gerçekçi Axon Bodycam görünümü  
- Model seçimi (Axon Body 2, 3, 4)  
- Tarih ve saat ayarlama  
- Kolay arayüz  
- OBS ile uyumlu HTML/CSS/JS altyapısı  

---

## Kurulum
1. Projeyi bilgisayarınıza indirin veya zip olarak çıkarın.  
2. Bilgisayarınızda **Python 3** kurulu olduğundan emin olun.  
3. Gerekli Python kütüphanelerini yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
4. **main.py** dosyasını çalıştırın:
   ```bash
   python main.py
   ```
5. Açılan pencereden tarih, model ve diğer bilgileri ayarlayın.  
6. OBS'e girin ve bir **Tarayıcı Kaynağı (Browser Source VEYA Browser)** ekleyin.  
   Ardından **index.html** dosyasını kaynak olarak seçin.  

---

## Dosya Yapısı
```
axon-bodycam/
│
├── index.html          # OBS'e eklenecek HTML arayüzü
├── style.css           # Arayüz tasarımı
├── config.js           # Ayar dosyası (Python script tarafından güncellenir)
├── axon_logo.png       # Axon logosu
├── main.py             # Python kontrol paneli (ayar yönetimi)
├── requirements.txt    # Gerekli Python kütüphaneleri
└── README.md           # Proje açıklaması
```

---

## Notlar
- HTML/CSS dosyaları **OBS Tarayıcı Kaynağı** olarak eklenmelidir.  
- **Python kodu yalnızca tarih ve model bilgilerini düzenlemek içindir.**  
- Fontlar ve efektler **otomatik olarak yüklenir**.  
- Gerçekçi efektler ve Axon logosu, OBS üzerinde tam uyum sağlar.  

---

Yapımcı : hàk

