## How this site was made

This site was made using [mkdocs](https://www.mkdocs.org/). Follow these steps to get mkdocs up and running in a [virtual environment](https://docs.python.org/3/library/venv.html):

    mkdir my-docs
    cd my-docs

    sudo apt-get update
    sudo apt-get install python3-virtualenv
    virtualenv --python=/usr/bin/python3.10 .venv
    python3.10 -m venv .venv
    source .venv/bin/activate
    pip install mkdocs
    pip install mkdocs-material
    pip install svglib reportlab
    pip install rlPyCairo

    # possibly also
    pip install --upgrade --force-reinstall reportlab

    mkdocs new .
    mkdocs serve
    curl 127.0.0.1:8000

## Directory layout

After running `mkdocs new .` you will have this layout:

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## livereload

By default mkdocs runs in `livereload` mode so any changes made to your markdown files under the `docs/` folder will be rendered immediately at [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Run on port 80

You can make your mkdocs site available on your local network, and on port 80. with

    mkdocs serve --dev-addr=0.0.0.0:80

