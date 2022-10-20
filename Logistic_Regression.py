import numpy
from sklearn import linear_model

# Dydis centimetrais (.reshape pakeičia eilutę į stulpelį)
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)

# Išskirstoma į dvi grupes (0 = NO, 1 = YES)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

'''
fit() yra LogisticRegression metodas kuris pasirenka nepriklausomas ir priklausomas reikšmes kaip parametrus 
ir užpildo regresijos objektą duomenimis, apibūdinančiais ryšį:
'''
logr = linear_model.LogisticRegression()
logr.fit(X, y)

# nustatoma kad 3.46 jau turi būti tinkama reikšmė
predicted = logr.predict(numpy.array([3.46]).reshape(-1, 1))

print(predicted)  # [0]

# Paskaičiuoja tikimybe tapti tinkamu
log_odds = logr.coef_
odds = numpy.exp(log_odds)

print(odds)  # [[4.03541657]]


'''
Sukurkite funkciją, kuri naudoja modelio koeficiento ir pertraukos reikšmes, kad grąžintų naują reikšmę. 
Ši nauja vertė parodo tikimybę,
'''
def logit2prob(logr, x):
    '''
    Norėdami rasti kiekvieno stebėjimo logaritminį koeficientą, pirmiausia turime sukurti formulę,
    kuri atrodo panaši į formulę iš tiesinės regresijos, išskiriant koeficientą ir pertrauką.
    '''
    log_odds = logr.coef_ * x + logr.intercept_
    # Norėdami konvertuoti log-odds į koeficientus, turime padidinti log-odds.
    odds = numpy.exp(log_odds)
    # Dabar, kai turime šansą, galime jį konvertuoti į tikimybę, padalydami iš 1 ir šansų.
    probability = odds / (1 + odds)
    return (probability)


print(logit2prob(logr, X))


