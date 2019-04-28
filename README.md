# Intro to reinforcement learning

### Preliminaries: playing frozen lake

To get you started with RL, play for a while with the Frozen Lake puzzle from the [OpenAI gym](https://gym.openai.com/envs/FrozenLake-v0/). To run the code, you will need to install the OpenAI gym by running:

`pip3 install --user gym`

if you are under pythonanywhere, or

`sudo pip3 install gym`

if you are under your own environment.

A Q-table implementation that tackles the puzzle can be found [here](https://github.com/simoninithomas/Deep_reinforcement_learning_Course/blob/master/Q%20learning/Q%20Learning%20with%20FrozenLake.ipynb) as a Jupyter notebook. In this repo, you will also find a version of the same code that you can simply run from the terminal:

`python3 frozen_lake.py`

Understand the environment and the steps taken by the algorithm. Try to modify the parameters to see their influence on the result.


### Learning politeness

Now, let's implement our own RL problem. It is a much simpler problem than the frozen lake but it will make things more transparent.

An Italian café has the following sign above the counter:

```
un caffè / a coffee: 3 EUR
buongiorno, un caffè / hello, a coffee: 2 EUR
bungiorno, un caffè per favore / hello, a coffee please: 1 EUR
```

Let's design an RL agent that will learn some obvious politeness rules.

We're going to make the environment a little more challenging in the following ways:

* When we ask for our coffee using the most polite form, things sometimes go wrong. The café owner is so busy that she doesn't wait to hear the end of the sentence, leading her to think that we simply said *Buongiorno, un caffè!* This displeases her.

* Sometimes, the café owner is in a really good mood, and even though we were not that polite (we only said *Buongiorno, un caffè!*, or perhaps *Un caffè, per favore!*) she still makes us pay 1 EUR only.


### Let's write down the environment

This is a pen and paper exercise. Try to write down the environment: which states we have, which actions we can take, and which rewards we will be given. 

NB: all rewards are 0 apart from the ones we get at the end of the utterance, which match the price of the coffee: -1 for 1 EUR, -2 for 2 EUR, -3 for 3 EUR.

NB2: if you get stuck, have a look at the *states.png* file in this repo!


### Run the code

Run the code:

`python3 caffe.py`

First, have a look at the produced Q-table. Can you read it? Do you understand what it is saying? And what is happening at test time?

Run the code several times. You should find that witht the given parameters, the system is not always as polite as it could be. Why is that?



### Change the environment

What if we added an extra state? Sometimes, the café owner is so pleased that someone was polite to her that she gives them the coffee for free, and adds a big smile to it. Reward +1.

Try to change the code to add that extra state (you can choose whichever transition probabilities you prefer) and see how things change.
