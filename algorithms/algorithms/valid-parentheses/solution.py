# 有效的括号（LeetCode 20）
# 思路：栈，遇到左括号压栈，遇到右括号检查栈顶是否匹配

def isvalid(s:str)->bool:
     stack=[]
     mapping={')':'(',']':'[','}':'{'}
     for ch in s:
          if ch in mapping.values():   #左括号
               stack.append(ch)
          elif ch in mapping:      #右
              if not stack or stack[-1]!=mapping[ch]:
                   return False
              stack.pop()
          else:
              return False
    return not stack
