class Stack:
    def __init__(self):
        self.container = []
        self.count = 0
    
    def push(self, value):
        self.container.append(value)
        self.count += 1
        
    def pop(self):
        if self.count == 0:
            return -1
        self.count -= 1
        return self.container.pop()
        
    def size(self):
        return self.count
    
    def empty(self):
        if self.count == 0:
            return 1
        else:
            return 0
        
    def top(self):
        if self.count == 0:
            return -1
        return self.container[-1]
import sys       
stack = Stack()
N = int(sys.stdin.readline())
for _ in range(N):
    #commnd = input().split()
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.push(command[1])
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] =='empty':
        print(stack.empty())
    else:
        print(stack.top())