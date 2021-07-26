from zksk import Secret, DLRep
from zksk import utils

def ZK_equality(G,H):

    #Generate two El-Gamal ciphertexts (C1,C2) and (D1,D2)
    R1 = utils.get_random_num(bits=32)
    R2 = utils.get_random_num(bits=32)
    r1 = Secret(R1)
    r2 = Secret(R2)
    m = utils.get_random_num(bits=32)

    C1 = (r1 * G)
    C2 = r1 * H + m * G
    D1 = (r2 * G)
    D2 = r2 * H + m * G

    #Generate a NIZK proving equality of the plaintexts
    print("trying to state stuff")
    stmt = DLRep(C1,r1*G) & DLRep(C2,r1*H+m*G) & DLRep(D1,r2*G) & DLRep(D2,r2*H+m*G)
    print("I am here")

    zk_proof = stmt.prove()


    #Return two ciphertexts and the proof
    return (C1,C2), (D1,D2), zk_proof

