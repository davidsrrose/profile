# Examining the 'Perfect' Shuffle

 If you shuffle a deck of cards *perfectly*, will the deck return to the start order? How many shuffles would that take?

 Let's find out.

## Defining a Perfect Shuffle

We will define a 'perfect' shuffle as a *Riffle Shuffle.*

To perform a classic riffle shuffle:

1. Divide the deck into two equal halves
2. Combine the decks, allowing the cards to interlace one at a time
3. Square up the deck and repeat

# Lets get shuffling and find out! 

## Before Shuffling
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; width: 100%;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20A.jpg" alt="Diamonds | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%202.jpg" alt="Diamonds | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%203.jpg" alt="Diamonds | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%204.jpg" alt="Diamonds | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%205.jpg" alt="Diamonds | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%206.jpg" alt="Diamonds | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%207.jpg" alt="Diamonds | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%208.jpg" alt="Diamonds | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%209.jpg" alt="Diamonds | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%2010.jpg" alt="Diamonds | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20J.jpg" alt="Diamonds | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20Q.jpg" alt="Diamonds | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20K.jpg" alt="Diamonds | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20A.jpg" alt="Clubs | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%202.jpg" alt="Clubs | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%203.jpg" alt="Clubs | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%204.jpg" alt="Clubs | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%205.jpg" alt="Clubs | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%206.jpg" alt="Clubs | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%207.jpg" alt="Clubs | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%208.jpg" alt="Clubs | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%209.jpg" alt="Clubs | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%2010.jpg" alt="Clubs | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20J.jpg" alt="Clubs | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20Q.jpg" alt="Clubs | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20K.jpg" alt="Clubs | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20A.jpg" alt="Hearts | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%202.jpg" alt="Hearts | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%203.jpg" alt="Hearts | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%204.jpg" alt="Hearts | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%205.jpg" alt="Hearts | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%206.jpg" alt="Hearts | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%207.jpg" alt="Hearts | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%208.jpg" alt="Hearts | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%209.jpg" alt="Hearts | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%2010.jpg" alt="Hearts | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20J.jpg" alt="Hearts | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20Q.jpg" alt="Hearts | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20K.jpg" alt="Hearts | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20A.jpg" alt="Spades | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%202.jpg" alt="Spades | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%203.jpg" alt="Spades | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%204.jpg" alt="Spades | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%205.jpg" alt="Spades | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%206.jpg" alt="Spades | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%207.jpg" alt="Spades | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%208.jpg" alt="Spades | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%209.jpg" alt="Spades | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%2010.jpg" alt="Spades | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20J.jpg" alt="Spades | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20Q.jpg" alt="Spades | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20K.jpg" alt="Spades | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
</div>

## After Shuffle 1
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; width: 100%;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20A.jpg" alt="Diamonds | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20A.jpg" alt="Hearts | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%202.jpg" alt="Diamonds | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%202.jpg" alt="Hearts | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%203.jpg" alt="Diamonds | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%203.jpg" alt="Hearts | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%204.jpg" alt="Diamonds | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%204.jpg" alt="Hearts | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%205.jpg" alt="Diamonds | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%205.jpg" alt="Hearts | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%206.jpg" alt="Diamonds | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%206.jpg" alt="Hearts | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%207.jpg" alt="Diamonds | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%207.jpg" alt="Hearts | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%208.jpg" alt="Diamonds | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%208.jpg" alt="Hearts | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%209.jpg" alt="Diamonds | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%209.jpg" alt="Hearts | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%2010.jpg" alt="Diamonds | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%2010.jpg" alt="Hearts | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20J.jpg" alt="Diamonds | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20J.jpg" alt="Hearts | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20Q.jpg" alt="Diamonds | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20Q.jpg" alt="Hearts | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20K.jpg" alt="Diamonds | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20K.jpg" alt="Hearts | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20A.jpg" alt="Clubs | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20A.jpg" alt="Spades | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%202.jpg" alt="Clubs | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%202.jpg" alt="Spades | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%203.jpg" alt="Clubs | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%203.jpg" alt="Spades | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%204.jpg" alt="Clubs | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%204.jpg" alt="Spades | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%205.jpg" alt="Clubs | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%205.jpg" alt="Spades | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%206.jpg" alt="Clubs | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%206.jpg" alt="Spades | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%207.jpg" alt="Clubs | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%207.jpg" alt="Spades | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%208.jpg" alt="Clubs | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%208.jpg" alt="Spades | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%209.jpg" alt="Clubs | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%209.jpg" alt="Spades | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%2010.jpg" alt="Clubs | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%2010.jpg" alt="Spades | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20J.jpg" alt="Clubs | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20J.jpg" alt="Spades | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20Q.jpg" alt="Clubs | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20Q.jpg" alt="Spades | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20K.jpg" alt="Clubs | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20K.jpg" alt="Spades | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
</div>

