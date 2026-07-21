import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator, StochasticOscillator, MACD
from ta.volatility import BollingerBands, AverageTrueRange
from ta.trend import IchimokuIndicator
import config

class TechnicalIndicators:
    """Professional Technical Indicators for Gold Trading"""
    
    def __init__(self, df: pd.DataFrame):
        """
        Initialize with OHLCV data
        df must contain: open, high, low, close, volume
        """
        self.df = df.copy()
        self.signals = {}
        
    def calculate_all(self):
        """Calculate all technical indicators"""
        self._calculate_rsi()
        self._calculate_macd()
        self._calculate_ichimoku()
        self._calculate_atr()
        self._calculate_bollinger_bands()
        self._calculate_stochastic()
        
        return self.signals
    
    def _calculate_rsi(self):
        """RSI - Relative Strength Index"""
        rsi = RSIIndicator(close=self.df['close'], window=config.RSI_PERIOD)
        self.df['rsi'] = rsi.rsi()
        
        self.signals['rsi'] = {
            'value': self.df['rsi'].iloc[-1],
            'oversold': self.df['rsi'].iloc[-1] < config.RSI_OVERSOLD,
            'overbought': self.df['rsi'].iloc[-1] > config.RSI_OVERBOUGHT,
        }
    
    def _calculate_macd(self):
        """MACD - Moving Average Convergence Divergence"""
        macd = MACD(
            close=self.df['close'],
            window_fast=config.MACD_FAST,
            window_slow=config.MACD_SLOW,
            window_sign=config.MACD_SIGNAL
        )
        
        self.df['macd'] = macd.macd()
        self.df['macd_signal'] = macd.macd_signal()
        self.df['macd_diff'] = macd.macd_diff()
        
        # Bullish crossover
        bullish = (self.df['macd'].iloc[-2] < self.df['macd_signal'].iloc[-2] and
                   self.df['macd'].iloc[-1] > self.df['macd_signal'].iloc[-1])
        
        # Bearish crossover
        bearish = (self.df['macd'].iloc[-2] > self.df['macd_signal'].iloc[-2] and
                   self.df['macd'].iloc[-1] < self.df['macd_signal'].iloc[-1])
        
        self.signals['macd'] = {
            'macd': self.df['macd'].iloc[-1],
            'signal': self.df['macd_signal'].iloc[-1],
            'histogram': self.df['macd_diff'].iloc[-1],
            'bullish_crossover': bullish,
            'bearish_crossover': bearish,
        }
    
    def _calculate_ichimoku(self):
        """Ichimoku Cloud - Support/Resistance and Trend"""
        ichimoku = IchimokuIndicator(
            high=self.df['high'],
            low=self.df['low'],
            window1=9,
            window2=26,
            window3=52
        )
        
        self.df['ichimoku_a'] = ichimoku.ichimoku_a()
        self.df['ichimoku_b'] = ichimoku.ichimoku_b()
        self.df['ichimoku_base'] = ichimoku.ichimoku_base_line()
        self.df['ichimoku_conversion'] = ichimoku.ichimoku_conversion_line()
        
        current_price = self.df['close'].iloc[-1]
        cloud_top = max(self.df['ichimoku_a'].iloc[-1], self.df['ichimoku_b'].iloc[-1])
        cloud_bottom = min(self.df['ichimoku_a'].iloc[-1], self.df['ichimoku_b'].iloc[-1])
        
        self.signals['ichimoku'] = {
            'conversion': self.df['ichimoku_conversion'].iloc[-1],
            'base': self.df['ichimoku_base'].iloc[-1],
            'cloud_top': cloud_top,
            'cloud_bottom': cloud_bottom,
            'above_cloud': current_price > cloud_top,
            'below_cloud': current_price < cloud_bottom,
            'bullish': self.df['ichimoku_conversion'].iloc[-1] > self.df['ichimoku_base'].iloc[-1],
        }
    
    def _calculate_atr(self):
        """ATR - Average True Range (Volatility)"""
        atr = AverageTrueRange(
            high=self.df['high'],
            low=self.df['low'],
            close=self.df['close'],
            window=config.ATR_PERIOD
        )
        
        self.df['atr'] = atr.average_true_range()
        
        self.signals['atr'] = {
            'value': self.df['atr'].iloc[-1],
            'atr_percent': (self.df['atr'].iloc[-1] / self.df['close'].iloc[-1]) * 100,
        }
    
    def _calculate_bollinger_bands(self):
        """Bollinger Bands - Price Volatility"""
        bb = BollingerBands(close=self.df['close'], window=20, window_dev=2)
        
        self.df['bb_upper'] = bb.bollinger_hband()
        self.df['bb_middle'] = bb.bollinger_mavg()
        self.df['bb_lower'] = bb.bollinger_lband()
        
        current_price = self.df['close'].iloc[-1]
        
        self.signals['bollinger'] = {
            'upper': self.df['bb_upper'].iloc[-1],
            'middle': self.df['bb_middle'].iloc[-1],
            'lower': self.df['bb_lower'].iloc[-1],
            'price_position': (current_price - self.df['bb_lower'].iloc[-1]) / (
                self.df['bb_upper'].iloc[-1] - self.df['bb_lower'].iloc[-1]
            ),
            'touch_upper': current_price >= self.df['bb_upper'].iloc[-1],
            'touch_lower': current_price <= self.df['bb_lower'].iloc[-1],
        }
    
    def _calculate_stochastic(self):
        """Stochastic Oscillator - Momentum"""
        stoch = StochasticOscillator(
            high=self.df['high'],
            low=self.df['low'],
            close=self.df['close'],
            window=14,
            smooth_window=3
        )
        
        self.df['stoch_k'] = stoch.stoch()
        self.df['stoch_d'] = stoch.stoch_signal()
        
        self.signals['stochastic'] = {
            'k': self.df['stoch_k'].iloc[-1],
            'd': self.df['stoch_d'].iloc[-1],
            'oversold': self.df['stoch_k'].iloc[-1] < 20,
            'overbought': self.df['stoch_k'].iloc[-1] > 80,
            'bullish_crossover': (self.df['stoch_k'].iloc[-2] < self.df['stoch_d'].iloc[-2] and
                                  self.df['stoch_k'].iloc[-1] > self.df['stoch_d'].iloc[-1]),
        }
    
    def get_signals_summary(self):
        """Get a summary of all signals"""
        return self.signals
