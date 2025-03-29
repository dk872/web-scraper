import requests
from bs4 import BeautifulSoup


def get_page_soup(url, default=None):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')

    except requests.exceptions.RequestException as e:
        print(f"Error while loading {url}: {e}")
        return default


def parse_company_info(soup):
    def get_text_or_default(selector, default='Unknown'):
        element = soup.select_one(selector)
        return element.get_text(strip=True) if element else default

    name = get_text_or_default(
        'span.typography_display-s__pKPhT.typography_appearance-default__t8iAq.title_displayName__OBSVU')
    rating = get_text_or_default(
        'p.typography_body-l__v5JLj.typography_appearance-subtle__PYOVM')
    category = get_text_or_default(
        'a.link_internal__Eam_b.typography_appearance-action__u_Du4.link_link__jBdLV.link_notUnderlined__y4Qsc.'
        'styles_breadcrumbLink__BTE_W')
    contact = get_text_or_default(
        'a.link_internal__Eam_b.typography_body-l__v5JLj.typography_appearance-action__u_Du4.link_link__jBdLV.'
        'link_notUnderlined__y4Qsc.styles_underline__j1_xR')

    return name, rating, category, contact


def parse_reviews_and_details(soup):
    num_of_reviews = 20
    review_elements = soup.find_all('p', class_='typography_body-l__v5JLj typography_appearance-default__t8iAq')

    reviews = []
    for review in review_elements:
        review_text = review.get_text(strip=True).replace("See more", "...").replace("\n", " ").replace("\r", "")

        if review_text.lower().endswith("total"):
            continue

        reviews.append({'text': review_text})

    description = reviews[4] if len(reviews) > 4 else None
    address = reviews[5] if len(reviews) > 5 else None

    if description:
        reviews.remove(description)
    if address:
        reviews.remove(address)

    return description, address, reviews[:num_of_reviews]


def parse_data(url):
    soup = get_page_soup(url)
    if not soup:
        return None

    name, rating, category, contact = parse_company_info(soup)
    description, address, reviews = parse_reviews_and_details(soup)

    return name, rating, category, contact, description, address, reviews
