
> ![image](https://user-images.githubusercontent.com/69976409/195754514-06dcba6c-7ea4-42da-a3d8-8f334194c1f8.png)
# Blackjack Project
Approach to Blackjack by Jack Johnson & Kelsey Peltz
### [Website Link](https://kelseypeltz.github.io/blackjackproject.github.io/)
<details open="open">
<summary>Table of Contents</summary>

- [The Game](#the-game)
- [Project Goals](#project-goals)
  - [Collaboration Plan](#collaboration-plan)
- [ETL](#etl)
   
   
</details>

---   
## Background
This project aims to explore how blackjack rule variation affects the house's edge when a player is using basic strategy. The house edge is the percentage a casino will win over the player. In other words, the house edge is the ratio of the players' average loss to their initial bets. In 1962 Edward Thorp created a basic strategy for blackjack that produces an almost even game (house edge of 0.56%) when played with general casino rules. In a game with general casino rules, it is assumed that the house uses 6 decks and the following rules: double on any first 2 cards, no double after splitting, resplit all pairs except Aces, dealer stands of soft 17, and no surrender. The problem we found was when the rules vary from the general casino rules, the house edge changes, giving a naive player using basic strategy the false assumption that it is an almost even game. In this project, we attempt to model how rule variations affect the house edge to allow players to estimate their true disadvantage (or advantage) when using basic strategy. 

## The Game
Blackjack is the most popular casino banking game in the world. In blackjack, there is one deck of 52 cards, everyone plays against the dealer, players place bets, and each player is dealt two cards at a time (including the dealer). The players know one of the dealer's cards, while the other remains unknown until the round is done. After everyone is dealt, players can decide if they want to "hit," meaning they'd be dealt more cards (one at a time) to get a sum closest to 21 without "busting" (going over 21). If a player is satisfied with their hand, they do not "hit." The goal is to have a sum greater than the dealers.1 Players and dealers often use card counting as away to become an advantaged player. Card counting is a mathematical strategy used in blackjack that helps determine one’s probable advantage or disadvantage of the next dealt card. 

## Basic Strategy 

The goal of this project is to determine the best mathematical strategy to become an advantaged player in blackjack. 

## Collaboration Plan 

We have set up a google colab to work on our code together. Since we are partnering this project with our Capstone project, we plan on meeting on a weekly to bi-weekly schedule our faculty mentor. We plan on dividing work by doing independent research and coding and discussing it during our scheduled meetings and throughout the week as needed. 

## ETL 
### (Extract, Transform, and Load)
Currently we are coding a blackjack simulation that will run the game thousands of times using different strategies since the data source we had been hoping to use was too large for github. We are hoping to somehow upload the data from [here](https://www.kaggle.com/datasets/mojocolors/900000-hands-of-blackjack-results) to get more insights the average player. In the meantime, we found a smaller dataset to begin analyzing. We also compiled  to help us understand blackjack basic strategy (a.k.a. the book) and the "typical" human strategy so we can compare those with the counting card strategies.  


