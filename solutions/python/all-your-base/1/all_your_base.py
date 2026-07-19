def rebase(input_base, digits, output_base):
    baseten=0
    mult=1
    n=len(digits)
    for i in range(n):
        digit=digits[i]
        baseten*=input_base
        baseten+=digit
    res=[]
    if input_base<2:
        raise ValueError("input base must be >= 2")
    if digits==[] or all(digit==0 for digit in digits):
        return [0]
    
    if any(digit<0 or digit>=input_base  for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base<2:
        raise ValueError("output base must be >= 2")
    while baseten:
        res.append(baseten%output_base)
        baseten=baseten//output_base
    return res[::-1]
        
