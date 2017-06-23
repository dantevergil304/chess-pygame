from piece import *
import operator

class Agent:
    def __init__(self):
        self.PV = [None] * 4
        self.MAX_DEPTH = 3
        self.CUR_DEPTH = 0

    def ITERATIVE_DEEPENING(self, state):
        depth = self.MAX_DEPTH
        for d in range(0, depth):
            self.CUR_DEPTH = d
            move = self.ALPHA_BETA_SEARCH(state, -1000000, 1000000, d+1)
        self.PV = [None] * 4
        return move

    def ALPHA_BETA_SEARCH(self, state, alpha, beta, depth):
        value = -1000000
        actions = state.getActions(pColor.Black)

        pos = self.CUR_DEPTH - depth + 1
        if self.PV[pos] is not None and self.PV[pos] in actions:
            ret = self.PV[pos]
            value = self.MIN_VALUE(state.result(self.PV[pos]), alpha, beta, depth-1)
            alpha = max(alpha, value)

        global COUNT
        COUNT = 0
        for action in actions:
            COUNT += 1

            if action == self.PV[pos]:
                continue
            tmp = self.MIN_VALUE(state.result(action), alpha, beta, depth-1)
            if tmp > value:
                ret = action
                value = tmp

            if value >= beta:
                return ret
            alpha = max(alpha, value)

        if depth == 1:
            self.PV[self.CUR_DEPTH] = ret
        if depth == self.MAX_DEPTH:
            print('Number of Nodes: ', COUNT)
        return ret

    def MAX_VALUE(self, state, alpha, beta, depth):
        if depth == 0:
            return state.evaluationFunction()
        value = -1000000
        actions = state.getActions(pColor.Black)

        pos = self.CUR_DEPTH - depth + 1
        if self.PV[pos] is not None and self.PV[pos] in actions:
            ret = self.PV[pos]
            value = self.MIN_VALUE(state.result(self.PV[pos]), alpha, beta, depth-1)
            alpha = max(alpha, value)

        global COUNT
        for action in actions:
            COUNT += 1

            if action == self.PV[pos]:
                continue
            tmp = self.MIN_VALUE(state.result(action), alpha, beta, depth-1)
            if tmp > value:
                ret = action
                value = tmp

            if value >= beta:
                return value
            alpha = max(alpha, value)

        if depth == 1:
            self.PV[self.CUR_DEPTH] = ret
        return value

    def MIN_VALUE(self, state, alpha, beta, depth):
        if depth == 0:
            return state.evaluationFunction()
        value = 1000000
        actions = state.getActions(pColor.White)

        pos = self.CUR_DEPTH - depth + 1
        if self.PV[pos] is not None and self.PV[pos] in actions:
            ret = self.PV[pos]
            value = self.MAX_VALUE(state.result(self.PV[pos]), alpha, beta, depth - 1)
            beta = min(beta, value)

        global COUNT
        for action in actions:
            COUNT += 1

            if action == self.PV[pos]:
                continue
            tmp = self.MAX_VALUE(state.result(action), alpha, beta, depth-1)
            if tmp < value:
                ret = action
                value = tmp

            if value <= alpha:
                return value
            beta = min(beta, value)

        if depth == 1:
            self.PV[self.CUR_DEPTH] = ret
        return value

