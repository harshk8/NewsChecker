This is a test application given by one of the reputted company of India, and I cleared their one of the test this repo is the example of it.

Description: This is a basic news Fetcher application for fetch and check the authenticity of news.

#Any user can search on this platform; login is mandatory for users to search.

#If a user signin account they have option to add news as preference so next time whenever they will come to platform they will get related new to their selected preferences.


#Installation Procedure:

1. Take clone of application: 
	// git clone https://github.com/harshk8/NewsChecker.git

2. Create virtual environment
	// virtualenv env

3. Install dependencies, inside the root folder at News/Checker run below given command:
	// pip install -r requirements.txt

4. Now run migrations:
	// python manage.py migrate

5. Now run collect static:
	// python manage.py collectstatic

6. After that load all the predefined Categories: 
	// python manage.py loaddata news/fixtures/news_category.json 

7. Now run last step to start server:
	// python manage.py runserver


#Application Features
1. User can search on the platform we have several options inside the search feature:
   (A) Query 
   (B) FromDate
   (C) ToDate
   (D) Category

2. We are fetching the news from "https://newsapi.org/" right now, we also have option to add more APIs in "NewsSource" model, with its APIKEY if any.

3. User can signUp and add or remove news category to their own Preference list, user can also check their own prefernce on My Preference page.

4. Whenver anyone search on the platform and any new news comes in our system contact we will store that news and will notify those users who had selected the category from which new news generated.

5. We are listing out new Notification count at the right-top corner of the page, where New Notification counts are listed. When click on button it will redirect to Notification Page which again contain an * in front of the news Number, so user can easily identify new news.


#We have few plannings which I not implemented due to lack of time
	#Fetch News function process should run in background using celery
	#Signal should be use on behalf of direct wirting code inside the function.
	#A cronjob can be run in a periodic time so latest news can be generate fast.
