import os
import diffusion as dif
import confusion as con
import reshape as res
import cv2
import Image as i
import time
import Key as k


def decrypt(filepath, destination_path, key):
    im_encrypted = i.Image(filepath, i.Type.ENCRYPTED, cv2.imread(filepath, cv2.IMREAD_UNCHANGED), key)
    print("\n")
    print(im_encrypted.filename)
    print(im_encrypted.dimension)
    print("\n")

    path = r"C:\Image Encryption and Decryption\images"
    
    #undiffusion
    print("Undiffusion Starts:")
    start_time = time.perf_counter()
    im_undiffused = i.Image(path+"\\undiffused\\"+im_encrypted.filename.split('.')[0]+".png", i.Type.UNDIFFUSED, dif.pixelManipulation(im_encrypted), key)
    cv2.imwrite(im_undiffused.filepath, im_undiffused.matrix)
    elapsed_time = time.perf_counter() - start_time
    print(f"Time taken for undiffusion: {elapsed_time:0.2f} seconds")

    #unconfusion
    print("Unconfusion Starts:")
    start_time = time.perf_counter()
    im_unconfused = i.Image(path+"\\unconfused\\"+im_encrypted.filename.split('.')[0]+".png", i.Type.UNCONFUSED, con.reconstructArnoldMap(im_undiffused), key)
    elapsed_time = time.perf_counter() - start_time
    print(f"Time taken for unconfusion: {elapsed_time:0.2f} seconds")
    cv2.imwrite(im_unconfused.filepath, im_unconfused.matrix)

    #reshape crop border
    start_time = time.perf_counter()
    im_decrypted = i.Image(destination_path+"\\"+im_encrypted.filename.split('.')[0]+".png", i.Type.DECRYPTED, res.cropBorder(im_unconfused), key)
    elapsed_time = time.perf_counter() - start_time
    cv2.imwrite(im_decrypted.filepath, im_decrypted.matrix)
