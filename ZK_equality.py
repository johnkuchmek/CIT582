from zksk import Secret, DLRep
from zksk import utils

def ZK_equality(G,H):

    #Generate two El-Gamal ciphertexts (C1,C2) and (D1,D2)
    R1 = utils.get_random_num(bits=128)
    R2 = utils.get_random_num(bits=128)
    r1 = Secret(R1)
    r2 = Secret(R2)
    m = utils.get_random_num(bits=128)

    C1 = (R1 * G)
    C2 = R1 * H + m * G
    D1 = (R2 * G)
    D2 = R2 * H + m * G

    #Generate a NIZK proving equality of the plaintexts
    stmt = DLRep(C1,R1*G) & DLRep(C2,R1*H+m*G) & DLRep(D1,R2*G) & DLRep(D2,R2*H+m*G)
    zk_proof = stmt.prove()


    #Return two ciphertexts and the proof
    return (C1,C2), (D1,D2), zk_proof

