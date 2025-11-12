# single inheritance 

class p:
    def par(self):
        return "hello - 1"
        
class c(p):
    def chl(self):
        return "hello - 2"
        
obj = c()

print(obj.chl())
print(obj.par())