"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random


class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def custom_score_1(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    nrof_mymoves = len(game.get_legal_moves(player))
    nrof_opmoves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(nrof_mymoves - 2*nrof_opmoves)

def custom_score_2(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    
    my_score = 0
    opp_score = 0

    center_x = game.height/2
    center_y = game.width/2
    #get_close to edges is better
    for x, y in game.get_legal_moves(player):
        my_score += abs(center_x - x) + abs(center_y - y)

    for x, y in game.get_legal_moves(game.get_opponent(player)):
        opp_score += abs(center_x - x) + abs(center_y - y)

    return float(my_score - opp_score)

def custom_score_3(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    
    my_score = 0
    opp_score = 0

    center_x = game.height/2
    center_y = game.width/2
    #get_close to edges is better
    for x, y in game.get_legal_moves(player):
        my_score += center_x-abs(center_x - x) + center_y- abs(center_y - y)

    for x, y in game.get_legal_moves(game.get_opponent(player)):
        opp_score += center_x- abs(center_x - x) + center_y- abs(center_y - y)

    return float(my_score - opp_score)

def custom_score_4(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    
    my_score = 0
    opp_score = 0

    center_x = game.height/2
    center_y = game.width/2
    remain_spc_pct = len(game.get_blank_spaces()) / (game.height * game.width)


    for x, y in game.get_legal_moves(player):
        my_score += ((1-remain_spc_pct)*(center_x-abs(center_x - x) + center_y- abs(center_y - y))+remain_spc_pct * (abs(center_x-x)+abs(center_y-y)))

    for x, y in game.get_legal_moves(game.get_opponent(player)):
        opp_score += ((1-remain_spc_pct)*(center_x-abs(center_x - x) + center_y- abs(center_y - y))+remain_spc_pct * (abs(center_x-x)+abs(center_y-y)))
    return float(my_score - opp_score)

def custom_score_5(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    
    my_score = 0
    opp_score = 0

    center_x = game.height/2
    center_y = game.width/2
    remain_spc_pct = len(game.get_blank_spaces()) / (game.height * game.width)


    for x, y in game.get_legal_moves(player):
        my_score += ((remain_spc_pct)*(center_x-abs(center_x - x) + center_y- abs(center_y - y))+(1-remain_spc_pct) * (abs(center_x-x)+abs(center_y-y)))

    for x, y in game.get_legal_moves(game.get_opponent(player)):
        opp_score += ((remain_spc_pct)*(center_x-abs(center_x - x) + center_y- abs(center_y - y))+(1-remain_spc_pct) * (abs(center_x-x)+abs(center_y-y)))
    return float(my_score - opp_score)

def custom_score_6(game, player):
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    
    
    my_score = 0
    opp_score = 0

    center_x = game.height/2
    center_y = game.width/2
    remain_spc_pct = len(game.get_blank_spaces()) / (game.height * game.width)


    for x, y in game.get_legal_moves(player):
        my_score += (1-remain_spc_pct) * 2
        my_score += ((remain_spc_pct)*(center_x-abs(center_x - x) 
        + center_y- abs(center_y - y))+(1-remain_spc_pct) * (abs(center_x-x)+abs(center_y-y)))

    for x, y in game.get_legal_moves(game.get_opponent(player)):
        opp_score +=(1-remain_spc_pct) * 2
        opp_score += ((remain_spc_pct)*(center_x-abs(center_x - x) + center_y- abs(center_y - y))
        +(1-remain_spc_pct) * (abs(center_x-x)+abs(center_y-y)))
    return float(my_score - opp_score)


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    
    return custom_score_4(game, player)


class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)  This parameter should be ignored when iterative = True.

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).  When True, search_depth should
        be ignored and no limit to search depth.

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            DEPRECATED -- This argument will be removed in the next release

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left

        # TODO: finish this function!

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves
        if (len(legal_moves)==0):
            return (-1,-1)
        else:
            move = legal_moves[0]

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring
            if self.iterative:
                depth = 0
                while move != (-1,-1):
                    depth += 1
                    if self.method is 'minimax':
                        _, move = self.minimax(game, depth)
                    elif self.method is 'alphabeta':
                        _, move = self.alphabeta(game, depth)
                    if self.time_left() < self.TIMER_THRESHOLD:
                        raise Timeout()
            else:
                if self.method is 'minimax':
                    _, move = self.minimax(game, self.search_depth)
                elif self.method is 'alphabeta':
                    _, move = self.alphabeta(game, self.search_depth)
                if self.time_left() < self.TIMER_THRESHOLD:
                    raise Timeout()

        except Timeout:
            # Handle any actions required at timeout, if necessary
            return move

        # Return the best move from the last completed search iteration
        return move



    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """

        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()        
        

        nodes= game.get_legal_moves()

        if not nodes:
            return float("-inf"),(-1,-1)

        if depth == 0:
            return self.score(game, self), nodes[0]

        if maximizing_player:
            best_v= float("-inf")
            best_node =(-1,-1)

            for node in nodes:
                v, _= self.minimax(game.forecast_move(node), depth-1, False)
                #minimax(game.forecast_move(node),depth-1,False)
                if v>best_v:
                    best_v=v
                    best_node= node
            return best_v,best_node
        
        else:
            best_v= float("inf")
            best_node =(-1,-1)
            for node in nodes:
                v, _= self.minimax(game.forecast_move(node), depth-1, True)
                if v<best_v:
                    best_v=v
                    best_node= node
            return best_v,best_node



    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        nodes = game.get_legal_moves()

        best_move = (-1, -1)
        #according to wiki Pseudocode
        if not nodes:
            return self.score(game, self), game.get_player_location(self)


        if depth == 0:
            return self.score(game, self), game.get_player_location(self)
        if maximizing_player:
            v=float("-inf")
            for child in nodes:
                value, _= self.alphabeta(game.forecast_move(child), depth-1, alpha, beta, False)

                if v < value:
                    v = value
                    best_move = child
                alpha = max(v,alpha)
                if alpha >= beta:
                    break
            return v, best_move

        else:
            v= float("inf")
            for child in nodes:
                value,_= self.alphabeta(game.forecast_move(child), depth-1 ,alpha, beta, True)

                if v > value:
                    v = value
                    best_move = child

                beta = min(beta,v)
                if beta <= alpha:
                    break
            return v, best_move
        
