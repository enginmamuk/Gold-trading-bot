# 🏆 Professional Gold Trading Bot

Binance'den gerçek zamanlı XAUUSDT (Altın) verilerini analiz ederek, profesyonel teknik göstergeler ve ekonomik haberler kullanarak **giriş-çıkış sinyalleri** veren otomatik trading botu.

## 🚀 Özellikler

- ✅ **Binance API** - Gerçek zamanlı canlı veriler
- ✅ **Teknik Göstergeler** - RSI, MACD, Ichimoku, ATR, Bollinger Bands, Stochastic
- ✅ **Timeframe'ler** - 5 dakika, 15 dakika, 1 saat
- ✅ **Long/Short Sinyalleri** - Her iki yönde işlem
- ✅ **Ekonomik Haberler** - Altını etkileyen tüm haberler
- ✅ **Telegram Alerts** - Mobil bildirimler
- ✅ **Konsol Alerts** - Terminal uyarıları
- ✅ **Risk Management** - Position sizing ve Stop Loss

## 📊 Teknik Göstergeler

1. **RSI (Relative Strength Index)** - Momentum göstergesi
2. **MACD** - Trend ve momentum
3. **Ichimoku Cloud** - Destek/direnç ve trend
4. **ATR (Average True Range)** - Volatilite
5. **Bollinger Bands** - Fiyat dalgalanması
6. **Stochastic Oscillator** - Momentum

## 📰 İzlenen Ekonomik Haberler

- Federal Reserve Kararları (Fed Funds Rate)
- NFP (Non-Farm Payroll)
- CPI (Tüketici Fiyat Endeksi)
- Enflasyon Verileri
- İşsizlik Oranı
- Ekonomik Büyüme (GDP)
- Faiz Oranı Değişiklikleri
- Jeopolitik Riskler

## 🔧 Kurulum

```bash
git clone https://github.com/enginmamuk/gold-trading-bot.git
cd gold-trading-bot
pip install -r requirements.txt
```

## ⚙️ Yapılandırma

`.env` dosyasını oluştur:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
TELEGRAM_BOT_TOKEN=your_telegram_token
TELEGRAM_CHAT_ID=your_chat_id
```

## 🚀 Kullanım

```bash
python main.py
```

## 📈 Stratejisi

### LONG Sinyali
- RSI < 30 (Oversold)
- MACD Bullish Crossover
- Ichimoku above Cloud
- ATR confirms volatility

### SHORT Sinyali
- RSI > 70 (Overbought)
- MACD Bearish Crossover
- Ichimoku below Cloud
- ATR confirms volatility

### Risk Management
- Stop Loss: 2% risk per trade
- Take Profit: 3:1 risk/reward ratio
- Position Size: Dynamic based on volatility

## 📞 İletişim

Sorularınız için: enginmamuk@github.com

---

**⚠️ Disclaimer:** Bu bot eğitim amaçlıdır. Trading riskleridir. Her zaman stop loss kullanın.