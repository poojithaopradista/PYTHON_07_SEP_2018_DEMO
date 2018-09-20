
st = input("Enter a string : ")

pos = 0

while True:
    print (pos + 1)
    pos = st.find(' ',pos + 1)
    if pos == -1:
        break


