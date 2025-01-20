---
title: Everyone Makes a Wordle Bot
hide_title: true
---
<style>
/* Import Wordle font */
@import url('https://fonts.googleapis.com/css2?family=Lucky+Guy&display=swap');

/* Body and main styling */
body {
  margin: 0;
  font-family: "Lucky Guy", sans-serif; /* Use Wordle's font */
  background-color: #f5f5f5;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 100vh;
  overflow: hidden;
  text-align: center;
  padding: 10px;
}

.wordle-container {
  display: flex;
  flex-direction: column;
  gap: 3px;
  justify-content: flex-start;  /* Left justify words */
  align-items: flex-start; /* Align words to the left */
}

/* Styling for individual tiles */
.wordle-tile {
  display: inline-block;
  width: 50px; /* 2/3 of the original size */
  height: 50px;
  margin: 1px;
  font-size: 28px; /* 2/3 of the original size */
  font-weight: bolder; /* Thicker text */
  line-height: 50px; /* Center text vertically */
  text-transform: uppercase;
  background-color: #787c7e; /* Start with gray color (dark gray) */
  color: white;
  opacity: 0; /* Initially hide the tile */
  transform: rotateX(90deg); /* Flip effect */
  animation: flipTile 0.6s ease-out forwards; /* Tile flip animation */
  text-align: center; /* Center text horizontally */
}

.wordle-tile .letter {
  opacity: 0; /* Letters are hidden initially */
  transform: rotateX(90deg); /* Letter is hidden */
  animation: flipLetter 0.6s ease-out forwards; /* Letter flip animation */
  animation-delay: 0s; /* No delay for the letter animation */
}

/* Animation for tile flipping effect */
@keyframes flipTile {
  0% {
    opacity: 0; /* Letters hidden at start */
    transform: rotateX(90deg);
  }
  50% {
    opacity: 1; /* Keep opacity to show tile */
    transform: rotateX(180deg); /* Flip halfway */
  }
  100% {
    opacity: 1; /* Tile fully visible after flip */
    transform: rotateX(0deg); /* Flip to normal position */
  }
}

/* Animation for letter flipping effect */
@keyframes flipLetter {
  0% {
    opacity: 0; /* Letters hidden at start */
    transform: rotateX(90deg); /* Letter hidden */
  }
  100% {
    opacity: 1; /* Letters visible immediately after flip */
    transform: rotateX(0deg); /* Letter flips to normal position */
  }
}

/* Wordle-like colors */
.wordle-tile.green { background-color: #6aaa64; }
.wordle-tile.yellow { background-color: #c9b458; }
.wordle-tile.gray { background-color: #787c7e; }

/* Sequential animation for each word row */
.wordle-word {
  display: flex;
  gap: 3px;
  justify-content: flex-start;
  opacity: 0;
  animation: wordAnimation 1s forwards;
}

@keyframes wordAnimation {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

/* Small stagger for each word to start one after another */
.wordle-word:nth-child(1) { animation-delay: 0s; } /* "everyone" */
.wordle-word:nth-child(2) { animation-delay: 0.05s; } /* "makes" */
.wordle-word:nth-child(3) { animation-delay: 0.1s; } /* "a" */
.wordle-word:nth-child(4) { animation-delay: 0.15s; } /* "wordle" */
.wordle-word:nth-child(5) { animation-delay: 0.2s; } /* "bot" */
</style>

<div class="wordle-container">
  <!-- "Everyone" Row -->
  <div class="wordle-word">
    <div class="wordle-tile green" style="animation-delay: 0s;">
      <div class="letter">E</div>
    </div>
    <div class="wordle-tile green" style="animation-delay: 0.2s;">
      <div class="letter">V</div>
    </div>
    <div class="wordle-tile gray" style="animation-delay: 0.4s;">
      <div class="letter">E</div>
    </div>
    <div class="wordle-tile green" style="animation-delay: 0.6s;">
      <div class="letter">R</div>
    </div>
    <div class="wordle-tile yellow" style="animation-delay: 0.8s;">
      <div class="letter">Y</div>
    </div>
    <div class="wordle-tile gray" style="animation-delay: 1s;">
      <div class="letter">O</div>
    </div>
    <div class="wordle-tile gray" style="animation-delay: 1.2s;">
      <div class="letter">N</div>
    </div>
    <div class="wordle-tile yellow" style="animation-delay: 1.4s;">
      <div class="letter">E</div>
    </div>
  </div>

  <!-- "Makes" Row -->
  <div class="wordle-word">
    <div class="wordle-tile gray" style="animation-delay: 0.05s;">
      <div class="letter">M</div>
    </div>
    <div class="wordle-tile yellow" style="animation-delay: 0.25s;">
      <div class="letter">A</div>
    </div>
    <div class="wordle-tile yellow" style="animation-delay: 0.45s;">
      <div class="letter">K</div>
    </div>
    <div class="wordle-tile green" style="animation-delay: 0.65s;">
      <div class="letter">E</div>
    </div>
    <div class="wordle-tile yellow" style="animation-delay: 0.85s;">
      <div class="letter">S</div>
    </div>
  </div>

  <!-- "A" Row -->
  <div class="wordle-word">
    <div class="wordle-tile green" style="animation-delay: 0.1s;">
      <div class="letter">A</div>
    </div>
  </div>

  <!-- "Wordle" Row -->
  <div class="wordle-word">
    <div class="wordle-tile yellow" style="animation-delay: 0.15s;">
      <div class="letter">W</div>
    </div>
    <div class="wordle-tile yellow" style="animation-delay: 0.35s;">
      <div class="letter">O</div>
    </div>
    <div class="wordle-tile gray" style="animation-delay: 0.55s;">
      <div class="letter">R</div>
    </div>
    <div class="wordle-tile green" style="animation-delay: 0.75s;">
      <div class="letter">D</div>
    </div>
    <div class="wordle-tile yellow" style="animation-delay: 0.95s;">
      <div class="letter">L</div>
    </div>
    <div class="wordle-tile gray" style="animation-delay: 1.15s;">
      <div class="letter">E</div>
    </div>
  </div>

  <!-- "Bot" Row -->
  <div class="wordle-word">
    <div class="wordle-tile green" style="animation-delay: 0.2s;">
      <div class="letter">B</div>
    </div>
    <div class="wordle-tile yellow" style="animation-delay: 0.4s;">
      <div class="letter">O</div>
    </div>
    <div class="wordle-tile gray" style="animation-delay: 0.6s;">
      <div class="letter">T</div>
    </div>
  </div>
</div>
