import random

#stworzenie klasy stosu zamiast listy, w celu utrudnienia sobie życia
class Stack:
  # lista defacto stosu
    def __init__(self):
        self.items = []
        
  # pusty
    def is_empty(self):
        return self.items == []
      
  # dodanie elementu
    def push(self,item):
        self.items.append(item)
        
  # wyjęcie elementu
    def pop(self):
        return self.items.pop()
      
  # pokazanie co jest następne do wyjęcia
    def top(self):
        return self.items[len(self.items)-1]
      
  # pokaż cały stos
    def see_stack(self):
        return self.items
      
  # pokaż rozmiar stosu(liczba elementów)
    def size(self):
        return len(self.items)
      
      
#stworzenie stosu
stack1 = Stack()
# dodawanie elementów do stosu
for i in range(0,5):
    stack1.push(random.randint(1,10))

print('Current stack: ', stack1.see_stack())
print('Current stack size: ', stack1.size())

#dodanie elementu na górę stosu
stack1.push(11)
print('Current stack: ', stack1.see_stack())
print('Current stack size: ', stack1.size())

# zpopujemy ostatni dodany element, a nie element dodany jako pierwszy
print('Popped element: ', stack1.pop())
print('Current stack size: ', stack1.size())
print('Current element at the top: ', stack1.top())
#jak widać kolejny element do "zdjęcia" z góry to element dodany do listy jako ostatni
