import wikipedia


def main():
    search_input = user_input()
    while search_input != '':
        search_summary = wikipedia.summary(search_input, auto_suggest=False)
        print(search_summary)
        page_details = get_page_details(search_input)
        print(page_details.title)
        print(page_details.url)
        print(page_details.summary)
        search_input = user_input()
    print("Thank you and have a nice day.")


def user_input():
    search_input = input("Please type what you would like to search: ")
    return search_input


def get_page_details(title, auto_suggest=False):
    page_details = wikipedia.page(title)
    return page_details


if __name__ == "__main__":
    main()
