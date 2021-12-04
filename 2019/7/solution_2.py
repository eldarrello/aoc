def process(s, ip, input, output):    
    while s[ip] != 99:
        opcode = s[ip] % 100
        mode = s[ip] - opcode
        p1_im = mode % 1000 == 100
        mode -= mode % 1000
        p2_im = mode % 10000 == 1000
        if opcode == 1:
           p1 = s[ip + 1] if p1_im else s[s[ip + 1]]
           p2 = s[ip + 2] if p2_im else s[s[ip + 2]]
           s[s[ip + 3]] = p1 + p2
           ip += 4
        elif opcode == 2:
           p1 = s[ip + 1] if p1_im else s[s[ip + 1]]
           p2 = s[ip + 2] if p2_im else s[s[ip + 2]]
           s[s[ip + 3]] = p1 * p2
           ip += 4
        elif opcode == 3:
           s[s[ip + 1]] = input.pop(0)
           ip += 2
        elif opcode == 4:
           p = s[ip + 1] if p1_im else s[s[ip + 1]]
           output.append(p)
           ip += 2
           return [s, ip]
        elif opcode == 5:
           p1 = s[ip + 1] if p1_im else s[s[ip + 1]]
           p2 = s[ip + 2] if p2_im else s[s[ip + 2]]            
           if p1 != 0:
               ip = p2
           else:
               ip += 3
        elif opcode == 6:
           p1 = s[ip + 1] if p1_im else s[s[ip + 1]]
           p2 = s[ip + 2] if p2_im else s[s[ip + 2]]            
           if p1 == 0:
               ip = p2
           else:
               ip += 3
        elif opcode == 7:
           p1 = s[ip + 1] if p1_im else s[s[ip + 1]]
           p2 = s[ip + 2] if p2_im else s[s[ip + 2]]            
           s[s[ip + 3]] = 1 if p1 < p2 else 0
           ip += 4
        elif opcode == 8:
           p1 = s[ip + 1] if p1_im else s[s[ip + 1]]
           p2 = s[ip + 2] if p2_im else s[s[ip + 2]]            
           s[s[ip + 3]] = 1 if p1 == p2 else 0
           ip += 4
        else:
           print('error')
           a = 1
    return [[], 0]
        
def load():
    with open("input.txt") as f:
        s = f.read().split(',')
    s = [int(a) for a in s]
    return s
    
def evaluate(p):
  input = []
  output = [0]
  init = True
  s = load()
  ss = []
  sip = [0, 0, 0, 0, 0]
  for i in range(5):
      ss.append(s)
  while True:
    for i in range(5):
      #print(i, output)
      if init:  
          input.append(p[i])
      input.append(output.pop())
      r = process(ss[i], sip[i], input, output)
      ss[i] = r[0]
      sip[i] = r[1]
      if len(r[0]) == 0:
          return cur_output
    init = False
    cur_output = output[0]
  
import random    
phases = [5, 6, 7, 8, 9]
max = 0
while True:
    random.shuffle(phases)
    #print(phases)
    result = evaluate(phases)
    if result > max:
        max = result
        print(max, phases)

