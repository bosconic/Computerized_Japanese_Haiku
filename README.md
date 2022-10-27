# Computerized Japanese Haiku

1. By: Nicholas Bosco
2. Topic: Computerized Japanese haiku using Python

# Background Information

This idea for this particular idea comes from an exhibition called "Cybernetic Serendipity", where the purpose of the exhibition was to explore the connection between control, computers and humans. Drawing on the concept of Cybernetics, many people from across the globe in different professions show the possible capabilities people and machines can achieve when working together. I had found this particular exhibition by researching another object that was displayed within the exhibit, I thought I can try my hand at re-creating one of the art pieces that tries to reimagine how we view creativity and since poems/haikus are such a human thing, expressing feeling, I am curious to see how well a computer can do. I would like to point out that this is a modified of the actual program that can be found on page 54 of the catalogue and would require me to provide the computer instructions through pyuthon to achive the goal of a Computerized Japanese Haiku. This project was first attempted with the programming language TRAC and were produced by Margaret Masterman and Robin McKinnon Wood [^1][^2].

[^1]: Reichradt, J. (1968). Cybernetic serendipity: The computer and the arts: A studio international special issuee. Studio International. 
[^2]: Reichradt, J. (1968). In Cybernetic serendipity: The computer and the arts: A studio international special issuee (p. 54). Studio International. 


## From The Catalogue Page

This is the image and inspiration for the project
![computerized_haiku_template](https://user-images.githubusercontent.com/98721827/198149317-4b0e84d9-5083-44e1-9e85-2dfdf31d7089.png)


Here are the words from the catelogue that describe this program:

> These are examples, produced by on-line man-machine interaction at the Cambridge Language Research Unit, of one use of a
computer for producing poetry. The programme is written in the TRAC language. The programme is a frame with 'slots' in which the operator types words. In '1 Poem' and '2 Poem', the operator chooses his words as he wises. In the two '3 Poem' exhibits his choice constrained by the lists and arrow directions given in the thesaurus. By using these arrows, a semantic schema of the haiku can be built up (see diagram) which shows that the semantic centre of the poem - with five arrows going to it and going from it - is situated at slot No.5. These poems were produced by Margaret Masterman and Robin McKinnon Wood[^2].

# Program Overview

## Inputs
Given this is my first time interacting with python to generate onto here, the program is a bit involved with the use of 
`Import Random` as the primary way to randomize the computer generated haiku's. Within the code itself you will find an initial if statement asking the user if they would like to participate. The proceeding user inputs correspont to the individual slots, giving the user the chance to choose a particular word from the individual slots in order to generate the collaborative haiku. A note should be made that the user can only control the input of the first 6 slots of the haiku, as slot 7, slot 8 and slot 9 will always be computer generated.

## Processing
The __Blackbox__ portion of the computer is that randomization feature I had mentioned earlier, The user will not know the outputs for each randomized slot until the very end of the program. However I included the `if else` statements with individual print statements to give the user some feedback on whether or not their guess by chance was the same as the computer generated output.

## Output
Before the user has the chance to interact with the program, I had attatched the same photo you see here within the program's readMe as a way for new readers to get a gist of the inspriation of this python re-creation. In order to get the image of the catalogue page to appear onto the program as it runs, please refer to this link on the [pillow library](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html) [^3]. All of the user inputs, the user is presented with are two different Haiku's one being soley computer generated (generated without the user's input) and strictly given after the randomization of the random library. The other Haiku is the collaborative Haiku, that was 2/3 user input and 1/3 computer input.
[^3]: Tutorial. Tutorial - Pillow (PIL Fork) 9.2.0 documentation. (n.d.). from https://pillow.readthedocs.io/en/stable/handbook/tutorial.html 

# Final Remarks
If you have made it this far in reading the readMe section, I am very thankful and grateful for your vested interest for this particular python program. If you are ever curious to check out even more projects for inspiration I encourage you to check out the pdf within this repository. There are many other cool fascinating art/computer combinations that are great ways for added practice when on your python programming journey.
