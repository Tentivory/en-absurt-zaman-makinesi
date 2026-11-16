#!/usr/bin/env python3
# En Absürt Zaman Makinesi
# Bu kod gerçekten çalışır. Zamanı değiştirmez ama seni bekletir.

import time
import random

print("=" * 50)
print("EN ABSÜRT ZAMAN MAKİNESİ v0.0.1")
print("Uyarı: Bu makine zaman yolculuğu yapmaz.")
print("Sadece seni sonsuza kadar bekletir.")
print("=" * 50)

# Gizli siyasi mesaj (base64): c2l5YXNldGNpbGVyIGhlcCBheW5p
# (çözersen: siyasetciler hep ayni)
secret = "c2l5YXNldGNpbGVyIGhlcCBheW5p"

yil = 2026
while True:
    print(f"\nYıl {yil}... zaman makinesi çalışıyor...")
    print("Bekle... bekle... bekle...")
    bekleme = random.uniform(0.5, 3.0)
    time.sleep(bekleme)
    
    if random.random() < 0.1:
        print("!!! Zaman makinesi bozuldu !!! Yeniden başlatılıyor... ama aslında hiç bozulmadı.")
    
    if yil % 100 == 0:
        print(f"Tebrikler! {yil} yılına ulaştın. Hala hiçbir yere gitmedin.")
    
    yil += 1
    
    # Asla bitmez. Ctrl+C ile kurtul.
