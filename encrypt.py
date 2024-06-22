import os
import diffusion as dif
import confusion as con
import reshape as res
import cv2
import Image as i
import time
import tkinter as tk
from tkinter import filedialog as fd
import Key as k

def encrypt(filepath, destination_path, key):
    im_original = i.Image(filepath, i.Type.ORIGINAL, cv2.imread(filepath), key)
    print("\n")
    print(str(im_original.filename))
    print(im_original.dimension)
    print("\n")

    path = r"C:\Image Encryption and Decryption\images"

    #reshape the image into square
    start_time = time.perf_counter()
    im_reshaped = i.Image(path+"\\reshaped\\"+im_original.filename.split('.')[0]+".png", i.Type.RESHAPED, res.squareImage(im_original), key)
    elapsed_time = time.perf_counter() - start_time
    print(f"Time taken for reshaping: {elapsed_time:0.2f} seconds\n")
    cv2.imwrite(im_reshaped.filepath, im_reshaped.matrix)
    
    #confusion
    print("Confusion Starts:")
    start_time = time.perf_counter()
    im_confused = i.Image(path+"\\confused\\"+im_original.filename.split('.')[0]+".png", i.Type.CONFUSED, con.generateArnoldMap(im_reshaped), key)
    elapsed_time = time.perf_counter() - start_time
    print(f"Time taken for confusion: {elapsed_time:0.2f} seconds\n")
    cv2.imwrite(im_confused.filepath, im_confused.matrix)

    #diffusion
    print("Diffusion starts:")
    start_time = time.perf_counter()
    im_diffused = i.Image(destination_path+"\\"+im_original.filename.split('.')[0]+".png", i.Type.ENCRYPTED, dif.pixelManipulation(im_confused), key)
    cv2.imwrite(im_diffused.filepath, im_diffused.matrix)
    elapsed_time = time.perf_counter() - start_time
    print(f"Time taken for Diffusion: {elapsed_time:0.2f} seconds\n")
    print(im_diffused.dimension)


