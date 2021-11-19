# Modified Disboard Scraper

This is a modified version of the DisboardScraper repository by daegontaven / Discord Federation.

It scrapes servers from Disboard based on tags and can output the data as a CSV file. This fork features the following adjustments from the original:

- It collects *server descriptions* in addition to server names, online members, and tags.
- HTML elements are cleaned from server descriptions.
- It includes a sleep function to allow scraping in higher volumes without getting rate limited.

Features available from the original scraper:

- Displaying online member counts.
- Displaying tags of each server.
- Showing most popular tags for each tag position.
- Outputing server data as a CSV file.

This repository is an updated version of the script used in our article on hate networks on Discord, available here: [LINK]

If you would like a more in-depth tutorial on how to install and use the scraper, see my blog post here: [LINK.]

## Setting Up the Environment

- Make sure to download the latest [Python (>= 3.8.x)](https://www.python.org/downloads/).
- Then install [PyCharm](https://www.jetbrains.com/pycharm/) (the Community version is fine!).
- Ensure you have [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed. If you are unfamiliar with Git, you may also install [GitHub Desktop](https://desktop.github.com/) as a user-friendly way to use Git.

Clone this repository:

```
git clone https://github.com/IceBerge421/Modified-Disboard-Scraper.git
```

Open the new folder you just cloned in PyCharm.

In PyCharm, go to File > Settings > [Project Name] > Python Interpreter."

Select your version of Python as the interpeter. PyCharm will then create a virtual environment. Now, in the Interpreter Menu, click the '+' symbol to add packages. Add the following packages:

- `cloudscraper`
- `pandas`
- `discord.py`
- `toml`
- `beautifulsoup4`
- `schema`
- `tqdm`
- `lxml`

## Running the Scraper

Duplicate the file `config.example.toml` and rename it to `config.toml`. 
(Note: If you run the project and do not see any output, you likely forgot to rename the new config file.)

Edit the newly the newly created `config.toml` file by setting any of the Configuration Options (see below).

When you are ready, you can run the script clicking Run > and selecting `App` or run it from the terminal:

```
python app.py
```
The scraper will output to the terminal, and a new file titled `[tag-name].csv` will be newly created in the project folder.

## Configuration Options

### Scraper Configuration

You should make a copy of the included `config.example.toml` file and save it as `config.toml` with your own settings for it to be picked up by the script.

|  Configuration        |  Type            | Description                                                                                                                               |
|-----------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `tag`                 | `str`            | This is the tag you want to scrape  servers.                                                                                          |
| `pages`               | `int`            | This configures how many pages for a tag you want to scrape.                                                                              |
| `top_positional_tags` | `true`,  `false` | This displays the most popular tags for each tag's position.                                                                              |
| `tpt_limit`           | `int`            | Limits the number of tags shows for all tag positions. This only works if `top_positional_tags` is enabled.                               |
| `csv`                 | `true`, `false`  | When enabled will output all scraped data into a CSV file. This should make further analysis easier.                                      |
| `debug`               | `true`, `false`  | While set to `true` the script will display more output onto the console for debugging purposes. This will also disable the progress bar. |
### Scraper Configuration
