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
