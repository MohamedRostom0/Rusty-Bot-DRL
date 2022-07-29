# Rusty-Bot-DRL 🤖
A Deep Reinforcement Learning based chatbot that answers students FAQs related to their university.

## General Information
  - Using a DQN agent to maintain the Dialogue Policy of the Dialogue Manager (DM) module of the Dialogue system.
  - The DM can be used in a Modular pipeline or for End-to-End training and testing.
  - NLU used is powered by Rasa, and can be found here: https://github.com/MohamedRostom0/RustyBot-NLU
  
## Acknowledgements
  - The repo done by @github.com/maxbren is just amazing and easy to follow up with, especially with his 5 medium articles where he explains every piece of code. 
  - The code I implemented follows the approach offered in this paper https://arxiv.org/pdf/1703.01008.pdf.
  
## Project overview
  ![alt text](https://github.com/MohamedRostom0/Rusty-Bot-DRL/blob/main/RustyBot2(NL).png)
  - This repo includes the Dialogue Manager module (Dialogue State Tracker "DST", Dialogue Policy).
  - The Train.py or Test.py work as follows;
    - Take text input from user from CLI.
    - Send the text input in an HTTP request to Rasa NLU API that runs either on a local port or on a deployment environment.
    - The response from Rasa is the {user intent, extracted entities}, and we convert it into a Semantic Frame (Which is basically an object containing           these info following a convention).
    - Then the Semantic frame is passed to the DST module to get a unique state representation.
    - The state rep. then passes to the DQN agent that applies an Epsilon-greedy dialogue policy; Meaning that the DQN agen either chooses a random action        to perform, or just asks the Deep Neural Network to predict the best possible action.
    - Finally, the action passes to the NLG to get it represented in Natural Language(English). However, in our repo, we didn't implement the NLG, we just      mapped each action directly to an English representation (Nothing fancy 🤷‍♂️).

## How to run:
  ### Install dependencies
  `pip install requirements.txt`
  
  ### Set up constants.json file to be able to train/test.
  - Train a model
    - To be added
  
  - Test already trained model
    - `load_weights_file_path` Set this to the path of the trained model.
    - `usersim: false` To make the user type input by himself/herself/themselves in CLI.
    - `num_ep_run`: specifies number of episodes(dialogues) you want it to run for.
    - `use_rasa`: Works when you are running Rasa NLU on another Port, and you want to test having dialogues in English.
    - To run test: `python "src/test.py"`
  

## How to modify the repository for other dialogue examples?
  - To be added
  
## If you have any questions, feel free to contact me via:
  - Email 📧: Mohamedrostom62@gmail.com