## After Shuffle 2
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; width: 100%;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20A.jpg" alt="Diamonds | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20A.jpg" alt="Clubs | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20A.jpg" alt="Hearts | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20A.jpg" alt="Spades | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%202.jpg" alt="Diamonds | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%202.jpg" alt="Clubs | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%202.jpg" alt="Hearts | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%202.jpg" alt="Spades | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%203.jpg" alt="Diamonds | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%203.jpg" alt="Clubs | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%203.jpg" alt="Hearts | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%203.jpg" alt="Spades | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%204.jpg" alt="Diamonds | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%204.jpg" alt="Clubs | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%204.jpg" alt="Hearts | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%204.jpg" alt="Spades | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%205.jpg" alt="Diamonds | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%205.jpg" alt="Clubs | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%205.jpg" alt="Hearts | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%205.jpg" alt="Spades | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%206.jpg" alt="Diamonds | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%206.jpg" alt="Clubs | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%206.jpg" alt="Hearts | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%206.jpg" alt="Spades | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%207.jpg" alt="Diamonds | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%207.jpg" alt="Clubs | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%207.jpg" alt="Hearts | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%207.jpg" alt="Spades | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%208.jpg" alt="Diamonds | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%208.jpg" alt="Clubs | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%208.jpg" alt="Hearts | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%208.jpg" alt="Spades | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%209.jpg" alt="Diamonds | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%209.jpg" alt="Clubs | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%209.jpg" alt="Hearts | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%209.jpg" alt="Spades | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%2010.jpg" alt="Diamonds | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%2010.jpg" alt="Clubs | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%2010.jpg" alt="Hearts | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%2010.jpg" alt="Spades | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20J.jpg" alt="Diamonds | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20J.jpg" alt="Clubs | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20J.jpg" alt="Hearts | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20J.jpg" alt="Spades | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20Q.jpg" alt="Diamonds | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20Q.jpg" alt="Clubs | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20Q.jpg" alt="Hearts | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20Q.jpg" alt="Spades | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20K.jpg" alt="Diamonds | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20K.jpg" alt="Clubs | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20K.jpg" alt="Hearts | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20K.jpg" alt="Spades | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
</div>

