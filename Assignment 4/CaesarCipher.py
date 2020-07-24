def main():
    print("Using Cesar Cipher to decode encrypted message from a file.")
    file=input("Enter file name:")
    open_file=open(file, "r")
    read_file=open_file.read()
    shift_number=int(input("Enter decode key:"))
    shift_number=shift_number%26
    new_file=input("Enter name of file to store decrypted message:")
    alphabet=['a', 'b', 'c' 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c' 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in read_file:
        if i in alphabet:
            i=shift_number+alphabet.index(i)
            i=alphabet[i]
        print (str(i))
        
 
main()
