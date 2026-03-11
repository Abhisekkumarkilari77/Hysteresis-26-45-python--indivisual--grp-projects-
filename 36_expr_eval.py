# 36. Expression Evaluator
import operator
ops = {"+": (1, operator.add), "-": (1, operator.sub), "*": (2, operator.mul), "/": (2, operator.truediv)}

def is_float(s):
    try: float(s); return True
    except: return False

def to_postfix(tokens):
    out, stack = [], []
    for t in tokens:
        if t.isdigit() or is_float(t):
            out.append(t)
        elif t in ops:
            while stack and stack[-1] in ops and ops[stack[-1]][0] >= ops[t][0]:
                out.append(stack.pop())
            stack.append(t)
        elif t == "(": stack.append(t)
        elif t == ")":
            while stack and stack[-1] != "(": out.append(stack.pop())
            if stack: stack.pop()
    out.extend(reversed(stack))
    return out

def eval_postfix(pf):
    stack=[]
    for t in pf:
        if t in ops:
            b=float(stack.pop()); a=float(stack.pop())
            stack.append(ops[t][1](a,b))
        else: stack.append(float(t))
    return stack[0]

def evaluate(expr):
    tokens=[]; num=""
    for ch in expr.replace(" ",""):
        if ch.isdigit() or ch==".": num+=ch
        else:
            if num: tokens.append(num); num=""
            tokens.append(ch)
    if num: tokens.append(num)
    return eval_postfix(to_postfix(tokens))

if __name__ == "__main__":
    print(evaluate("(3+5)*2"))
