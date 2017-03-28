# Crawler
### Task #2
[[pptx]](https://www.dropbox.com/s/ay7b92bkjjng9yi/Task%202.pptx?dl=0) [[repository]](https://github.com/Andrew414/crawlertask) [[russian]](https://github.com/Andrew414/crawlertask/blob/master/README.rus.md)

### Description
You need to implement a [Web Crawler](https://en.wikipedia.org/wiki/Web_crawler) able to download wikipedia sites using multi-threading/multi-processing. Your crawler should be able to download the [small wikipedia sites](https://en.wikipedia.org/wiki/Template:Wikipedias). You need to choose one [wikipedia language edition](https://en.wikipedia.org/wiki/Wikipedia#Language_editions) and put it to `README.md` file in your local folder in repository. Please choose some edition that has more than 100 pages to make some time/performance measures possible.

Crawler should perform a multi-threaded [BFS](https://en.wikipedia.org/wiki/Breadth-first_search). It should start from the main page, parse it to find all links, drop all of them that lead outside of that local wikipedia edition and add all left links to the processing queue. All pages should then be saved to disk. Some optimizations that are valid only for wikipedia can be used, for example, all `HTTP` `GET` parameters can be dropped, all links that lead to `index.php` (e.g. [https://en.wikipedia.org/w/index.php?title=Star_Wars&action=edit](https://en.wikipedia.org/w/index.php?title=Star_Wars&action=edit)) can also be dropped, etc.

Pictures, CSS styles, templates and other resources that are not wikipedia pages should not be downloaded.

### Additional tasks
There are four additional tasks:
* Add settings to Crawler
 * Your Crawler should use some configuration passed with config file or parameters to be able to download different sites:
  * For example, some sites (like Wikipedia) have own URLs for different pages. Some another (like [fpmi.bsu.by](http://fpmi.bsu.by/)) have one URL for all pages and pages are distinguished only by `HTTP` `GET` parameters. For example, both http://fpmi.bsu.by/main.aspx?guid=18751 and http://fpmi.bsu.by/main.aspx?guid=21081 URLs point to `main.aspx` page, but the content is different because of the `guid` parameter
  * Some sites process different URLs as same URLs. For example, both http://fpmi.bsu.by/main.aspx?guid=18751 and http://fpmi.bsu.by/ru/main.aspx?guid=18751 lead to the same page, but their URLs differ
  * Some sites see the difference between UPCASE and lowcase in URLs, some do not
  * Sometimes pictures are important and should be downloaded, sometimes not
 * Your Crawler should be aware of all these possible tweaks and should provide a way of such fine-tuning of parsing engine (how to convert the URL, which parts of it should be dropped or not, which pages should not be processed, etc).
* Add performance measurement to your task
 * This is needed to compare the speed of downloading (working with network), parsing (working with CPU) and saving (working with Disk)
* Add GUI to your task
 * GUI should show the general statistics, should provide possibilities to control the download process (start/pause it, select the site), should provide the performance statistics and access to settings if you implement them
* Demonstrate the archive of the downloaded website
 * The archive should not be committed, please show it during classes

### Github repository
[Github repository](https://github.com/Andrew414/crawlertask) consists of one main [`README.md`](https://github.com/Andrew414/crawlertask/blob/master/README.md) page and fourteen personal folders. You need to fork the repository and make changes in your local folder only. All local folders contain an empty `.gitignore` file that you need to fill in with your project's temp files. Also, for this task, you need to create your own `README.md` file with the link to your own chosen wikipedia edition. The rest of the files should be your code and project files.

### Passing the task
You can choose any programming language, IDE and framework(s) for implementing this task. If some uncommon configurations or installations are required, please provide some instructions for setting up the test environment. 

You can't use libraries or frameworks that do a very similar job that task requires. For example, you can use some tool that performs general parsing (regular expressions) and can use some library that downloads files from the Web, but can't use some professional HTML parser or framework that can download the whole site by calling one function.

You should create a **pull request** from your forked repository to the task repository. Your pull request should contain **only code, project files and informational files (.gitignore, README.md)**. You should not include build results, temp files and the downloaded archive of the web site.

### Score
You can earn up to **10 points** for this task.
- **3 points** for implementing the main task
- **3 points** for finishing in time
- **1 point** for implementing *settings* subtask
- **1 point** for implementing *performance test* subtask
- **1 point** for implementing *GUI* subtask
- **1 point** for showing the full downloaded archive

### Time frames
You have four weeks (March 28 - April 24) to pass the task. The task is passed when your Pull Request gets approved. The days when your are waiting for my review are not counted. 
![ ](https://i.snag.gy/lPOzf7.jpg)

For example, if you pass the task 3 weeks after its start (April 17) and I provide my feedback on last day (April 24), you still have 1 week to fix all issues, all days after your commit and before my review are not counted.


### Good luck!