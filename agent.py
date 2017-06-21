from piece import *
import operator
class Agent:
    def ALPHA_BETA_SEARCH(self, state, alpha, beta, depth=0):
        value = -1000000
        successors = state.getSuccessors(pColor.Black)
        global COUNT
        COUNT = 0
        myList = descendingSort(successors)
        for successor in myList:
            COUNT += 1
            successorValue = self.MIN_VALUE(successor, alpha, beta, depth + 1)
            if value < successorValue:
                value = successorValue
                ret = successor
            if value >= beta:
                break
            alpha = max(alpha, value)
        print('NUMBER OF NODES: ', COUNT)
        return ret

    def MAX_VALUE(self, state, alpha, beta, depth):
        if depth == 2:
            return state.evaluationFunction()
        v = -1000000
        successors = state.getSuccessors(pColor.Black)
        myList = descendingSort(successors)
        global COUNT
        for successor in myList:
            COUNT += 1
            v = max(v, self.MIN_VALUE(state, alpha, beta, depth + 1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def MIN_VALUE(self, state, alpha, beta, depth):
        if depth == 2:
            return state.evaluationFunction()
        v = 1000000
        successors = state.getSuccessors(pColor.White)
        myList = ascendingSort(successors)
        global COUNT
        for successor in myList:
            COUNT += 1
            v = min(v, self.MAX_VALUE(state, alpha, beta, depth + 1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

def ascendingSort(successors):
    myList = []
    for successor in successors:
        myList.append((successor, successor.evaluationFunction()))
    myList.sort(key=operator.itemgetter(1))
    ret = [k[0] for k in myList]
    return ret


def descendingSort(successors):
    myList = []
    for successor in successors:
        myList.append((successor, successor.evaluationFunction()))
    myList.sort(key=operator.itemgetter(1), reverse=True)
    ret = [k[0] for k in myList]
    return ret
