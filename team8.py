####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

#Testing
team_name = 'NotSure TBH' # Only 10 chars displayed.
strategy_name = 'Ravid Dusnak'
strategy_description = 'Use of a slight favor of colluding and a strategy analysis.'
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    answer = 'c'
    colludeTotal = 0
    betrayTotal = 0
    theirTotal = int(len(their_history))
    strategy = 0
    if my_history == '':
        answer = 'c'
    if theirTotal <= 50 and theirTotal > 0:
        if their_history[-1] == 'c':
            colludeTotal += 1
        if their_history[-1] == 'b':
            betrayTotal += 1
        if their_history[-1] == 'b' and my_history[-1] == 'c':
            answer = 'b'
        if their_history[-1] == 'b' and my_history[-1] == 'b':
            answer = 'b'
        if their_history[-1] == 'c' and my_history[-1] == 'c':
            answer = 'c'
        if their_history[-1] == 'c' and my_history[-1] == 'b':
            answer = 'c'
    if theirTotal == 51:
        if colludeTotal == betrayTotal:
            strategy = 0
        if colludeTotal < betrayTotal:
            strategy = 0
        if colludeTotal > betrayTotal:
            strategy = 1
        answer = 'c'
    if theirTotal > 51:
        if strategy == 1:
            if my_history[-1] == 'c':
                answer =  'b'
            elif my_history[-2] == 'c' and my_history[-1] == 'b':
                answer = 'b'
            else:
                answer = 'c'
        if strategy == 0:
            if my_history[-1] == 'c':
                answer =  'c'
            elif my_history[-2] == 'c' and my_history[-1] == 'c':
                answer = 'b'
            else:
                answer = 'c'  
    return answer

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             