## After Shuffle 3
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; width: 100%;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20A.jpg" alt="Diamonds | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%207.jpg" alt="Hearts | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20A.jpg" alt="Clubs | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%207.jpg" alt="Spades | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20A.jpg" alt="Hearts | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%208.jpg" alt="Diamonds | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20A.jpg" alt="Spades | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%208.jpg" alt="Clubs | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%202.jpg" alt="Diamonds | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%208.jpg" alt="Hearts | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%202.jpg" alt="Clubs | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%208.jpg" alt="Spades | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%202.jpg" alt="Hearts | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%209.jpg" alt="Diamonds | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%202.jpg" alt="Spades | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%209.jpg" alt="Clubs | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%203.jpg" alt="Diamonds | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%209.jpg" alt="Hearts | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%203.jpg" alt="Clubs | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%209.jpg" alt="Spades | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%203.jpg" alt="Hearts | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%2010.jpg" alt="Diamonds | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%203.jpg" alt="Spades | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%2010.jpg" alt="Clubs | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%204.jpg" alt="Diamonds | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%2010.jpg" alt="Hearts | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%204.jpg" alt="Clubs | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%2010.jpg" alt="Spades | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%204.jpg" alt="Hearts | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20J.jpg" alt="Diamonds | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%204.jpg" alt="Spades | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20J.jpg" alt="Clubs | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%205.jpg" alt="Diamonds | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20J.jpg" alt="Hearts | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%205.jpg" alt="Clubs | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20J.jpg" alt="Spades | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%205.jpg" alt="Hearts | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20Q.jpg" alt="Diamonds | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%205.jpg" alt="Spades | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20Q.jpg" alt="Clubs | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%206.jpg" alt="Diamonds | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20Q.jpg" alt="Hearts | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%206.jpg" alt="Clubs | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20Q.jpg" alt="Spades | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%206.jpg" alt="Hearts | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20K.jpg" alt="Diamonds | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%206.jpg" alt="Spades | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20K.jpg" alt="Clubs | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%207.jpg" alt="Diamonds | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20K.jpg" alt="Hearts | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%207.jpg" alt="Clubs | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20K.jpg" alt="Spades | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
</div>

## After Shuffle 4
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; width: 100%;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20A.jpg" alt="Diamonds | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%204.jpg" alt="Clubs | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%207.jpg" alt="Hearts | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%2010.jpg" alt="Spades | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20A.jpg" alt="Clubs | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%204.jpg" alt="Hearts | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%207.jpg" alt="Spades | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20J.jpg" alt="Diamonds | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20A.jpg" alt="Hearts | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%204.jpg" alt="Spades | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%208.jpg" alt="Diamonds | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20J.jpg" alt="Clubs | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20A.jpg" alt="Spades | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%205.jpg" alt="Diamonds | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%208.jpg" alt="Clubs | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20J.jpg" alt="Hearts | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%202.jpg" alt="Diamonds | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%205.jpg" alt="Clubs | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%208.jpg" alt="Hearts | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20J.jpg" alt="Spades | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%202.jpg" alt="Clubs | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%205.jpg" alt="Hearts | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%208.jpg" alt="Spades | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20Q.jpg" alt="Diamonds | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%202.jpg" alt="Hearts | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%205.jpg" alt="Spades | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%209.jpg" alt="Diamonds | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20Q.jpg" alt="Clubs | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%202.jpg" alt="Spades | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%206.jpg" alt="Diamonds | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%209.jpg" alt="Clubs | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20Q.jpg" alt="Hearts | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%203.jpg" alt="Diamonds | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%206.jpg" alt="Clubs | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%209.jpg" alt="Hearts | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20Q.jpg" alt="Spades | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%203.jpg" alt="Clubs | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%206.jpg" alt="Hearts | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%209.jpg" alt="Spades | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20K.jpg" alt="Diamonds | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%203.jpg" alt="Hearts | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%206.jpg" alt="Spades | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%2010.jpg" alt="Diamonds | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20K.jpg" alt="Clubs | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%203.jpg" alt="Spades | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%207.jpg" alt="Diamonds | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%2010.jpg" alt="Clubs | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20K.jpg" alt="Hearts | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%204.jpg" alt="Diamonds | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%207.jpg" alt="Clubs | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%2010.jpg" alt="Hearts | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20K.jpg" alt="Spades | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
</div>

