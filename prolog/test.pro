%% -------------- Defined Functions --------------
if(Test, Then, _) :- Test, !, Then.
if(_ , _ , Else) :- Else.

