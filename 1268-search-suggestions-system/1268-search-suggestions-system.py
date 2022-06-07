class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        products.sort()
        for x in range(len(searchWord)):
            word = searchWord[:x+1]
            products = [item for item in products if item.startswith(word)]
            result.append(products[:3])
        return result