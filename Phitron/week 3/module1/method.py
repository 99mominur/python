class Phone:
    color = "black"
    feature = ["waterproof", "big battery"]
    def call(self):
        print("ring ring ring")
    def messege(self, text, number):
        print("\n% Sort Messege Service %")
        mess = f'SMS: {text}\nTo: {number}\n'
        return mess
    
my_phone = Phone()

my_phone.call()
mess = my_phone.messege('I miss you', 5108561457)
print(mess)
