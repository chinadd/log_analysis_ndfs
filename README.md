# log_analysis_ndfs
udacity project for fullstack

### How to Run?

#### Setup Project:
  1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the newsdata.zip from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
  4. Unzip this file after downloading it. The file inside is called newsdata.sql.
  
#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded repository using command and ssh connect to it:
  
  ```
    $ vagrant up
  ```
  ```
    $ vagrant ssh
  ```
  2. Change directory to /vagrant .
  
#### Setting up the database and Creating Views:

  1. Load the data in [PostgreSQL](https://www.postgresql.org/) database:
  
  ```
    psql -d news -f newsdata.sql
  ```
  The database includes three tables:
  * The authors table includes information about the authors of articles.
  * The articles table includes the articles themselves.
  * The log table includes one entry for each time a user has accessed the site.
  
  2. Use `psql -d news` to connect to database.
  
  3. Create view toparticle using:
  ```
   	create view toparticle as
            select articles.slug as slug, count(log.path) as num
              from articles left join log
                 on log.path = concat('/article/', articles.slug)
                  group by slug
                    order by num desc;
  ```
  4. Create view topauthor using:
  ```
    create view topauthor as
       select authors.name as name, count(log.path) as num
          from authors left join articles
              on authors.id = articles.author
                  left join log
                    on log.path = concat('/article/', articles.slug)
                      group by name
                        order by num desc;
  ```
  5. Create vier log_error_view using:
  ```
    create view log_error_view as select date(time),
	round(100.0*sum(case log.status when '200 OK' 
	then 0 else 1 end)/count(log.status),2) as "Error" 
	from log group by date(time) order by "Error" desc;
  ```

#### Running the scripts:
  1. From the above directory ,run newsdatadb.py :
  ```
    $ python newsdatadb.py
  ```
  
