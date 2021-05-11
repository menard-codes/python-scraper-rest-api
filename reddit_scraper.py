from requests_html import HTMLSession


def top_posts_reddit_scrapper(query: str) -> list:
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Host": "www.reddit.com",
    }

    # initialize the scraper
    session = HTMLSession()
    url = f"https://www.reddit.com/search/?q={query}"
    response = session.get(url, headers=HEADERS)
    response.html.render(sleep=1, keep_page=True, scrolldown=1)

    # css selectors of target elements
    HOT_POSTS_LIST_SELECTOR = "._1oQyIsiPHYt6nx7VOmd1sz"
    TITLE_SELECTOR = "._eYtD2XCVieq6emjKBH3m"
    UPVOTES_SELECTOR = "._1rZYMD_4xY3gRcSS3p8ODO"
    DATE_POSTED_SELECTOR = "._3jOxDPIQ0KaOWpzvSQo-1s"
    POST_LINK_SELECTOR = ".SQnoC3ObvgnGjWt90zD9Z"

    # reddit scraper utils
    extract_post_info = lambda post_elem: {
        "post_title": post_elem.find(TITLE_SELECTOR, first=True).text,
        "upvotes": post_elem.find(UPVOTES_SELECTOR, first=True).text,
        "date_posted": post_elem.find(DATE_POSTED_SELECTOR, first=True).text,
        "link": list(post_elem.find(POST_LINK_SELECTOR, first=True).absolute_links)[0],
    }
    posts_snapshot_data = lambda posts_list: list(map(extract_post_info, posts_list))

    # actual scraping
    hot_posts_list = response.html.find(HOT_POSTS_LIST_SELECTOR)
    posts_data = posts_snapshot_data(hot_posts_list)

    return posts_data
