from reddit_scraper import top_posts_reddit_scrapper
from time import sleep
import json
from random import randint


def main():
    top_cryptos = [
        "btc",
        "eth",
        "litecoin",
        "cardano",
        "polkadotDOT",
        "bitcoinCash",
        "stellar",
        "Chainlink",
    ]

    print("Starting...")
    scraped_data = {}
    for crypto in top_cryptos:
        print(f"scraping {crypto}")
        result = top_posts_reddit_scrapper(crypto)
        scraped_data[crypto] = result
        sleep(randint(5, 10))
        print(f"done scraping {crypto}!")

    with open("scraped_data.json", "w") as file:
        json.dump(scraped_data, file, indent=2)
        print("Saved successfully!")


if __name__ == "__main__":
    main()
