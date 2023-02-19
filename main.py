# Uygulama - Mülakat Sorusu
#######################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

ifade = "hi my name is john and i am learning python"

def mulakat(str):
    new_ifade= ""
    for irem in range(len(str)):
        if irem % 2 == 0:
         new_ifade += str[irem].upper()
        else:
         new_ifade += str[irem].lower()
    print(new_ifade)

mulakat(ifade)

# alternating fonksiyonunun enumerate ile yazılması

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate(ifade)