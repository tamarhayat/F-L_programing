%רקורסיה ורשימות
%1
reverse([], []).

reverse([H|T], Z) :- 
    reverse(T, TReversed), 
    append(TReversed, [H], Z).

%2
member(X, [X|_]).

member(X, [_|T]) :- 
    member(X, T).    
    
%3
palindrome(L) :- reverse(L, L). 

%4
sorted([]).
sorted([_]).
sorted([X, Y | T]) :- 
    X =< Y, 
    sorted([Y | T]).

%5
permutation([], []).

% recursiun - remove 1 (by "select") and check all the permutation
permutation(L, [X|P]) :- 
    select(X, L, Rest), 
    permutation(Rest, P).

%remove 1 and return the rest of the list
select(X, [X|T], T).

select(X, [H|T], [H|Rest]) :- 
    select(X, T, Rest).


