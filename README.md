<h1>Mathematical ciphers</h1>
<h3>"</h3>
<p>Despite the advantages for an agent in using keyword
substitution, most of the ciphers produced and studied by
modern cryptographers are automated and rely on
mathematics to provide the encryption. On the other side
of the cyber battle lie the cryptanalysts, who spend
every waking hour applying more mathematics to try to
break these ciphers.</p>

<p>A good way to start thinking mathematically is to revisit
the Caesar shift cipher which can be viewed as a type of
addition.</p>

<p>Each letter is first encoded by its numerical position in
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
required range.</p>

<p>You can think of this as putting the numbers 0 - 25 on a
clock face and adding them by counting round the face. We
do this when telling the time. Three hours after 11
o’clock is 2 o’clock, which we get by adding 3+11 = 14,
then subtracting 12 to get 2.</p>

<p>The military use the 24-hour clock, and 4 hours after
what they call “23 Hundred Hours” is 3am, which is given
by adding 4 +23 =27, then subtracting 24.</p>

<p>Mathematicians call this modular arithmetic. The standard
12-hour clock is just arithmetic mod 12, the military
clock is arithmetic mod 24, and the Caesar cipher is
carried out using arithmetic mod 26.</p>

<P>Just to recap, returning to our Caesar shift cipher, the
shift by 3 sends 6 to 6+3=9, which corresponds to mapping
the plaintext letter g to the ciphertext letter J. At the
end of the alphabet we have x mapping to A, y mapping to
B and z mapping to C which correspond to the modular
arithmetic 23+3=0 mod 26, 24+3=1 mod 26 and 25+3=2 mod 26.</P>

<p>There is a convenient shorthand for the Caesar shift by
n, given by</p>



<pre id="myPreTag">x → x+n.<br></pre>

<p>Here we are using x to stand for the position of a
letter, and n to stand for the shift amount, i.e., x and
n are each one of the values 1–26, rather than letters in
the English alphabet. The shift is defined by the
integer n, which can take any one of 26 values, and this
gives all 26 Caesar shift ciphers. Putting n=0 we don’t
move the letters at all, which is not much use, so in
practice, as we noted in the first section, there are
only 25 different useable Caesar shift ciphers.</p>

<h3>"</h3>
