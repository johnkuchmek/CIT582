from zksk import Secret, DLRep
from zksk import utils

def ZK_equality(G,H):

    #Generate two El-Gamal ciphertexts (C1,C2) and (D1,D2)
    r1 = Secret(utils.get_random_num(bits=32))
    r2 = Secret(utils.get_random_num(bits=32))
    m = utils.get_random_num(bits=32)

    C1 = (r1 * G)
    print(C1)
    C2 = (r1 * H) + (m * G)
    print(C2)
    D1 = (r2 * G)
    print(D1)
    D2 = (r2 * H + m * G)
    print(D2)
    print("I worked!")

    #Generate a NIZK proving equality of the plaintexts
    stmt = DLRep(C1,r1*G) & DLRep(C2,r1*H+m*G) & DLRep(D1,r2*G) & DLRep(D2,r2*H+m*G)
    zk_proof = stmt.prove()


    #Return two ciphertexts and the proof
    return (C1,C2), (D1,D2), zk_proof

