
''' 
3. COURSECON International Summer Seminars - 2023 July & August

Genç Ekonomistler Kulübü

Lecture: Cemre Yoldaş / Leicester University

Create (Applied) : Yasin Tosun / Siegen University (Applied)

'''

# %% UYGULAMA 1

# 1. Kayıp Kaçınma (Loss Aversion)

"Kaybetme korkusuyla riskli kararlar almaya yönelme"

" Kaybetme korkusu hisse senedinin değerini tutmaktan daha baskın olabilir."

import random

# Rastgele bir hisse senedi getirisi simülasyonu
def simulate_stock_returns():
    return random.uniform(-0.1, 0.1)

def make_investment(current_value):
    if current_value >= 1000:
        decision = 'hold'
    else:
        decision = 'sell'
    return decision

initial_investment = 1000
current_value = initial_investment

for _ in range(1):
    decision = make_investment(current_value)
    stock_return = simulate_stock_returns()
    
    #Negatif hisse senedi getirisi varsa "sell" kararı al
    if stock_return < 0:
        decision = 'sell'
    if decision =='hold':
        current_value += stock_return * current_value
    elif decision == 'sell':
        current_value = current_value
    print("Karar:", decision)

print("Son portföy değeri:", current_value)

# 2. Aşırı Güven (Overconfidence)

"Kendini başkalarından daha yetenekli ve başarılı görme"

import random

# Rastgele bir hisse senedi getirisi simülasyonu
def simulate_stock_returns():
    return random.uniform(-0.1, 0.1)

def make_investment(prediction):
    return prediction + simulate_stock_returns()

initial_investment = 1000
current_value = initial_investment

# Tahmin edilen getiriler
predictions = [0.05, 0.03, 0.02, 0.08, 0.06, 0.04, 0.01, 0.07, 0.09, 0.03]

for prediction in predictions:
    stock_return = make_investment(prediction)
    current_value += stock_return * current_value

print("Son portföy değeri:", current_value)

# 3. Takip Etme Etkisi (Herding)

" Başkalarının davranışlarını takip ederek kararlar alma "


import random

# Rastgele bir hisse senedi getirisi oluşturma
def generate_stock_returns():
    return random.uniform(-0.1, 0.1)

def make_investment(decision, market_sentiment):
    if decision == 'follow':
        return market_sentiment + generate_stock_returns()
    elif decision == 'contrarian':
        return -market_sentiment + generate_stock_returns()
    else:
        raise ValueError("Geçersiz Karar")


initial_investment = 1000
current_value = initial_investment

# Piyasa duyarlılığı

market_sentiment = random.uniform(-0.1, 0.1)

# Follow durumunda diğer yatırımcıların davranışına göre karar alma
decision = 'follow'
for _ in range(10):
    stock_return = make_investment(decision, market_sentiment)
    current_value += stock_return * current_value
    
if current_value >= initial_investment:
    decision_result = 'Takip et'
else:
    decision_result = 'Contrarian'

print("Karar:", decision_result)
print("Son Portföy değeri:", current_value)



# 4. İmaj Önemi (Image Bias)

"Başkalarının algıladığı imajı korumak için finansal kararlar alma"

"""
Revenue 1.000.000 büyükse iyi gelir,
                    1.000.000. az ise kötü gelir.

Profitability değeri 0.25 den büyükse iyi karlı, 
                    0.25 den az ise kötü karlı.

Reputation değeri 7 ve üzerindeyse iyi performans, vice versa.

Branding değeri 7 ve üzeriyse iyi imajlı, vice versa.

"""

def image_bias(revenue, profitability, reputation, branding):
    if revenue > 1000000 and profitability > 0.25 and reputation >=7 and branding >= 7:
        decision = 'A: Rasyonel seçim yapılmıştır.'
    else:
        decision = 'B: Rasyonel olmayan seçim yapılmıştır.'
    print("Karar:", decision)

# image_bias (revenue, profitability, reputation, branding):

image_bias(1000001, 0.26, 9, 8)


# %% UYGULAMA 2

# 5. İçgüdüsel Yanıltma (Emotinal Bias)

"Duygusal tepkilerin finansal kararları etkilemesi"

def evaluate_investment(A,B,C):
    if C > 3 * A and C > 2 * B:
        return "C şirketinin seçimi en karlı  ve mantıklı seçimdir."
    elif B > 2 * A and B > 0.75 * C:
        return "B şirketinin seçimi optimaldir."
    elif A > 3 * C and A > 1.5 * B:
        return "A hissesinin seçimi yanlış, duygusal bir seçimdir."
    else:
        return "Geçersiz yatırım fırsatı!"


evaluate_investment(0.03, 0.09, 0.08)


# 6 . Sezgisel Karar Verme (Intuitive Decision Making)

" Duygusal hislerin ve sezgilerin mantıksal kararları baskılaması"

import random

nasdaq_stocks = [
    "AAPL", "GOOG", "AMZN", "MSFT", "FB", "TSLA", "NVDA", "ADBE",
    "PYPL", "INTC", "CSCO", "CMCSA", "PEP", "AMD", "COST", "AMGN", 
    "TXN", "QCOM","INTU", "ISRG", "GILD", "SBUX", "VRTX", "BKNG", 
    "MDLZ", "AVGO" ,"NFLX" , "ATVI", "ADP", "CSX"]

def emotional_choice(stocks):
    selected_stocks = random.sample([stock 
                                     for stock in stocks 
                                     if len(stock) == 2], 1)
    return selected_stocks

selected_stocks = emotional_choice(nasdaq_stocks)
print("Sezgisel karar verme:", selected_stocks)


# 7. Statüko Yanılgısı (Status Quo Bias)

"Mevcut durumu değiştirmek yerine mevcut durumu koruma eğilimi"

def selected_package(gold_value, silver_value, bronze_value):
    if gold_value < silver_value * 2 and gold_value < bronze_value * 2 :
        return "Seçilen paket: Gold"
    elif silver_value < bronze_value * 1.5 :
        return "Seçilen paket: Silver"
    else :
        return "Seçilen paket: Bronze"

selected_package(1600, 600, 500)























