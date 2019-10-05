import epicbox
import hashlib
from random import randint
from sys import stderr

epicbox.configure(
    profiles=[
        #epicbox.Profile('python', 'python:3.6.5-alpine')
        epicbox.Profile('python', 'hortune/python3.6-alpine')
    ]
)

q_num = 0

def is_valid(digest, diff):
    bits = ''.join(bin(i)[2:].zfill(8) for i in digest)
    return bits[:diff] == '0' * diff

def proofofwork():
    hardness = 23
    prefix = hex(randint(1000000000000000000000000000000000000, 123123123213123000000123213**3))[-18:-2] 
    print(f'prefix = "{prefix}"')
    print(f'sha256(prefix + answer) has {hardness} leading zeros. (In binary)')
    print("input:")
    inp = input().strip()
    s = prefix + inp
    assert is_valid(hashlib.sha256(s.encode()).digest(), hardness)

def propose(question, example_input, example_output, testcases, len_limit):
    global q_num
    print("Question:",question)
    print("Example Input:\n",example_input,sep='',end='\n\n')
    print("Example Output:\n",example_output,sep='')
    print("Input Length Limit:", len_limit)
    print("Your list comprehension code:")
    content = input()
    assert len(content) < len_limit, 'Length exceed limit'
    assert content.find('"') == -1, 'Find invalid character "'
    assert content.find("'") == -1, 'Find invalid character \''
    new_content = '[\n'+ content +'\n]'
    
    for idx, (input_, output_) in enumerate(testcases):
        files = [{'name': 'main.py', 'content': new_content.encode('utf-8')},
                 {'name': 'input', 'content': input_.encode('utf-8')}]
        limits = {'cputime': 3, 'memory': 512}
        n_result = epicbox.run('python', 'python3 main.py < input', files=files, limits=limits)

        files = [{'name': 'main.py', 'content': content.encode('utf-8')},
                 {'name': 'input', 'content': input_.encode('utf-8')}]
        limits = {'cputime': 3, 'memory': 512}
        result = epicbox.run('python', 'python3 main.py < input', files=files, limits=limits)
                
        #print(n_result['exit_code'], result['exit_code'], n_result['stdout'], result['stdout'])
        if not (n_result['exit_code'] is not None and not n_result['exit_code']):
            print("Runtime Error QQ")
            exit(1)

        if not (result['exit_code'] is not None and not result['exit_code']):
            print("Runtime Error QQ")
            exit(1)
            
        if not (n_result['stdout'].decode('utf-8').strip() == result['stdout'].decode('utf-8').strip() == output_.strip()):
            print("Wrong Answer QQ")
            exit(1)

        print("Pass the {} test case.".format(idx), flush=True)
    print('Congrats! You pass question {}.'.format(q_num))
    q_num += 1
    
print(
"""
Welcome to the list comprehension ppm!!!
We are the guy that loves to solve programming problems with list comprehension.
In this challenge, all of your code should be only one line long. xD

By the way, your code would be tested by **directly running** and tested by running with **"[\\n{}\\n]".format(code)**.


There are three small challenges!!!

Conqure all and get the flag!!!
"""
)


import json
proofofwork()
questions = json.load(open('questions.json'))
for question in questions:
    propose(*question)

print('FLAG:Balsn{8_8_l13t_c0mp63h3ns10n_0r_A_5en8_80x_ch01l3n93}')
