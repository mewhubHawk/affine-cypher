<h1>Mathematical ciphers</h1>
Despite the advantages for an agent in using keyword
substitution, most of the ciphers produced and studied by
modern cryptographers are automated and rely on
mathematics to provide the encryption. On the other side
of the cyber battle lie the cryptanalysts, who spend
every waking hour applying more mathematics to try to
break these ciphers.
A good way to start thinking mathematically is to revisit
the Caesar shift cipher which can be viewed as a type of
addition.
Each letter is first encoded by its numerical position in
the alphabet. For reasons lost in the mists of time the
convention is that we take a to lie in position 0, b in
position 1 and so on, and the Caesar shift is then given
by adding a constant to each of the positions. So if a is
shifted to D that corresponds to moving a three places
along the alphabet, or in other words to adding 3 to all
the positions. You have to think a bit about how to deal
with x, y and z here since 23+3=26, 24+3=27 and 25+3=28, and
there are no letters in those positions, but since those
letters move to A, B, C in positions 0,1,2 we can fix
that by changing our addition so that when the answer is
bigger than 26 we subtract 26 to put it back in the
required range.
You can think of this as putting the numbers 0 - 25 on a
clock face and adding them by counting round the face. We
do this when telling the time. Three hours after 11
o’clock is 2 o’clock, which we get by adding 3+11 = 14,
then subtracting 12 to get 2.
