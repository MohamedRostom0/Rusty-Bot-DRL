# Rusty-Bot-DRL
A Deep Reinforcement Learning based chatbot that answers students FAQs related to their university.

## General Information
  - Using a DQN agent to maintain the Dialogue Policy of the Dialogue Manager (DM) module of the Dialogue system.
  - The DM can be used in a Modular pipeline or for End-to-End training and testing.
  - NLU used is powered by Rasa, and can be found here: https://github.com/MohamedRostom0/RustyBot-NLU
  
## Project overview
  ![alt text](https://github.com/MohamedRostom0/Rusty-Bot-DRL/blob/main/RustyBot2(NL).png)
  - This repo includes the Dialogue Manager module (Dialogue State Tracker "DST", Dialogue Policy).
  - The Train.py or Test.py work as follows;
    - Take text input from user from CLI.
    - Send the text input in an HTTP request to Rasa NLU API that runs either on a local port or on a deployment environment.
    - The response from Rasa is the {user intent, extracted entities}, and we convert it into a Semantic Frame (Which is basically an object containing           these info following a convention).
    - Then the Semantic frame is passed to the DST module to get a unique state representation.
    - The state rep. then passes to the DQN agent that applies an Epsilon-greedy dialogue policy; Meaning that the DQN agen either chooses a random action        to perform, or just asks the Deep Neural Network to predict the best possible action.
    - Finally, the action passes to the NLG to get it represented in Natural Language(English). However, in our repo, we didn't implement the NLG, we just      mapped each action directly to an English representation (Nothing fancy).

## How to run:
  - To be added

## How to train the chatbot to learn your custom intents?
  - To be added
