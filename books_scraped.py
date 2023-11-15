import requests
from bs4 import BeautifulSoup
import re
from word2number import w2n

def main():

    outfile = open('scraped_books.txt', "w")

    outfile.write("title\tprice\tstars\tpage\tstars_text\n")

    for num in range(1, 5):

        url = f"https://books.toscrape.com/catalogue/category/books/fiction_10/page-{num}.html"

        source_page = requests.get(url).text

        # print(source_page)

        soup = BeautifulSoup(source_page, "html.parser")

        page_num = re.findall("\d+",soup.find("li", class_="current").text)[0]

        books = soup.find_all("article", class_="product_pod")


        books = list(map(lambda x: parse_book(x, page_num), books))

        # books.map(lambda x : print(f"{x} page {}"))
        outfile.write("\n".join(books))
        outfile.write("\n")
        # write(books, f"bookpage-{num}")

    # write(source_page, "text")
    outfile.close()

def parse_book(html, page):   
    book = {
        "title": html.find("h3").find("a")["title"],
        "price": float(re.sub("[^\d+.\d+]", "", html.find("p", class_="price_color").text)),
        "stars": w2n.word_to_num(html.find("p", class_="star-rating")["class"][1]),
        "stars_text": html.find("p", class_="star-rating")["class"][1]
        }
    
    return f"{book['title']}\t{book['price']}\t{book['stars']}\t{page}\t{book['stars_text']}"

def write(content, file_name):
    file = open(f"./scraped/{file_name}.txt", mode="w")
    file.write(content)
    file.close()

def convert_word_num(word: str):
    word = word.lower()
    if(word == "one"):
        return 1
    elif(word == "two"):
        return 2
    elif(word == "three"):
        return 3
    elif(word == "four"):
        return 4
    elif(word == "five"):
        return 5

word_num_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

main()