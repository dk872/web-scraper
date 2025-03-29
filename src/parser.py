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
