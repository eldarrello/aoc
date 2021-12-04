def process(s, input, output):
    ip = 0    
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
        
def load():
    with open("input.txt") as f:
        s = f.read().split(',')
    s = [int(a) for a in s]
    return s
    
def evaluate(p):
  input = []
  output = [0]
  for i in range(5):    
      s = load()
      input.append(p[i])
      input.append(output.pop())
      #print(input)
      process(s, input, output)
      #print(output)
  return output.pop()
  
import random    
phases = [0,1,2,3,4]
max = 0
while True:
    random.shuffle(phases)
    #print(phases)
    result = evaluate(phases)
    if result > max:
        max = result
        print(max, phases)

