from utils import read_input

def main():
    line = read_input(day=6)
    
    chars = []
    for i in range(len(line)):
        c = line[i]
        
        if c in chars:
            while c in chars:
                chars.pop(0)
            chars.append(c)
        else:
            chars.append(c)
         
        if len(chars) == 14:
            print(i+1)
            break
    

if __name__ == '__main__':
    main()
