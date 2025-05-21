-- questions  All movies where imdb rating is not available (imagine the movie is just released)

-- 	All movies where imdb rating is available 

-- Print first 5 bollywood movies with highest rating

-- Select movies starting from second highest rating movie till next 5 movies for bollywood

-- Select all movies that are by Marvel studios and Hombale Films
-- 1. How many movies were released between 2015 and 2022
-- 2. Print the max and min movie release year
-- 3. Print a year and how many movies were released in that year starting with the latest year


select	* from moviesdb.movies;

select title,release_year from moviesdb.movies;

select * from moviesdb.movies where title like '%Avenger%';

select release_year from moviesdb.movies where title="The Godfather";

select distinct studio from moviesdb.movies where industry = 'Bollywood';

select * from moviesdb.movies where imdb_rating between 6 and 9;

select * from moviesdb.movies where imdb_rating > 9;

select * from moviesdb.movies where release_year in(2018,2019,2022);

-- select * from moviesdb.movies where imdb_rating between	1 and 10 ;

select * from moviesdb.movies;

select * from moviesdb.movies where industry = 'Bollywood' order by imdb_rating asc;

select * from moviesdb.movies order by imdb_rating asc;

select max(imdb_rating) from moviesdb.movies;

select * from moviesdb.movies order by release_year; 

select * from moviesdb.movies where release_year = 2022;

select * from moviesdb.movies where release_year > 2020;

select * from moviesdb.movies where release_year> 2020 and imdb_rating>8;

-- select * from moviesdb.movies where studio= 'Marvel studios' and 'Hombale Films'

select * from moviesdb.movies where title like '%THOR%' order by imdb_rating asc;

select * from moviesdb.movies where studio not like 'Marvel Studios';

select * from moviesdb.movies where industry not like 'Bollywood';

select * from moviesdb.movies;

select count(*) from moviesdb.movies;

select min(imdb_rating) from moviesdb.movies;

select * from moviesdb.movies where imdb_rating = 1.9;

select min(imdb_rating) from moviesdb.movies where studio = 'Marvel Studios';

-- select title from moviesdb.movies where 'Marvel Studios' = '6.8';

select * from moviesdb.movies where release_year between 2015 and 2022; 

select min(release_year), max(release_year) from moviesdb.movies;

select round(avg(imdb_rating),1) from moviesdb.movies where studio = 'Marvel Studios';

select min(release_year) from moviesdb.movies;