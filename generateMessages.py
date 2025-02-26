import random

# Sample users and products for the review generation
users = ["John", "Mary", "Ann", "Peter", "Alice"]
products = ["Laptop", "Phone", "Book", "Tablet", "Watch"]
reviews = ["ok", "Great", "Good", "Nice product", "TERRIBLE", "Awesome", "@#$%)", "BAD", "WORST","@#$%)23e26wedsdfgh"]
attachments = ["PICTURE", "IMAGE", "PHOTO", "GRAPHIC", "SCREENSHOT"]
buyers = {"Laptop": ["John"], "Phone": ["Mary", "Peter"], "Book": ["Ann"], "Tablet": ["John", "Alice"], "Watch": ["Alice", "Ann"]}

# Function to generate a random review message
def generate_review():
    username = random.choice(users)
    product = random.choice(products)
    review = random.choice(reviews)
    attachment = random.choice(attachments)

    # Check if the user bought the product (this is mock logic)
    if username not in buyers[product]:
        return None  # Eliminate this message as the user hasn't bought the product

    return f"{username}, {product}, {review}, {attachment}"

# Function to generate multiple reviews
def generate_reviews(num_reviews):
    reviews = []
    while len(reviews) < num_reviews:
        review = generate_review()
        if review:
            reviews.append(review)
    return reviews

# Function to write reviews to a file
def write_reviews_to_file(reviews, filename="input.txt"):
    with open(filename, "w") as file:
        for review in reviews:
            file.write(f"{review}\n")

if __name__ == "__main__":
    num_reviews = int(input("Enter the number of reviews to generate: "))
    reviews = generate_reviews(num_reviews)
    write_reviews_to_file(reviews)
    print(f"{num_reviews} reviews have been generated and written to 'input.txt'.")
