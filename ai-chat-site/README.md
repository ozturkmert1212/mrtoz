# Cline AI Chat (Flask + Gemini)

Basit bir AI sohbet uygulaması. Konfigürasyon ve çalıştırma:

1. Sanal ortam oluşturun ve bağımlılıkları yükleyin:

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

2. `GEMINI_API_KEY` ortam değişkenini ayarlayın (veya `.env` kullanın):

```bash
set GEMINI_API_KEY=your_key_here  # Windows cmd
$env:GEMINI_API_KEY="your_key_here"  # PowerShell
```

3. Uygulamayı çalıştırın:

```bash
python app.py
```

4. Tarayıcıda `http://127.0.0.1:5000` adresini açın.

Notlar:
- Bu örnek konuşma geçmişini veya log tutmaz (kullanıcının isteği üzerine).
- Gemini API çağrıları için Google tarafında doğru izinlerin ve anahtarın yapılandırıldığından emin olun.
- Tailwind CDN kaldırıldı; statik stil dosyası `static/css/tailwind.css` olarak projeye eklendi. Görsel uyumsuzluk yaşarsanız bu dosyayı yeniden derleyin.

Alternatif: WSGI ile (Waitress) üretim/servis benzeri çalıştırma (Windows için önerilir):

1. Kurulum:

```powershell
pip install -r ai-chat-site\requirements.txt
```

2. Çalıştırma:

```powershell
python ai-chat-site\run_waitress.py
```

Sunucu `0.0.0.0:5000` üzerinde çalışacaktır; tarayıcıdan `http://127.0.0.1:5000` adresini açın.

Not: Üretimde ek güvenlik, ters proxy (nginx/Cloud Load Balancer), TLS ve süreç yönetimi (örn. Windows servis veya systemd/PM2/tini) yapılandırın.

Gemini uç noktası (güncel)

- Kullanılan modeller (varsayılan sıra): `gemini-2.5-flash` (primary), `gemini-2.5-pro` (fallback). İsteğe bağlı ek: `grok-3` (xAI) seçilebilir.

İstemci tarafında model seçimi

- `/api/chat` isteğine `model` alanı ekleyebilirsiniz. Örnek JSON:

```json
{
	"prompt": "Hello, how are you?",
	"model": "gemini-2.5-pro"
}
```

- Desteklenen modeller: `gemini-2.5-flash`, `gemini-2.5-pro`, `grok-3`.
- Eğer `model` göndermezseniz, yukarıdaki varsayılan sırayla denenir.
- Endpoint örneği: `https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key=YOUR_KEY`
- Örnek curl (Windows PowerShell `curl.exe` ile):

```powershell
curl.exe -X POST -H "Content-Type: application/json" ^
	-d "{\"contents\":[{\"parts\":[{\"text\":\"Hello, how are you?\"}]}],\"generationConfig\":{\"temperature\":0.2,\"maxOutputTokens\":256}}" ^
	"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key=YOUR_KEY"
```

Grok (xAI) kullanımı

- Ortam değişkeni: `GROK_API_KEY`
- Endpoint: `https://api.x.ai/v1/chat/completions`
- Model: `grok-3`
- Örnek curl (PowerShell `curl.exe`):

```powershell
curl.exe -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_GROK_KEY" ^
  -d "{\"model\":\"grok-3\",\"messages\":[{\"role\":\"user\",\"content\":\"Hello\"}],\"temperature\":0.2}" ^
  "https://api.x.ai/v1/chat/completions"
```

Tailwind yeniden derleme (opsiyonel, Node gerekir)

1) Node yüklü ise (şu anda ortamda `npm` bulunmuyor):

```bash
cd ai-chat-site
npm install -D tailwindcss postcss autoprefixer
```

2) Giriş dosyası: `src/input.css` already has `@tailwind base; @tailwind components; @tailwind utilities;`

3) Derleme:

```bash
npx tailwindcss -i ./src/input.css -o ./static/css/tailwind.css --minify
```

Not: `tailwind.config.js` `./templates/**/*.html` yollarını tarar. Üretim dağıtımlarında bu adımı CI/CD’ye ekleyin.
