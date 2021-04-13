project_name = "Stock_span"
file = 'stock_span.ipynb'


get_ipython().getoutput("pip install jovian --upgrade --quiet")


import jovian


jovian.commit(project=project_name, filename=file)


GOOG = [2043,2036,1835,1751,1760,1621,1469,1634,1482,1413,1428,1348]
MSFT = [230,231,231,221,213,201,209,223,203,202,181,177]
AAPL = [119,121,131,132,118,108,115,128,105,90,78,72]
TSLA = [654,675,793,705,567,388,429,498,286,215,167,156]
AMZN = [3074,3092,3206,3256,3168,3036,3148,3450,3164,2758,2442,2474]
NVDA = [513,548,519,522,535,501,540,534,424,379,354,291]
INTC = [63,60,55,49,47,43,51,49,46,58,61,58]
AMD = [79,84,85,91,92,75,81,90,77,52,53,52]


# Reversing the list, because it was copy in desceding time order
GOOG = GOOG[::-1]
MSFT = MSFT[::-1]
AAPL = AAPL[::-1]
TSLA = TSLA[::-1]
AMZN = AMZN[::-1]
NVDA = NVDA[::-1]
INTC = INTC[::-1]
AMD = AMD[::-1]

# update lists
print('Updated List ascending order: \n','Google:',GOOG,'\n','Microsoft:',MSFT,'\n',
        'Apple:',AAPL,'\n','Tesla:',TSLA,'\n','Amazon:',AMZN,'\n',
        'Nvidia:',NVDA,'\n','Intel:',INTC,'\n','AMD:',AMD )


import matplotlib.pyplot as plt
import numpy as np

f, (ax1,ax2,ax3) = plt.subplots(1, 3, figsize=(20, 5))
index = np.arange(len(GOOG))
ax1.bar(np.arange(len(GOOG)),GOOG, color='pink')
ax1.set_title('Google prices')
ax2.bar(np.arange(len(MSFT)),MSFT, color='blue')
ax2.set_title('Microsoft prices')
ax3.bar(np.arange(len(AAPL)),AAPL,color='gray')
ax3.set_title('Apple prices')
f, (ax4,ax5,ax6) = plt.subplots(1, 3, figsize=(20, 5))
ax4.bar(np.arange(len(TSLA)),TSLA, color='red')
ax4.set_title('Tesla prices')
ax5.bar(np.arange(len(AMZN)),AMZN,color='orange')
ax5.set_title('Amazon prices')
ax6.bar(np.arange(len(NVDA)),NVDA,color='green')
ax6.set_title('Nvidia prices')
f, (ax7,ax8,ax9) = plt.subplots(1, 3, figsize=(20, 5))
ax7.bar(np.arange(len(INTC)),INTC, color='cyan')
ax7.set_title('Intel prices')
ax8.bar(np.arange(len(AMD)),AMD,color='black')
ax8.set_title('AMD prices')



# Create a function signature here. The body of the function can contain a single statement: pass
def span_brute(price): 
    pass      


import jovian


jovian.commit()


test0 = {
    'input': {'price': [10, -10 ,0, 5, 90, 120, 80, 100, 80, 60, 70, 60, 75, 85]},
    'output': [1, 1, 2, 3, 5, 6, 1, 2, 1, 1, 2, 1, 4, 6]
    }


test1 = {
    'input': {'price': [1348, 1428, 1413, 1482, 1634, 1469, 1621, 1760, 1751, 1835, 2036, 2043]},
    'output': [1, 2, 1, 4, 5, 1, 2, 8, 1, 10, 11, 12]}
test2 = {
    'input': {'price': [177, 181, 202, 203, 223, 209, 201, 213, 221, 231, 231, 230]},
    'output': [1, 2, 3, 4, 5, 1, 1, 3, 4, 10, 11, 1]}
test3 = {
    'input': {'price': [72, 78, 90, 105, 128, 115, 108, 118, 132, 131, 121, 119]},
    'output': [1, 2, 3, 4, 5, 1, 1, 3, 9, 1, 1, 1]}
test4 = {
    'input': {'price': [156, 167, 215, 286, 498, 429, 388, 567, 705, 793, 675, 654]},
    'output': [1, 2, 3, 4, 5, 1, 1, 8, 9, 10, 1, 1]}
test5 = {
    'input': {'price': [2474, 2442, 2758, 3164, 3450, 3148, 3036, 3168, 3256, 3206, 3092, 3074]},
    'output': [1, 1, 3, 4, 5, 1, 1, 3, 4, 1, 1, 1]}
test6 = {
    'input': {'price': [291, 354, 379, 424, 534, 540, 501, 535, 522, 519, 548, 513]},
    'output': [1, 2, 3, 4, 5, 6, 1, 2, 1, 1, 11, 1]}
test7 = {
    'input': {'price': [58, 61, 58, 46, 49, 51, 43, 47, 49, 55, 60, 63]},
    'output': [1, 2, 1, 1, 2, 3, 1, 2, 3, 7, 9, 12]}
test8 = {
    'input': {'price': [52, 53, 52, 77, 90, 81, 75, 92, 91, 85, 84, 79]},
    'output': [1, 2, 1, 4, 5, 1, 1, 8, 1, 1, 1, 1]}


tests = []


tests.append(test0)


# add more test cases
tests.append(test1)
tests.append(test2)
tests.append(test3)
tests.append(test4)
tests.append(test5)
tests.append(test6)
tests.append(test7)
tests.append(test8)


tests


jovian.commit()


jovian.commit()


def span_brute(price): 
    # Span value of first day is always 1 
    n = len(price)
    S = [None] * n
    S[0] = 1
    # it has 3 arguments:
    # price: the list of stock prices,
    # n: the lenght of the list pf prices and,
    # S: is the output and empty list of the stock prices with same size
    # Calculate span value of remaining days by linearly  
    # checking previous days 
    for i in range(0, len(price)): 
        S[i] = 1   # Initialize span value 
        # Traverse left while the next element on left is 
        # smaller than price[i] 
        j = i - 1
        while (j >= 0) and (price[i] >= price[j]):
            S[i] += 1
            j -= 1
    return S  


from jovian.pythondsa import evaluate_test_case


evaluate_test_case(span_brute, test0)


from jovian.pythondsa import evaluate_test_cases


res2= evaluate_test_cases(span_brute, tests)


n = 500
y1 = 15*n+1 
y2 = 25*n+10 

print(y1,y2)

y3 = 15*n**2+1 
y4 = 25*n**2+10 

print(y3,y4)


get_ipython().run_line_magic("matplotlib", " inline")
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

time_0 = [res2[0][2],res2[1][2],res2[2][2],res2[3][2],res2[4][2],res2[5][2],res2[6][2],res2[7][2],res2[8][2]]
time_01 = np.cumsum(time_0)
    
N = np.arange(0,9,1)

ax = plt.axes()
z = np.polyfit(N,time_01,2)
p = np.poly1d(z)
xp = np.linspace(0, 20)

plt.plot(N, time_01, '.', xp, p(xp),'-b', label='O(n²)')
# plt.plot(N, time_0, '-g', label='O(n)')
plt.title("Time complexity")
plt.legend();


jovian.commit()


jovian.commit()


jovian.commit()














jovian.commit()



