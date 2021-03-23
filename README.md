# Music Grapher
Generates graphs on users music listening habits.

This is meant for processing and analysing the data from my [cmus-music-monitor](https://github.com/benarmstead/cmus-music-monitor) shell script.

However, this program will work on any CSV formatted:

`<Title>, <Artist>,	<Album>, <Genre>, <Song Length>, <Track number>,	<Year>,	<Play 
date>, <Play time>, <Volume>`

(Its also very easy to modify it to take data from another format if you know python).


## Future goals

- Move to a database format rather than CSV (need to convert [cmus-music-monitor](https://github.com/benarmstead/cmus-music-monitor) to this first though.)
- Generate predicted usage and spot patterns with machine learning.
- Implement more features such as different ways of viewing graphs etc.

## Installation

`git clone https://github.com/benarmstead/music-grapher`

`cd music-grapher/src`

## Running

In the `main.py` file in the `get_all_data()` function. 

Change the `your_path = ""` vairable to the path of your CSV

`python3 main.py`


## Image Examples

### Start

![Start](https://raw.githubusercontent.com/benarmstead/music-grapher/main/README_images/start.webp)


### Menu

![Menu](https://raw.githubusercontent.com/benarmstead/music-grapher/main/README_images/menu.webp)

### Most Played Songs

![Most Played Songs](https://raw.githubusercontent.com/benarmstead/music-grapher/main/README_images/most_played_songs-c.webp)

### Most Played Artists

![Most Played Artists](https://raw.githubusercontent.com/benarmstead/music-grapher/main/README_images/most-played-artists-c.webp)

### Avg songs p/day

![Avg songs p/day](https://raw.githubusercontent.com/benarmstead/music-grapher/main/README_images/avg-songs-p-day.webp)

### Most Played Days

![Most Played Days](https://raw.githubusercontent.com/benarmstead/music-grapher/main/README_images/most-played-days.webp)

### Unique songs played

![Unique songs played](https://raw.githubusercontent.com/benarmstead/music-grapher/main/README_images/unique-songs-p-day.webp)
