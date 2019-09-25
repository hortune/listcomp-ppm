from random import randint
import json

def problem1():
    content = 'The first line would contain a positive integer N. Then there would be N lines below. Each line contains two integer A and B. Please output the corresponding A+B.'
    eg_input = '3\n1 2\n3 4\n5 6'
    eg_output = '3\n7\n11'
    testcases = []
    len_limit = 75
    MAX = 12312312321321321321321321312
    for i in range(5):
        input_, output_ = [], []
        q = randint(1000,10000)
        input_.append('{}'.format(q))
        
        for _ in range(q):
            a, b = randint(-MAX,MAX), randint(-MAX,MAX)
            input_.append('{} {}'.format(a,b))
            output_.append('{}'.format(a+b))
        testcases.append(('\n'.join(input_),'\n'.join(output_)))
    return content, eg_input, eg_output, testcases, len_limit

def problem2():
    content = 'This is the knapsack problem that you know. Sasdffan is going to buy some junk foods. However, he has only limited budgets M. Each junk food would have two attributes, the cost of buying the junk food and the value of eating the junk food. The first line contains two positive integers N and M. Then, there would be N lines below. Each line contains two positive integers v and c. (v: value, c: cost). Please output the maximum value that Sasdffan could get after consuming all the junk foods he bought. Caution: Each junk food could only be bought once.\n 1000 <= N <= 2000, 1 <= M <= 3000, 1 <= c <= 3000, v > 0'
    eg_input = '3 5\n1 2\n1 3\n2 2'
    eg_output = '3'
    testcases = []
    len_limit = 200
    MAX = 1231231232132132132
    for i in range(5):
        input_, output_ = [], []
        N, M = randint(100,250), randint(1000,2000)
        input_.append('{} {}'.format(N,M))
        dp = [[0]*(M+1) for i in range(N+1)]

        for idx in range(1,N+1):
            v, c = randint(1,9487), randint(1,2000)
            input_.append('{} {}'.format(v, c))
            
            for qq in range(0,M+1):
                dp[idx][qq] = max(dp[idx-1][qq-c] + v, dp[idx-1][qq]) if qq >= c else dp[idx-1][qq]

        output_.append("{}".format(dp[N][M]))
        testcases.append(('\n'.join(input_),'\n'.join(output_)))
    return content, eg_input, eg_output, testcases, len_limit

def problem3():
    content = 'Depth of the tree. There is a size N tree with node index from 0 to N-1. The first line is an integer N (tree size). Then, there would be N numbers in the next line each represents the father of the node. (0 is always the root). 10 <= N <=10000. Please notice that for any i, father[i] < i.'
    eg_input = '3\n0 0 1'
    eg_output = '2'
    testcases = []
    len_limit = 300
    MAX = 1231231232132132132
    
    for i in range(5):
        input_, output_ = [], []
        N = randint(10,10000)
        input_.append('{}'.format(N))
        edges = []
        for up in range(0, N):
            if up == 0:
                edges.append(0)
            else:
                edges.append(randint(0,up-1))
        input_.append(' '.join(map(str,edges)))
        ans = 0
        for cur in range(N-1, 0, -1):
            cur_ans = 0
            while edges[cur] != cur:
                cur_ans += 1
                cur = edges[cur]
            ans = max(cur_ans, ans)
        output_.append("{}".format(ans))
        testcases.append(('\n'.join(input_),'\n'.join(output_)))
    return content, eg_input, eg_output, testcases, len_limit

question = [problem1(), problem2(), problem3()]
json.dump(question,open('questions.json','w'))
