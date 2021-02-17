val(root,5).
alphabeta( Pos, Alpha, Beta, GoodPos, Val) :-
moves( Pos, Poslist), !,
boundedbest( Poslist, Alpha, Beta, GoodPos, Val);
staticval( Pos, Val).
boundedbest( [Pos | Poslist], Alpha, Beta, GoodPos, GoodVal) :-
alphabeta( Pos, Alpha, Beta, _, Val),
goodenough( Poslist, Alpha, Beta, Pos, Val, GoodPos, GoodVal).
goodenough( [], -, -, Pos, Val, Pos, Val) :- !.
goodenough( -, Alpha, Beta, Pos, Val, Pos, Val) :-
min_to_move( Pos), Val > Beta, !;  %Maximizer attained upper bound
max_to_move( Pos), Val < Alpha, !. %Minimizer attained lower bound
goodenough( Poslist, Alpha, Beta, Pos, Val, GoodPos, GoodVal) :-
newbounds( Alpha, Beta, Pos, Val, NewAlpha, NewBeta), % Refine bounds
boundedbes( Poslist, NewAlpha, NewBeta, Posl, Vall),
betterof( Pos, Val, Posl, Vall, GoodPos, GoodVal).
newbounds( Alpha, Beta, Pos, Val, Val, Beta) :-
min_to_move( Pos), val > Alpha, !. % Maximizer increased lower bound
newbounds( Alpha, Beta, Pos, Val, Alpha, val) :-
max_to_move( Pos), Val < Beta, !. % Minimizer decreased upper bound
newbounds( Alpha, Beta, _, _, Alpha, Beta).
betterof( Pos, Val, pos1, Val1, Pos, Val) :-
min_to_move( Pos), val > Val1, !;
max_to_move( Pos), Val < Val1, !.
betterof( -, -, Pos1, val1, Pos1, val1).
