# Etsy_Plants_Shops

[Dashboard Link](https://public.tableau.com/views/EtsyPlantShopData/NurseryRx?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link)

[Google Slides Link](https://docs.google.com/presentation/d/1-ezjEoKWYN_8X0zNdRwadQ4JRfgeOBFjpD5VYN0eoMk/edit?usp=sharing)

## Overview

The goal of this project to develop a competitive analysis between Etsy plant shops. I utilized Etsy's API to extract data from competing plant shops across the platform. I then used that data to understand our company's performance compared to others. 

- Technologies Used
    - Postman
    - Etsy API 
    - Python
    - Crontab
    - PostgreSQL
    - Tableau

## Results

- Etsy API
    - Utilized Etsy's API documentation to gain access to their API. I was in contact with Etsy's Development team to help with Token issues during authentication. I used Postman to help configure the API and verify that the data was what I was looking for. Postman then helped me convert the API request to work in Python. 
- Python
    - Python was used to gain access to the JSON data from the API. The data was then parsed and pushed to my SQL server. I also had to extract the data to a CSV because Tableau public will not connect to a SQL Server.
- Crontab
    - Crontab is used to schedule when the python script runs. I set it run at the top and bottom of every hour. This will help give a clearer understanding of when sales are highest on the platform. 
- PostgreSQL
    - PostgreSQL was installed on a Linux server to collect the API data from the Python script. 
- Tableau
    - Data visualization dashboard. I was not able to connect this to the SQL database because I only have Tableau Public, so I used a CSV instead. 
