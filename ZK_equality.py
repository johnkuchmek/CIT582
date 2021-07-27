from zksk import Secret, DLRep
from zksk import utils

def ZK_equality(G,H):

    #Generate two El-Gamal ciphertexts (C1,C2) and (D1,D2)
    R1 = utils.get_random_num(bits=128)
    R2 = utils.get_random_num(bits=128)
    m = utils.get_random_num(bits=128)
    
    r1 = Secret(R1)
    r1_Prime = Secret(R1)
    r2 = Secret(R2)
    r2_Prime = Secret(R2)
    
    C1 = R1 * G
    C2 = R1 * H + m * G
    D1 = R2 * G
    D2 = R2 * H + m * G

    #Generate a NIZK proving equality of the plaintexts
    stmt = DLRep(C1,r1*G) 
    zk_proof = stmt.prove()

    #& DLRep(C2,r1_Prime*H+m*G) & DLRep(D1,r2*G) & DLRep(D2,r2_Prime*H+m*G)
    #Return two ciphertexts and the proof
    return (C1,C2), (D1,D2), zk_proof
