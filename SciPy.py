import scipy
import numpy as np

from scipy import constants
from math import cos
from scipy.optimize import root
from scipy.sparse import csr_matrix


def Break(x):
    txt ='{} -------------------------------------------------------------------------------------------------------------'
    print(txt.format(x))
def Comm(x):
    txt ='---- {} ----'
    print('')
    print(txt.format(x))
    print('')

'''„SciPy“ yra mokslinė skaičiavimo biblioteka, kurios apačioje naudojama „NumPy“.
SciPy reiškia Scientific Python.
Tai suteikia daugiau naudingų funkcijų optimizavimui, statistikai ir signalų apdorojimui.
Kaip ir „NumPy“, „SciPy“ yra atvirojo kodo, todėl galime juo laisvai naudotis.
„SciPy“ sukūrė „NumPy“ kūrėjas Travisas Olliphantas.'''

print(scipy.__version__)
print(constants.liter) # Kiek kubinių metrų yra viename litre
print(constants.pi) # PI reikšmė
print(dir(constants)) # Visos reikšmės

Comm('NumPy gali rasti daugianarių ir tiesinių lygčių šaknis, bet negali rasti šaknų netiesinėms lygtims, kaip ši:x + cos(x)')

def eqn(x):
  return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)

from scipy.optimize import minimize

Comm('Sumažinkite funkciją x^2 + x + 2 naudodami BFGS:')

def eqn(x):
  return x**2 + x + 2
mymin = minimize(eqn, 0, method='BFGS')
print(mymin)

Comm('CSR – suspausta reta eilutė. Greitam eilučių pjaustymui, greitesniems matricos vektoriniams produktams')

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data)

Comm('Nenulių skaičiavimas')
print(csr_matrix(arr).count_nonzero())

Comm('Nulinių įrašų pašalinimas')
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)

Comm('Pasikartojančių įrašų pašalinimas')
mat.sum_duplicates()
print(mat)

Comm('Konvertavimas iš csr į csc')
newarr = csr_matrix(arr).tocsc()
print(newarr)