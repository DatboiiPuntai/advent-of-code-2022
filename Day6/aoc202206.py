def main():
    with open(r'Day6\input.txt', 'r') as f:
        line = f.read()
    
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
