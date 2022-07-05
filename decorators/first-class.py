# def say_hello():
#     print("Merhaba Samet")

# selamla = say_hello
# selamla()

def good_morning(name):
    print("Günaydın", name)

def greet(func):
    print("Fonksiyon öncesi işlemler")
    func("Mustafa")
    print("Fonksiyon sonrası işlemler")

greet(good_morning)

