
cipher = 0x45b27f14b63071e0dcb260e85487241f767b8f7ba4a204f05a7e80841a4e45e2bdd91ec12e45a232ec66e258764dd97976aac18ab1ed96215b1f8776138fee75

#------------------number1--------------------------
n=12023325850010357245649581501933969602916802638115216449772319681620470831578013813691303285987744778300580064402311091477633041850117891610819309854950051
#e590cae5263ecdfe4f0c08fd66e2876e087e208adc4712517692905fa9b6c216c872a02d5ce032db3a521d5621c452a112ebfc7d7b5567c735a3e86f640682a3
#ca8a8b58cdfb8f87967a89dbf9505828ceb96940dac4a1f6d9e4ca187d06500a5a1aa2373670b8dd74659a22e4aba8d827315fb142e8ab9c739adb21fc639a21
p1=108856750554505701104706423850040410423616169573220585632850452978727311547097
p2=110450897980738030698105875416384588344493349807787967612535656573955573253083


#----------------number2-----------------------------
n=10676767715644279168180667738863623917884880122958252914418362799603762576985881985721052155015614082289355200925605126741588148459527747016865826518437451
#0xcbdaf418c0065668e545e475b1122639782d0307d3ecb450b860618e1a344b37e2e2d0aa5900e7bc2d6cfb327cfbb45e443e95eea64a6281fb4ad992c5a58e4b
#47af7942f2d3c7b31f5cd297e86a9f727a2629f8a8b78639147d20111e79e130e7230ab5c4239b5620bb9c410e7a59764829b9b2fcd5f928d2eb1eb8021b2991
p1=100127313021045771890581393202222629531593312891900833131046186292352986230837
p2=106631920836626546504833225776168295102130361766400116368453816656257265898623
e = 65537


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

d = modinv(e, (p1-1)*(p2-1))
print 'n', '%x'%n
print 'd', '%x'%d
premastersecret = pow(cipher, d, n)
print hex(premastersecret)
assert(pow(premastersecret, e, n) == cipher)