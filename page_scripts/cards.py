import os
from urllib.parse import unquote


class Deck:
    def __init__(self, folder_path, suit_order=None, rank_order=None):
        self.folder_path = folder_path
        # Default suit and rank order if not provided
        self.suit_order = suit_order or ['diamonds', 'clubs', 'hearts', 'spades']
        #self.rank_order = rank_order or ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        #self.rank_order = rank_order or ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        self.rank_order = rank_order or ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []

    def load_images(self):
        """
        Load the valid images from the specified folder and sort them.
        """
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError(f"Folder '{self.folder_path}' does not exist.")
        
        image_files = [
            f for f in os.listdir(self.folder_path) 
            if f.lower().endswith('.jpg')
        ]

        if not image_files:
            raise FileNotFoundError(f"No image files found in folder '{self.folder_path}'.")

        self.cards = [
            f for f in image_files 
            if self._is_valid_card(f)
        ]

        if not self.cards:
            raise ValueError("No valid card images found.")
        
        # Sort the cards by suit and rank order
        self.cards = self._sort_cards(self.cards)

    def _is_valid_card(self, file_name):
        """
        Check if the card's file name is valid.
        """
        suit, rank = self._extract_suit_and_rank(file_name)
        return suit in self.suit_order and rank in self.rank_order

    def _extract_suit_and_rank(self, file_name):
        """
        Extract suit and rank from the image filename.
        """
        # Decode URL-encoded characters
        decoded_name = unquote(file_name.lower().replace('.jpg', ''))
        parts = decoded_name.split('|')  # Split by the literal '|'
        if len(parts) != 2:
            return None, None
        suit, rank = parts[0].strip(), parts[1].strip().upper()
        return suit, rank

    def _sort_cards(self, cards):
        """
        Sort the cards based on suit and rank extracted from the filenames.
        """
        def sort_key(card_name):
            # Extract suit and rank from the filename
            suit, rank = self._extract_suit_and_rank(card_name)
            # Return tuple for sorting by suit and rank
            return (self.suit_order.index(suit), self.rank_order.index(rank))

        # Sort the cards based on the extracted suit and rank
        return sorted(cards, key=sort_key)

    def shuffle(self, times=1):
        """
        Perform perfect shuffles (riffle shuffles) multiple times.
        """
        for _ in range(times):
            self.cards = self._riffle_shuffle(self.cards)

    def _riffle_shuffle(self, deck):
        """
        Perform a perfect shuffle (riffle shuffle).
        """
        # Split the deck into two halves
        half_size = len(deck) // 2
        first_half = deck[:half_size]
        second_half = deck[half_size:]
        
        # Interleave the two halves to create the shuffled deck
        shuffled_deck = []
        for i in range(half_size):
            shuffled_deck.append(first_half[i])
            shuffled_deck.append(second_half[i])

        # If the deck has an odd number of cards, add the last card from the second half
        if len(deck) % 2 != 0:
            shuffled_deck.append(second_half[-1])

        return shuffled_deck

    def _write_card_images(self, md_file, github_raw_base):
        """
        Write card images in a 13x4 grid layout in the markdown file.
        """
        md_file.write('<div style="display: flex; flex-wrap: wrap; justify-content: space-between; width: 100%;">\n')
        for i, image in enumerate(self.cards):
            image_url = github_raw_base + image.replace(" ", "%20")
            md_file.write(f'  <img src="{image_url}" alt="{image}" width="6.9%" style="margin: 1px; border: 1px solid #ddd; border-radius: 5px;">\n')
            # Add a line break every 13 cards to create a 13x4 grid
            if (i + 1) % 13 == 0:
                md_file.write('<br>\n')
        md_file.write('</div>\n\n')

    def generate_markdown(self, output_file, github_raw_base):
        """
        Generate a markdown file with shuffled card images.
        """
        with open(output_file, "w") as md_file:
            md_file.write("# Examining the 'Perfect' Shuffle\n\n")
            md_file.write(" If you shuffle a deck of cards *perfectly*, will the deck return to the start order? How many shuffles would that take?")
            md_file.write("\n\n Let's find out.\n\n")
            md_file.write("## Defining a Perfect Shuffle\n\n")
            md_file.write("We will define a 'perfect' shuffle as a *Riffle Shuffle.*\n\n")
            md_file.write("To perform a classic riffle shuffle:\n\n")
            md_file.write("1. Divide the deck into two equal halves\n")
            md_file.write("2. Combine the decks, allowing the cards to interlace one at a time\n")
            md_file.write("3. Square up the deck and repeat\n\n")
            md_file.write("# Let's get shuffling and find out! \n\n")

            # Display the sorted deck before shuffling
            md_file.write("## Before Shuffling\n")
            self._write_card_images(md_file, github_raw_base)

            # Perform and display 8 rounds of shuffling
            for shuffle_round in range(1, 9):
                self.shuffle(1)  # Shuffle once per round
                md_file.write(f"## After Shuffle {shuffle_round}\n")
                if shuffle_round == 8:
                    md_file.write("We're back!\n\n")
                self._write_card_images(md_file, github_raw_base)


def generate_deck_and_markdown(folder_path, output_file, github_raw_base):
    """
    High-level function to generate a deck and markdown file.
    """
    deck = Deck(folder_path)
    deck.load_images()
    deck.generate_markdown(output_file, github_raw_base)

    print(f"Markdown file '{output_file}' created successfully!")


# Example usage
generate_deck_and_markdown(
    folder_path="media/card_images", 
    output_file="pages/examining_the_perfect_shuffle.md", 
    github_raw_base="https://raw.githubusercontent.com/davidsrrose/davidsrrose/refs/heads/dev/media/card_images/"
)


