# NBA Stats Database

## Plan

1. Data collection 
	- Selenium - live data from dyanic websites.
	- Beautiful soap/scrapy - historical static data.
	- Live data - websocket connections or periodic updates.  
&nbsp;    

2. Backend API
	- Django (Python): A more comprehensive framework that includes an ORM and admin panel out-of-the-box.
	- Django REST Framework
&nbsp;   

3. Backend DB
	-Initially SQL lite, but it quickly met its limitations when trying to scrape data for 30 teams at once. It could not handle all the simulataneous connections.
	- PostgreSQL is the new DB. 

4. Frontend
	- React/Redux
	- D3.js
	- Chart.js
	- Highcharts
	- Websockets or Server-Sent Events
&nbsp;  

1. Deployment



