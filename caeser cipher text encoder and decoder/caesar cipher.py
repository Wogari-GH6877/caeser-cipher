import string
import  logo


check="yes"
alphabet = string.ascii_lowercase
print(logo.symbol)

while(check !="no"):
    def caeser(cipher_path,cipher_text,shift_amount):
        end_word=""
        if cipher_path=="encode":
            for i in text:
                if i in alphabet:
                    alphabet_index = alphabet.index(i) + shift
                    if alphabet_index >= 26:
                        alphabet_index = alphabet_index - 26
                        end_word += alphabet[alphabet_index]
                    else:
                        end_word += alphabet[alphabet_index]
                else:
                    end_word += i


        else:
            for i in text:
                if i in alphabet:
                    alphabet_index = alphabet.index(i) - shift
                    if alphabet_index <= 0:
                        alphabet_index = alphabet_index + 26
                        end_word += alphabet[alphabet_index]
                    else:
                        end_word += alphabet[alphabet_index]
                else:
                    end_word += i

        print(end_word)
    path = input("Type encode to 'encrypt', type to 'decode' decrypt : \n")
    text = input("Type Your Message here :\n").lower()
    shift = int(input("Type the shift Number:\n"))
    caeser (cipher_path=path, cipher_text=text, shift_amount=shift)
    check = input("Type 'yes' if you want to go agin . Otherwise type 'no").lower()




