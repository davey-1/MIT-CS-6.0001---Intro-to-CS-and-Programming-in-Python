def get_permutations(sequence):
    def solve(seq, flag, cur):
        if len(seq) == len(cur):
            return [cur]
        
        res = []
        
        for i in range(len(flag)):
            if flag[i]:
                new_flag = flag[::]
                new_flag[i] = False
                res += solve(seq, new_flag, cur + seq[i])
        
        return res
        
    return solve(sequence, [True] * len(sequence), "")


if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abcd'
    
    
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
  
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)