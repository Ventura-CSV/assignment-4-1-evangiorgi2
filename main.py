def main():
    result = []
    #az = "abcdefghijklmnopqrstuvwxyz"
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the ending letter: ')
        
        
        
        for ch in range(ord(start), ord(end)+1):
           result.append(chr(ch))
           
           if (ord(start) > ord(end)):
               print('Input Error.')
               break
           
           
        print(result)
            
            
    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
