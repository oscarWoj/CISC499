# CISC499
Independent research project on the contents of a dark web cyber blackhat forum. 
We utilized the BERTopic neural network to parse and analyze conversations. After successfully trianing the model on 9,500,000 posts, we were able to deeply understand 10 years of topics discussed by participants.

We made further progress by developing techniques to isolating specific conversations, and identify bad actors in hopes of protecting against cyber attacks.

Contents:

- simple_hw_check - For solving dependencies...if this file runs on your server, the bertopic file should also.

- csv_parse.ipynb - Processing raw data into the proper input for BERTopic. Using pandas dataframes and simple tecniques we were able to reduce the charachter count down 22%

- onlinemodel_1000_3_3_10decay.ipynb - The training output from our final chosen model.

- bertopic_playground.ipynb - Loading the final model for comparizons and data visualizations.

- v4_bertopic_playground.ipynb - The final model with unimportant topics reduced to isolate "potential" harmful conversations.
