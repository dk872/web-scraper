from parser import parse_data


def prompt_user_for_urls():
    urls = []
    max_links = 5
    print(f"Welcome to the Web-Scraper! You can provide up to {max_links} links. \nEnter 'no' to stop.")

    while len(urls) < max_links:
        remaining_links = max_links - len(urls)
        url = input(f"Enter the link (you can enter {remaining_links} more link(s)): ")

        if url.lower() == 'no':
            break

        if url:
            urls.append(url)

    return urls


def show_parsed_data(url, parsed_data):
    char_limit = 500

    print(f"\nParsing results for {url}")

    name, rating, category, contact, description, address, reviews = parsed_data

    print(f"Company name: {name}")
    print(f"Category: {category}")
    print(f"Rating: {rating}")
    print(f"Written by the company: {description['text'][:char_limit]}" + '...')
    print(f"Contact: {contact}")
    print(f"Address: {address['text']}")

    print('-' * 21, "Reviews", '-' * 20)
    for review in reviews:
        print(f"Review: {review['text']}\n")
        print('-' * 50)
