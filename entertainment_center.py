import fresh_tomatoes
import media

# movie class instances to be displayed on the website in order of movie title, poster image URL, and the trailer URL
infernal_affairs = media.Movie(
    "Infernal Affairs",
    "https://resizing.flixster.com/7l_kZfq7mp6DTq5RB81ygotX1EY=/206x305/v1.bTsxMTE3NzgzOTtqOzE3Njc5OzEyMDA7ODAwOzEyMDA",
    "https://www.youtube.com/watch?v=S4R3nHkqyfM")

the_warlords = media.Movie(
    "The Warlords",
    "https://resizing.flixster.com/6YU9GhS7ycoiWKIWrf2svP9Egns=/206x305/v1.bTsxMTI5OTk3NTtqOzE3NjgwOzEyMDA7MTUzNjsyMDQ4",
    "https://www.youtube.com/watch?v=SGhfUq66ADQ")

true_legend = media.Movie(
    "True Legend",
    "http://www.impawards.com/intl/china/2010/posters/su_qier_ver6.jpg",
    "https://www.youtube.com/watch?v=gLgnZYNf84c")
enter_the_dragon = media.Movie(
    "Enter the Dragon",
    "https://images-na.ssl-images-amazon.com/images/I/51ht4NPSk0L.jpg",
    "https://www.youtube.com/watch?v=_NKUZjfTESM")

ip_man = media.Movie(
    "Ip Man",
    "http://img.moviepostershop.com/ip-man-movie-poster-2008-1010698460.jpg",
    "https://www.youtube.com/watch?v=BmkvuHpfrkk")

iron_monkey = media.Movie(
    "Iron Monkey",
    "http://img.moviepostershop.com/iron-monkey-movie-poster-1993-1010204039.jpg",
    "https://www.youtube.com/watch?v=0zM0fEsZjhM")

# list of movies to be displayed
movies = [
    infernal_affairs,
    the_warlords,
    true_legend,
    enter_the_dragon,
    ip_man,
    iron_monkey]
# fresh_tomatoes.py method to display our list on the site
fresh_tomatoes.open_movies_page(movies)
