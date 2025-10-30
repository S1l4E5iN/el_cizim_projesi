# El Çizim Projesi (Hand Drawing with MediaPipe & OpenCV)

Bu proje, **MediaPipe** ve **OpenCV** kütüphaneleri kullanılarak geliştirilmiş bir **el hareketiyle çizim uygulamasıdır**.  
Kullanıcının el hareketlerini kamera aracılığıyla algılar ve parmak pozisyonlarına göre dijital tuval üzerinde gerçek zamanlı çizim yapılmasını sağlar.

---

## Proje Amacı
Bilgisayarla görme (Computer Vision) alanında **el takibi (hand tracking)** ve **jest tanıma (gesture recognition)** tekniklerini uygulayarak,  
kamera üzerinden doğal kullanıcı etkileşimini (**Natural User Interaction**) simüle etmektir.  
Bu proje, temel **MediaPipe Hands API** ve **OpenCV çizim fonksiyonlarının** entegrasyonuna örnektir.

---

## Özellikler
- **Gerçek zamanlı el tespiti** (MediaPipe Hands)
- **İşaret parmağıyla çizim yapma**
- **Başparmak ve işaret parmağı yakınken çizimi durdurma (silgi modu)**
- **C tuşu ile ekranı temizleme**
- **ESC tuşu ile uygulamadan çıkış**
- **Renk ve kalınlık değiştirilebilir (isteğe göre genişletilebilir)**

---

## Kullanılan Teknolojiler
  **Python 3.10**
  **OpenCV** 
  **MediaPipe** 
  **NumPy**

---

## 🖥️ Kurulum ve Çalıştırma
```bash
# Gerekli kütüphaneleri yükle
pip install mediapipe opencv-python numpy

# Projeyi başlat
python cizim.py