## After Shuffle 5
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; width: 100%;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20A.jpg" alt="Diamonds | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%209.jpg" alt="Diamonds | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%204.jpg" alt="Clubs | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20Q.jpg" alt="Clubs | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%207.jpg" alt="Hearts | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%202.jpg" alt="Spades | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%2010.jpg" alt="Spades | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%206.jpg" alt="Diamonds | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20A.jpg" alt="Clubs | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%209.jpg" alt="Clubs | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%204.jpg" alt="Hearts | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20Q.jpg" alt="Hearts | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%207.jpg" alt="Spades | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%203.jpg" alt="Diamonds | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20J.jpg" alt="Diamonds | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%206.jpg" alt="Clubs | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20A.jpg" alt="Hearts | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%209.jpg" alt="Hearts | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%204.jpg" alt="Spades | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20Q.jpg" alt="Spades | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%208.jpg" alt="Diamonds | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%203.jpg" alt="Clubs | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20J.jpg" alt="Clubs | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%206.jpg" alt="Hearts | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20A.jpg" alt="Spades | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%209.jpg" alt="Spades | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%205.jpg" alt="Diamonds | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20K.jpg" alt="Diamonds | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%208.jpg" alt="Clubs | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%203.jpg" alt="Hearts | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20J.jpg" alt="Hearts | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%206.jpg" alt="Spades | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%202.jpg" alt="Diamonds | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%2010.jpg" alt="Diamonds | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%205.jpg" alt="Clubs | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20K.jpg" alt="Clubs | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%208.jpg" alt="Hearts | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%203.jpg" alt="Spades | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20J.jpg" alt="Spades | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%207.jpg" alt="Diamonds | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%202.jpg" alt="Clubs | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%2010.jpg" alt="Clubs | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%205.jpg" alt="Hearts | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20K.jpg" alt="Hearts | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%208.jpg" alt="Spades | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%204.jpg" alt="Diamonds | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20Q.jpg" alt="Diamonds | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%207.jpg" alt="Clubs | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%202.jpg" alt="Hearts | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%2010.jpg" alt="Hearts | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%205.jpg" alt="Spades | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20K.jpg" alt="Spades | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
</div>

## After Shuffle 6
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; width: 100%;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20A.jpg" alt="Diamonds | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%205.jpg" alt="Diamonds | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%209.jpg" alt="Diamonds | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20K.jpg" alt="Diamonds | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%204.jpg" alt="Clubs | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%208.jpg" alt="Clubs | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20Q.jpg" alt="Clubs | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%203.jpg" alt="Hearts | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%207.jpg" alt="Hearts | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20J.jpg" alt="Hearts | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%202.jpg" alt="Spades | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%206.jpg" alt="Spades | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%2010.jpg" alt="Spades | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%202.jpg" alt="Diamonds | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%206.jpg" alt="Diamonds | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%2010.jpg" alt="Diamonds | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20A.jpg" alt="Clubs | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%205.jpg" alt="Clubs | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%209.jpg" alt="Clubs | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20K.jpg" alt="Clubs | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%204.jpg" alt="Hearts | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%208.jpg" alt="Hearts | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20Q.jpg" alt="Hearts | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%203.jpg" alt="Spades | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%207.jpg" alt="Spades | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20J.jpg" alt="Spades | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%203.jpg" alt="Diamonds | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%207.jpg" alt="Diamonds | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20J.jpg" alt="Diamonds | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%202.jpg" alt="Clubs | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%206.jpg" alt="Clubs | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%2010.jpg" alt="Clubs | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20A.jpg" alt="Hearts | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%205.jpg" alt="Hearts | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%209.jpg" alt="Hearts | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20K.jpg" alt="Hearts | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%204.jpg" alt="Spades | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%208.jpg" alt="Spades | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20Q.jpg" alt="Spades | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%204.jpg" alt="Diamonds | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%208.jpg" alt="Diamonds | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20Q.jpg" alt="Diamonds | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%203.jpg" alt="Clubs | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%207.jpg" alt="Clubs | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20J.jpg" alt="Clubs | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%202.jpg" alt="Hearts | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%206.jpg" alt="Hearts | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%2010.jpg" alt="Hearts | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20A.jpg" alt="Spades | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%205.jpg" alt="Spades | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%209.jpg" alt="Spades | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20K.jpg" alt="Spades | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
</div>

