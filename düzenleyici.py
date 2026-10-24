import os
import shutil

ana_klasor = r"C:\Users\hasan\Desktop\kod"  # Sabit yol

if not os.path.isdir(ana_klasor):
    print(f"Hata: {ana_klasor} bulunamadı.")
    exit()

html_klasor = os.path.join(ana_klasor, "HTML")
python_klasor = os.path.join(ana_klasor, "Python")
cpp_klasor = os.path.join(ana_klasor, "C++")

os.makedirs(html_klasor, exist_ok=True)
os.makedirs(python_klasor, exist_ok=True)
os.makedirs(cpp_klasor, exist_ok=True)

# .cpp dışında C++ ile ilişkili diğer uzantılar (isteğe göre genişletilebilir)
cpp_uzantilari = (".cpp", ".cc", ".cxx", ".c++", ".hpp", ".hxx", ".hh")

for dosya_adi in os.listdir(ana_klasor):
    dosya_yolu = os.path.join(ana_klasor, dosya_adi)
    if os.path.isfile(dosya_yolu):
        _, uzanti = os.path.splitext(dosya_adi)
        uzanti = uzanti.lower()
        if uzanti in (".html", ".htm"):
            shutil.move(dosya_yolu, os.path.join(html_klasor, dosya_adi))
            print(f"Taşındı: {dosya_adi} -> HTML/")
        elif uzanti == ".py":
            shutil.move(dosya_yolu, os.path.join(python_klasor, dosya_adi))
            print(f"Taşındı: {dosya_adi} -> Python/")
        elif uzanti in cpp_uzantilari:
            shutil.move(dosya_yolu, os.path.join(cpp_klasor, dosya_adi))
            print(f"Taşındı: {dosya_adi} -> C++/")
        else:
            print(f"Atlandı: {dosya_adi}")

print("İşlem tamamlandı.")