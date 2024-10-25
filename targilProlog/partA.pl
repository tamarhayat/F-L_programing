parent(Avraham,Yitshak).
parent(Avraham,Yishmael).
parent(Sara,Yitshak).
parent(Sara,Yishmael).
parent(Yitzhak,Yahakov).
parent(Yitzhak,Esav).
parent(Rivka,Yahakov).
parent(Rivka,Esav).
parent(Yahakov,Yosef).
parent(Yahakov,Binyamin).
parent(Rachel,Yosef).
parent(Rachel,Binyamin).

male(Avraham).
male(Yitzhak).
male(Yishmael).
male(Yahakov).
male(Esav).
male(Yosef).
male(Binyamin).

female(Sara).
female(Rivka).
female(Rachel).


married(Avraham,Sara).
married(Yitzhak,Rivka).
married(Yahakov,Rachel).

/*Important note!
I didn't forget Leah, I just think 2 women will get a little complicated here..*/


is_father(X, Y) :- parent(X, Y), male(X).	
is_mother(X, Y) :- parent(X, Y), female(X).
is_son(X,Y) :- parent(Y,X), male(X).
is_daughter(X,Y) :- parent(Y,X), female(X).
is_grandfather(X, Y) :- parent(X, Z), parent(Z, Y), male(X).
is_grandmother(X, Y) :- parent(X, Z), parent(Z, Y), female(X).
is_grandson(X, Y) :- parent(Y, Z), parent(Z, X), male(X).
is_granddaughter(X, Y) :- parent(Y, Z), parent(Z, X), female(X).
is_sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
is_uncle(X, Y) :- married(X,M), is_sibling(M, Z), parent(Z, Y), male(X).
is_son_of_aunt(X,Y) :- is_son(X,A), female(A), is_sibling(A,B), parent(B,Y). %assume the aunt is with blood conect
is_brother_in_law(X, Y) :- married(X, Z), sibling(Z, Y), male(X).
is_niece(X, Y) :- sibling(Y, Z), parent(Z, X), female(X).
is_cousin(X,Y) :- parent(A, X), parent(B, Y), is_sibling(A, B).%add it for my comfortable
is_second_cousin(X, Y) :- parent(A, X), parent(B, Y), is_cousin(A, B).



















