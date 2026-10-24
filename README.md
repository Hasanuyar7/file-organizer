# 📁 Dosya Düzenleyici

Belirtilen bir klasördeki dosyaları uzantılarına göre otomatik olarak alt klasörlere taşıyan basit bir Python betiği.

## ✨ Özellikler

- 🗂️ Dosyaları uzantılarına göre kategorize eder
- 📂 Şu an desteklenen kategoriler:
  - **HTML** → `.html`, `.htm`
  - **Python** → `.py`
  - **C++** → `.cpp`, `.cc`, `.cxx`, `.c++`, `.hpp`, `.hxx`, `.hh`
- 🔒 Diğer uzantılar olduğu gibi bırakılır (atlanır)
- 📝 Her taşıma işlemi konsola yazdırılır

## 🚀 Kullanım

1. `düzenleyici.py` dosyasını indirin
2. İçindeki `ana_klasor` değişkenini kendi klasör yolunuza göre düzenleyin:

```python
ana_klasor = r"C:\Users\hasan\Desktop\kod"
