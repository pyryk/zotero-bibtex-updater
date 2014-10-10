# Zotero Bibtex Updater
Quick'n'dirty tool for updating your bibtex file from Zotero

## Usage
1. Generate an API key for this app in [https://www.zotero.org/settings/keys](https://www.zotero.org/settings/keys). The page also contains your userID for API calls. 
2. Input these to `zotero.json` (according to the example in `zotero.json.example`)
3. Install the project dependencies: `pip install requests; pip install bibtexparser`
4. Run the tool: `python updatesources.py`. The sources are saved to `sources.bib` in the project directory.

## Known issues
The app assumes that your bibtex file is is located in the app directory and is named `sources.bib`. Feel free to modify the source to suit your needs, or better yet, make it configurable and submit a pull request.