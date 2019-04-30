This is a simple python script to scrape the codejam scoreboard. Since I did this as a personal project, I did not really bother to fine-tune its usability. I will do so once I have more free time.

Requirements:
1. Internet connection
2. Python 2.7

To run the script:

1. Go to the codejam page and access one of the past rounds/currently ongoing round.
2. You should see a url like this in the address bar: `https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706`
3. Copy the part of the form `0000000000051706`
4. Edit the variable `url` and replace the corresponding part of the url.
5. Run the script in terminal/command prompt by issuing the command `python codejam_scraper.py`
6. Now, you will see the scoreboard printed in the console.

Notes:
1. The script prints only four fields from the scoreboard: rank, country, score and name.
2. The script prints usernames that are in the top 1500. You can modify the bounds of the `xrange` function to change this.
3. The script terminates after printing the scoreboard once. To make the script loop infinitely, just comment out the break statement at the end of the script.
