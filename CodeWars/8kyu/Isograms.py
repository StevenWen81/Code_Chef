# a = 97 ascii

def is_isogram(string):
     arr = [0 for i in range(26)]
     string = string.lower()
     for i in string:
          index = ord(i) - 97
          arr[index] += 1
     
     for i in  arr:
          if i > 1:
               return False
     return True
     
#print(is_isogram("moOse"))