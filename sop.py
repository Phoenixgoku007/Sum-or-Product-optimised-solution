#opt value is used to optimise the code for processing very large numbers while performing multiplication

#opt=10^9+7=1000000007

# n is any number 

# q will be either 1 or o

def sumOrProduct(n, q):
    if(q==1):
        ans=(n*(n+1))//2 #sum of n numbers formula used for optimisation
        return ans
    else:
        m=1
        opt=1000000007 
        while(n):
            m=m*n
            n=n-1
        return m%opt
    
print(sumOrProduct(4,2))