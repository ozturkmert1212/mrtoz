# mrtoz.ai Chat (Flask + Gemini/Grok)

Çok modellli, TR/EN dil seçenekli, koyu/açık temalı sohbet arayüzü. Sohbetler sadece tarayıcı `localStorage`’ında saklanır; sunucu log tutmaz.

## Özellikler
- Modeller: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemma-3-12b`, `grok-3`. Kullanıcı model seçerse fallback yapılmaz; seçmezse sıralama: flash → flash-lite → gemma.
- TR/EN dil toggle (UI, placeholder, hata/kota mesajları ve tarih formatı).
- Koyu/açık tema, kullanıcı balonu her zaman siyah metin.
- Görsel yanıtları otomatik gösterme (URL veya data URI img). 
- Yerel konuşma geçmişi (sidebar, multi-select silme, yeni konuşma).
- Quota/rate-limit durumları tek cümlelik uyarıyla iletilir (Gemini & Grok).
- Sidebar altı: “made by MRTOZ” ve `/information` linki (bilingüal bilgi sayfası).

## Kurulum (Python)
1) Sanal ortam + bağımlılıklar
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
2) Ortam değişkenleri (veya `.env` kullan)
```powershell
$env:GEMINI_API_KEY="your_key"
$env:GROK_API_KEY="your_grok_key"   # isteğe bağlı
```
3) Çalıştır
```powershell
python app.py
```
4) Aç: http://127.0.0.1:5000

Waitress (Windows servis benzeri)
```powershell
python run_waitress.py
```

## Docker Compose
Kök dizinde `.env` oluştur (gitignore’da kalır):
```
GEMINI_API_KEY=your_key
GROK_API_KEY=your_grok_key
```
Sonra:
```powershell
docker compose up --build
```

## API ve modeller
- Endpoint: `/api/chat`
- İstek gövdesi:
```json
{
  "prompt": "Hello",
  "model": "gemini-2.5-flash"
}
```
- Desteklenen modeller: `gemini-2.5-flash`, `gemini-2.5-flash-lite`, `gemma-3-12b`, `grok-3`.
- Model belirtmezsen: flash → flash-lite → gemma sırayla denenir; Grok seçiliyse Grok’a gider.
- Grok için `GROK_API_KEY` gerekir, endpoint: `https://api.x.ai/v1/chat/completions`.

## Tailwind derleme (opsiyonel)
```bash
npm install
npm run build:css   # src/input.css -> static/css/tailwind.css
```

## Notlar
- Log tutulmaz, sohbetler sadece tarayıcı `localStorage`’ında.
- `.env` dosyasını repoya ekleme; anahtarlarını gizli tut.
- Quota/rate-limit (402/403/429 veya body’de “quota/rate limit”) durumunda frontend tek satır uyarı gösterir.
