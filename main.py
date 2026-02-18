from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    print(get_mask_card_number(98471984790187240198759))
    print(get_mask_account(98471984790187240198759))

