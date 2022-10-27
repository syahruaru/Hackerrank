if __name__ == '__main__':
    grade_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade_score.append([name,score])
    # print(grade_score)
    sorted_ = sorted(list(set([x[1] for x in grade_score])))
    
    second_lowest = sorted_[1]
    
    low_list  = []
    for name in grade_score:
        if second_lowest == name[1]:
            low_list.append(name[0])
    for name in sorted(low_list):
        print(name)
