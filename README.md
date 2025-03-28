# KAIST MIC Lab
====================

Forked from fraser-lab.github.io;

See, [here](https://fraserlab.com/2020/05/03/Clone-this-website/)

# How to adjust the website

1. Change basic information in `_config.yml` file and `news.xml` file.
2. Change the logo, link, and color in `header.html` and `footer.html` files.


# How to run this website locally

Technologies this website uses:  

    Jekyll  
    Github Pages  
    Twitter Bootstrap 4.4.1

Before pushing changes, please check that they will work on your system first with the plugins included in the Gemfile using the bundler tool (results served at [localhost:4000](localhost:4000)):

    sudo gem install bundler
    bundle install
    bundle exec jekyll serve
    
To create a conda environment to locally test and host, the following should suffice:

    conda create -n jekyll -c conda-forge rb-jekyll
    conda activate jekyll
    bundle install
    bundle exec jekyll serve
