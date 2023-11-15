from functools import reduce

def main():
    book_list = populate_books()
    avg_sales(book_list)
    avg_sales_by_author(book_list)

def populate_books():
    file = open("books.txt")
    return list(map(lambda l: l.replace("\n", "").split("#"), file.readlines()))

def avg_sales(books):
    file = open("report.txt", "w")
    file.writelines(map(lambda x: [x[0], int(x[1]/x[2])], books))
    
    
def avg_sales_by_author(books):
    data = map(lambda x:  [x[0], int(x[1]/x[2])],sorted(books, key=lambda x: x[1]))
    curr_sales = data[0][1]
    curr_author = data[0][0]
    for [name, sales] in data[1:]:
        if(name == curr_author):
            curr_sales = curr_sales + sales
        else:
            print(curr_author + " " + curr_sales)
            curr_sales = sales
            curr_author = name


main()