## After Shuffle 7
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; width: 100%;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20A.jpg" alt="Diamonds | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%203.jpg" alt="Diamonds | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%205.jpg" alt="Diamonds | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%207.jpg" alt="Diamonds | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%209.jpg" alt="Diamonds | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20J.jpg" alt="Diamonds | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20K.jpg" alt="Diamonds | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%202.jpg" alt="Clubs | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%204.jpg" alt="Clubs | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%206.jpg" alt="Clubs | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%208.jpg" alt="Clubs | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%2010.jpg" alt="Clubs | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20Q.jpg" alt="Clubs | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20A.jpg" alt="Hearts | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%203.jpg" alt="Hearts | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%205.jpg" alt="Hearts | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%207.jpg" alt="Hearts | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%209.jpg" alt="Hearts | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20J.jpg" alt="Hearts | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20K.jpg" alt="Hearts | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%202.jpg" alt="Spades | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%204.jpg" alt="Spades | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%206.jpg" alt="Spades | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%208.jpg" alt="Spades | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%2010.jpg" alt="Spades | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20Q.jpg" alt="Spades | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%202.jpg" alt="Diamonds | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%204.jpg" alt="Diamonds | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%206.jpg" alt="Diamonds | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%208.jpg" alt="Diamonds | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%2010.jpg" alt="Diamonds | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20Q.jpg" alt="Diamonds | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20A.jpg" alt="Clubs | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%203.jpg" alt="Clubs | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%205.jpg" alt="Clubs | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%207.jpg" alt="Clubs | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%209.jpg" alt="Clubs | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20J.jpg" alt="Clubs | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20K.jpg" alt="Clubs | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%202.jpg" alt="Hearts | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%204.jpg" alt="Hearts | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%206.jpg" alt="Hearts | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%208.jpg" alt="Hearts | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%2010.jpg" alt="Hearts | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20Q.jpg" alt="Hearts | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20A.jpg" alt="Spades | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%203.jpg" alt="Spades | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%205.jpg" alt="Spades | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%207.jpg" alt="Spades | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%209.jpg" alt="Spades | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20J.jpg" alt="Spades | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20K.jpg" alt="Spades | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
</div>

## After Shuffle 8
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; width: 100%;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20A.jpg" alt="Diamonds | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%202.jpg" alt="Diamonds | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%203.jpg" alt="Diamonds | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%204.jpg" alt="Diamonds | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%205.jpg" alt="Diamonds | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%206.jpg" alt="Diamonds | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%207.jpg" alt="Diamonds | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%208.jpg" alt="Diamonds | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%209.jpg" alt="Diamonds | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%2010.jpg" alt="Diamonds | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20J.jpg" alt="Diamonds | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20Q.jpg" alt="Diamonds | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Diamonds%20|%20K.jpg" alt="Diamonds | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20A.jpg" alt="Clubs | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%202.jpg" alt="Clubs | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%203.jpg" alt="Clubs | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%204.jpg" alt="Clubs | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%205.jpg" alt="Clubs | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%206.jpg" alt="Clubs | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%207.jpg" alt="Clubs | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%208.jpg" alt="Clubs | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%209.jpg" alt="Clubs | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%2010.jpg" alt="Clubs | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20J.jpg" alt="Clubs | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20Q.jpg" alt="Clubs | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Clubs%20|%20K.jpg" alt="Clubs | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20A.jpg" alt="Hearts | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%202.jpg" alt="Hearts | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%203.jpg" alt="Hearts | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%204.jpg" alt="Hearts | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%205.jpg" alt="Hearts | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%206.jpg" alt="Hearts | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%207.jpg" alt="Hearts | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%208.jpg" alt="Hearts | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%209.jpg" alt="Hearts | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%2010.jpg" alt="Hearts | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20J.jpg" alt="Hearts | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20Q.jpg" alt="Hearts | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Hearts%20|%20K.jpg" alt="Hearts | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20A.jpg" alt="Spades | A.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%202.jpg" alt="Spades | 2.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%203.jpg" alt="Spades | 3.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%204.jpg" alt="Spades | 4.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%205.jpg" alt="Spades | 5.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%206.jpg" alt="Spades | 6.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%207.jpg" alt="Spades | 7.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%208.jpg" alt="Spades | 8.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%209.jpg" alt="Spades | 9.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%2010.jpg" alt="Spades | 10.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20J.jpg" alt="Spades | J.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20Q.jpg" alt="Spades | Q.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
  <img src="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/Spades%20|%20K.jpg" alt="Spades | K.jpg" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">
<br>
</div>

