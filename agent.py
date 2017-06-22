from piece import *
import operator

class Agent:
    def ALPHA_BETA_SEARCH(self, state, alpha, beta, depth=0):
        value = -1000000
        acts = state.getActions(pColor.Black)
        successors = [state.result(act) for act in acts]
        actions = descendingSort(acts, successors)
        global COUNT
        COUNT = 0
        for action in actions:
            COUNT += 1
            tmp = self.MIN_VALUE(action[1], alpha, beta, depth+1)
            #tmp = self.MIN_VALUE(state.result(action), alpha, beta, depth+1)
            if tmp > value:
                ret = action[0]
                value = tmp
            if value >= beta:
                return ret
            alpha = max(alpha, value)
        print('Number of Nodes: ', COUNT)
        return ret

    def MAX_VALUE(self, state, alpha, beta, depth):
        if depth == 2:
            return state.evaluationFunction()
        value = -1000000
        acts = state.getActions(pColor.Black)
        successors = [state.result(act) for act in acts]
        actions = descendingSort(acts, successors)
        global COUNT
        for action in actions:
            COUNT += 1
            value = max(value, self.MIN_VALUE(action[1], alpha, beta, depth+1))
            #value = max(value, self.MIN_VALUE(state.result(action), alpha, beta, depth+1))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def MIN_VALUE(self, state, alpha, beta, depth):
        if depth == 2:
            return state.evaluationFunction()
        value = 1000000
        acts = state.getActions(pColor.White)
        successors = [state.result(act) for act in acts]
        actions = ascendingSort(acts, successors)
        global COUNT
        for action in actions:
            COUNT += 1
            value = min(value, self.MAX_VALUE(action[1], alpha, beta, depth+1))
            #value = min(value, self.MAX_VALUE(state.result(action), alpha, beta, depth+1))
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value

def ascendingSort(actions, states):
    evalList = [state.evaluationFunction() for state in states]
    ret = [(action, state) for (value, action, state) in sorted(zip(evalList, actions, states), key=lambda pair: pair[0])]
    return ret

def descendingSort(actions, states):
    evalList = [state.evaluationFunction() for state in states]
    ret = [(action, state) for (value, action, state) in sorted(zip(evalList, actions, states), key=lambda pair: pair[0], reverse=True)]
    return ret

