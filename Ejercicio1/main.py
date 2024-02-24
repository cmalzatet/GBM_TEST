def palindrome(input: str):    
    if isinstance(input, str):
        process_input = input.lower().replace(' ','')
        return True if process_input == process_input[::-1] else False
    else:
        return False
    

if __name__ == "__main__":
    input = input()
    print(palindrome(input))
