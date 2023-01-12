def solution(X, A):
    answer = -1
    # Implement your solution here
    save_dict = dict()
    for idx, value_a in enumerate(A):
        if value_a in save_dict:
            save_dict[value_a] = min(idx,save_dict[value_a])
        else:
            save_dict[value_a] = idx

    max_t =0
    for leaf_pos in range(1,X+1):
        if leaf_pos not in save_dict:
            return answer
        if max_t < save_dict[leaf_pos]:
            max_t = save_dict[leaf_pos]
    answer = max_t
    return answer
