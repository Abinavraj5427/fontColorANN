import random
with open("test.csv",'w',encoding = 'utf-8') as f:
    f.write("R,G,B,Font")
    for i in range(1000000):
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        luminance = ( 0.299 * R + 0.587 * G + 0.114 * B)/255
        if(luminance > 0.5):
            f.write("\n"+str(R)+","+str(G)+","+str(B)+","+str(0))
        else:
            f.write("\n"+str(R)+","+str(G)+","+str(B)+","+str(1))
    f.close()