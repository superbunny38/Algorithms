#17413
#단어 뒤집기2


string = input()

final_ans = []
temp_print = []
store = []
reverse = True
for s in string:
    if s == '<':
        final_ans += store
        store = []
        temp_print.append(s)
        reverse = False
    elif s== '>':
        temp_print.append(s)
        reverse = True
        final_ans += temp_print
        temp_print = []
        
    elif reverse == False:
        temp_print.append(s)
    elif reverse == True:
        if s == ' ':
            store.append(s)
            final_ans += store
            store = []
            
        else:
            store.insert(0,s)
    
if len(store) != 0 and len(string) != len(final_ans):
    final_ans += store

print(''.join(final_ans))
