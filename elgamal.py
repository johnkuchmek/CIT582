import random

from params import p
from params import g

def keygen():
    rand = random.seed(a=None, version = 2)
    q = (p-1)/2
    a = random.randint(1,q)
    sk = a
    pk = pow(g,a,p)
    return pk,sk

def encrypt(pk,m):
    rand = random.seed(a=None, version = 2)
    q = (p-1)/2
    r = random.randint(1,q)
    c1 = pow(g,r,p)
    c2 = pk * pow(m,1,p)
    return [c1,c2]

def decrypt(sk,c):
    c1 = c[0]
    c2 = c[1]
    m = pow(c2/c1^sk,1,p)
    return m

