def ALPHA_BETA_SEARCH(self, gameState, currentDepth, depth, numAgent, alpha, beta):
    legalActions = gameState.getLegalActions(0)
    value = -1000000
    decision = "stop"
    for action in legalActions:
        successor = gameState.generateSuccessor(0, action)
        successorValue = self.MIN_VALUE(
            successor, currentDepth + 1, depth, numAgent, alpha, beta)
        if value < successorValue:
            value = successorValue
            decision = action
        if value > beta:
            return decision
        alpha = max(alpha, value)
    return decision


def MAX_VALUE(self, gameState, currentDepth, depth, numAgent, alpha, beta):
    agentIndex = currentDepth % numAgent
    legalActions = gameState.getLegalActions(agentIndex)
    if not legalActions or currentDepth == depth:
        return self.evaluationFunction(gameState)

    value = -1000000
    for action in legalActions:
        successor = gameState.generateSuccessor(agentIndex, action)
        value = max(value, self.MIN_VALUE(
            successor, currentDepth + 1, depth, numAgent, alpha, beta))
        if value > beta:
            return value
        alpha = max(alpha, value)
    return value


def MIN_VALUE(self, gameState, currentDepth, depth, numAgent, alpha, beta):
    agentIndex = currentDepth % numAgent
    legalActions = gameState.getLegalActions(agentIndex)
    if not legalActions or currentDepth == depth:
        return self.evaluationFunction(gameState)

    value = 1000000
    for action in legalActions:
        successor = gameState.generateSuccessor(agentIndex, action)
        if agentIndex == numAgent - 1:
            value = min(value, self.MAX_VALUE(
                successor, currentDepth + 1, depth, numAgent, alpha, beta))
        else:
            value = min(value, self.MIN_VALUE(
                successor, currentDepth + 1, depth, numAgent, alpha, beta))

        if value < alpha:
            return value
        beta = min(beta, value)
    return value