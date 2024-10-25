%1
%א
scum(1, 1).

scum(N, Res) :- 
    N > 1,
    scum(N-1,ResAll),
    Res is ResAll+N.

%ב
sumDigits(0, 0).

sumDigits(Num, Sum) :- 
    Num > 0,
    Digit is Num mod 10,
    Rest is Num // 10,
    sumDigits(Rest, SumRest),
    Sum is Digit + SumRest.

%2 
%א
split(0, []).

split(N, [Digit | Rest]) :-
    N > 0,
    Digit is N mod 10,
    NewN is N // 10,
    split(NewN, Rest).

%ב
create([], 0).

create([Digit | Rest], N) :-
    create(Rest, NRest),
    N is NRest * 10 + Digit.
%ג
reverseNumber(Num, Reversed) :-
    split(Num, Digits),
    reverse(Digits, RevDigits),
    create(RevDigits, Reversed).

%3
%א
intersection([], _, []).

intersection([X | T1], L2, [X | Z]) :-
    member(X, L2),
    intersection(T1, L2, Z).

intersection([_ | T1], L2, Z) :-
    intersection(T1, L2, Z).

%ב
minus([], _, []).

% if x in L2 we will not add it to Z
minus([X | T1], L2, [X | Z]) :-
    \+ member(X, L2),
    minus(T1, L2, Z).

% if x in L2 we will not add it
minus([X | T1], L2, Z) :-
    member(X, L2),
    minus(T1, L2, Z).





    