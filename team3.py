import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
#Version 1.1
team_name = 'Rogue Three' # Only 10 chars displayed.
strategy_name = 'Trying to be Nice'
strategy_description = 'The strategy generally colludes for the beginning of the game, and then using a counter variable sees if the other team colludes or betrays more. If they collude more we continue colluding. If they betray more we betray. If it cannot be determined it is random.'       
colludeNumber = 0
betrayNumber = 0
randomRoundDistance = 0
currentRound = 0 
runMethodRound = 0
def move(my_history, their_history, my_score, their_score, colludeNumber, betrayNumber):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if their_history[-1] == 'c':
        colludeNumber += 1
    if their_history[-1] == 'b':
        betrayNumber += 1
    
    if len(my_history) < 10:
        return 'c'
    
    else:
        if (colludeNumber > betrayNumber + 5 ):
            return 'c'
        elif (colludeNumber < betrayNumber + 5):
            return 'b'
        else:
             guesser = random.range(0,1,1)
             if (guesser == 0):
                 return 'c'
             if (guesser == 1):
                 return 'b'   
            
    
  
  

    return 'c'
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
 

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" + ", ".join(["'"+my_history+"'", "'"+their_history+"'", str(my_score), str(their_score)])+ ") returned " + "'" + real_result + "'" + " and should have returned '" + result + "'")
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
def counter(their_history, colludeNumber, betrayNumber):
    if their_history[-1] == 'c':
        colludeNumber += 1
    if their_history[-1] == 'b':
        betrayNumber += 1
            
def colludeForRandom(currentRound, runMethodRound):
    
    randomRoundCounter = random.range(3,7,1)
    if currentRound < (runMethodRound + randomRoundCounter):
        return 'c'
    else:
        return 'b'
        runMethodRound = currentRound
  
                
                    