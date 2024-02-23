import requests
 
def fetch_random_products():
    url = 'https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches'

    response = requests.get(url)
    res = response.json()
   
    if res["success"] and "data" in res:

        totalItems = res["data"]["totalItems"]
        products = res["data"]["data"]
        category = products[0]["category"]
       

        items = []
        for item in products:
            items.append({"title": item['title'], "price": item['price']})
        # print(items)
        
        return category, items, totalItems
    else:
        raise Exception("Failed to fetch items")


def main():
    try:
        category, items, totalItems = fetch_random_products()
        print(f"Category : {category}    totalItems : {totalItems}")
        
        for i, item in enumerate(items):
            print("*" * 70)
            print(f"{i+1}. Title : {item['title']}        Price : {item['price']}Rs.")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
