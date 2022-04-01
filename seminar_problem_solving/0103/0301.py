#week 0301 problem
def score_average():
    print("성적을 입력하세요. :")
    score_list = []
    while(True):
        score = input("점수(0~100) : ")
        if score == 'q':
            break
        try:
            score = int(score)
            if score <0 or score >100:
                print("Error!(Out of range)")
                continue
            else:
                score_list.append(score)
        except:
            print("Error!(Wrong value)")
            continue
        
        
    print("sum:",sum(score_list))
    print("average:",sum(score_list)/len(score_list))
    


score_average()
