# Plüton PDRM – Instagram otomatik yayın

- Claude her sabah `posts/<tarih>/` klasörüne görselleri (JPEG) ve `manifest.json` dosyasını yükler.
- GitHub Actions ("Instagram yayın") her 10 dakikada bir saati gelen postları Instagram'a gönderir.
- "Bağlantı kontrolü" iş akışı elle çalıştırılır; anahtarı ve Instagram hesap ID'sini doğrular.

## Bir postu iptal etmek
GitHub'da (mobil uygulama da olur) `posts/<tarih>/manifest.json` dosyasını açın, ilgili postun
`"status": "pending"` değerini `"status": "cancelled"` yapıp kaydedin. Ya da o günün klasörünü silin.

## Gerekli ayarlar (Settings → Secrets and variables → Actions → Secrets)
- `IG_TOKEN`  – Meta sistem kullanıcısı anahtarı (süresiz)
- `IG_USER_ID` – Instagram işletme hesabı ID'si ("Bağlantı kontrolü" çıktısında görünür)
