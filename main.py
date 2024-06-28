def main():
    result = ''
 
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the ending letter: ')
        
        if (ord(start) > ord(end)):
            print('Input Error.')
               
        
        for ch in range(ord(start), ord(end)+1):
           result = result + chr(ch)
           
           
           
        
        print(result)
            
            
    

    ########################################
    # Do not delete the return statement
    ########################################
        return result


if __name__ == '__main__':
    main()
