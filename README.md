# Tweets-classification
Scrapy is a tweet classification application that mines data from user profiles. The data mined from user profiles is used to predict the user that is most likely to post a particular tweet. Publicly available tweets are extracted, transformed and trained to build this application.
The developers of this application would not be held responsible for any misuse of the application as it was created solely for educational purposes.
(Please read the license for more information)


## PARTICIPANTS

The data used to build this application is gotten from Twitter. This information is generally available to the public and it in no way violates the users data rights. However, consent was still obtained from the users.
The following users consented to the use of their data:
1. Sanusi Ismaila
2. Robert Thas
3. Mercy Markus
4. Osamudiamen
5. Pablo Okwukogu
6. Segun
7. Ifeanyi Morah
8. Adinoyi Sadiq
9. Umar
10. Aliyu
11. Joy Victor
12. Mubaraq Sanusi
13. Kwatmi Tyron
14. Ane Itodo
15. Oluwasanmi Onemano
16. Abijah Johnnie
17. Segun Babalola
18. Tobi
19. Gabriel Arowosegbo
20. Abdulhakeem


# How to
Create a twitter app and generate tokens on [twitter] (https://developer.twitter.com/en/apps) to replace the dummies in the code (fetch.py)

run the index.py file to execute the tweets classification model

the fetch.py file contains the code for fetching users' tweets
# Steps taken
Fetch and save tweets from twitter

Load the tweets to the program

Preprocess the data

Vectorize tweets (CountVectorizer)

Transform the tweets (TFIDFTransformer)

Fit and Predict usig Multinomial Naive Bayes model

Evaluate The model
