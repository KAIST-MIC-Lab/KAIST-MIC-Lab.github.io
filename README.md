# KAIST MIC Lab

> [!Note]
> Maintained by Ph.D. student [**Myeongseok Ryu**](https://github.com/DDingR).  
> Contact me at <a href="mailto:dding_98@kaist.ac.kr">dding_98@kaist.ac.kr</a> for any questions or suggestions. 

Forked from [fraser-lab.github.io](https://fraserlab.com/2020/05/03/Clone-this-website/).

<!-- 
webpage made by Prof
https://sites.google.com/view/kaist-mic/news 
webpage (GIST)
https://mic.gist.ac.kr/prog/lectureMaster/mic/ALL/65352/list.do
-->

# How to adjust the website

> [!Note]
> Go to `_templates/` to contribute to the website.  
> Or just contact maintainer **Myeongseok Ryu**.

- Philosophy page: `./_data/philosophy.yml`
- Research page: `./research/`
- Add a new project
  - Copy the template in `./_templates/`.
  - Set `participants[].name` to each participant's member profile name. Their **Projects** section lists matching projects by start date, newest first, with a link to the project's section on the Projects page and its period underneath.
  - Member pages label projects as **[sponsor]** title, preferring `engsponsor` and `engtitle` independently and falling back to `krsponsor` and `krtitle`. The sponsor prefix is omitted when no sponsor is provided.
  - Set `state: completed` to display the end date on member pages; `state: ongoing` shows `startdate - Ongoing`. General participant labels such as `All members of the MIC Lab` do not assign projects to individuals.
- Add Member Information
  - Copy the template in `./_templates/`.
- Add a new publication
  -Copy the template in `./_templates/`.
- Faculty page: `./faculty/index.md`
- Teaching page: `./course/index.md`
- Add a news post
  - Copy the template in `./_templates/`.
  - Add names to `related_members` (for example, `related_members: [Myeongseok Ryu, Seunghun Jang]`), matching the `name` in each `_members/` profile. `memberLink.html` resolves the names automatically, and linked posts appear in each member's **News & Events**, newest first.
  - The top-level `author` / `author_link` still identifies the writer. Use `related_members: []` for posts without named individuals. Names without profiles are linked automatically once a matching member profile is added.
- News page: `./news/index.md`
- Join page: `./join/index.md`
- Contact page: `./contact/index.md`

# How to run this website locally

Technologies this website uses:  

    Jekyll  
    Github Pages  
    Twitter Bootstrap 4.4.1

Before pushing changes, please check that they will work on your system first with the plugins included in the Gemfile using the bundler tool (results served at [localhost:4000](localhost:4000)):
(For mac user; update your ruby; (https://mac.install.guide/ruby/update))
(For Windows user follow https://velog.io/@kimsoyeong/github.io-jekyll )

    sudo gem install bundler
    bundle install
    bundle exec jekyll serve
    
> [!Note]
> You may need to install old version of ruby (e.g. 3.1.4) for compatibility with Jekyll.

To create a conda environment to locally test and host, the following should suffice:

    conda create -n jekyll -c conda-forge rb-jekyll
    conda activate jekyll
    bundle install
    bundle exec jekyll serve
