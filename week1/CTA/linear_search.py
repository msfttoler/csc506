def linear_search(product_database, target_id):
    """
    Performs a linear search on a list of products to find a specific product by ID.

    Args:
        product_database (list): A list of tuples where each tuple represents a product.
        target_id (int): The ID of the product to be searched.

    Returns:
        int: The index of the found product, or -1 if not found.
    """
    for index, product in enumerate(product_database):
        if product[0] == target_id:
            return f"Product found at index {index}"
    return "Product not found"

# Example usage
product_database = [
    (1001, "Laptop", 999),
    (1002, "Phone", 699),
    (1003, "Tablet", 299)
]

target_id = int(input("Enter the product ID you want to search: "))
result = linear_search(product_database, target_id)
print(result)