# Disboard Scraper

This script will scrape all the servers on a particular tag and show various statistics. It can also output the data into a file. This script should be used in moderation to prevent being detected as a DOS attack.

These are the features currently available:

- Display online member counts.
- Display tags of each server.
- Show most popular tags for each tag position.
- Output server data as a file

## Usage

#### Requirements:
- Make sure to download the latest [Python (>= 3.8.x)](https://www.python.org/downloads/).
- Then install [pipenv](https://pypi.org/project/pipenv/).
- Ensure you have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed

Clone this repository:
```
git clone https://github.com/DiscordFederation/DisboardScraper.git
```

Then enter a pipenv environment using this command:

```
pipenv shell
```

Next install the requirements:

```
pipenv install
```

Finally edit the newly created `config.toml` file and run the script.

```
python app.py
```

## Configuration Options

You should make a copy of the included `config.example.toml` file and save it as `config.toml` with your own settings for it to be picked up by the script.

|  Configuration        |  Type            | Description                                                                                                                               |
|-----------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `tag`                 | `str`            | This is the tag you want to analyze for servers.                                                                                          |
| `pages`               | `int`            | This configures how many pages for a tag you want to scrape.                                                                              |
| `top_positional_tags` | `true`,  `false` | This displays the most popular tags for each tag's position.                                                                              |
| `tpt_limit`           | `int`            | Limits the number of tags shows for all tag positions. This only works if `top_positional_tags` is enabled.                               |
| `csv`                 | `true`, `false`  | When enabled will output all scraped data into a CSV file. This should make further analysis easier.                                      |
| `debug`               | `true`, `false`  | While set to `true` the script will display more output onto the console for debugging purposes. This will also disable the progress bar. |
