# Axon Bodycam Overlay

Bu proje, OBS üzerinde kullanılabilen basit bir Axon Bodycam arayüzüdür. Gerçek bir bodycam görüntüsüne benzer şekilde tarih, saat ve model bilgilerini ekranda gösterir. Ayrıca küçük bir panel üzerinden tarih, model ve isim gibi bilgileri ayarlayabilirsiniz.

## Özellikler
- Gerçekçi Axon Bodycam görünümü  
- Model seçimi (Axon Body 2, 3, 4, Axon Fleet 2, 3)  
- Tarih ve saat ayarlama  
- Kolay arayüz  
- OBS ile uyumlu HTML/CSS/JS altyapısı  

# Kurulum

## Gereksinimler
- Python 3.7 veya üzeri  
- OBS Studio  
- Git  

## Kurulum Adımları

### 1. Projeyi İndirme
```bash
git clone https://github.com/hakXz/axon-bodycam-obs-overlay.git
cd axon-bodycam-obs-overlay
```

### 2. Python Bağımlılıklarını Yükleme
```bash
pip install -r requirements.txt
```

### 3. Programı Çalıştırma
```bash
python3 main.py
```

### 4. Ayarları Yapılandırma
Programı çalıştırdıktan sonra gerekli ayarları seçin.

### 5. OBS Studio Ayarları
1. OBS Studio'yu açın  
2. "Kaynaklar" panelinde **"+"** butonuna tıklayın  
3. "Tarayıcı" seçeneğini seçin  
4. Yeni kaynağa bir isim verin  
5. Açılan pencerede **"Yerel dosya"** seçeneğini işaretleyin  
6. İndirdiğiniz zip dosyası içindeki **axon_overlay.html** dosyasını seçin  
7. **"Tamam"** butonuna tıklayın  

## Notlar
- OBS Studio'nun kurulu olduğundan emin olun  
- Python 3'ün sisteminizde yüklü olduğundan emin olun  
- Gerekirse pip'i güncellemek için:
```bash
pip install --upgrade pip
```

## Ekstra Notlar
HTML/CSS dosyaları OBS tarayıcı kaynağına eklenmelidir.

Python kodu model bilgilerini düzenlemek için kullanılır.

Fontlar otomatik olarak yüklenecek şekilde ayarlanmıştır.

## Örnek Görsel

<p align="center">
  <img src="https://raw.githubusercontent.com/hakXz/axon-bodycam-obs-overlay/main/Screenshot.png" 
       alt="Axon Bodycam Overlay Preview" width="600"><br>
  <em>OBS üzerinde çalışan Axon Bodycam arayüzü</em>
</p>
