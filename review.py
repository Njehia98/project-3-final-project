# review.py
class Review:
    reviews = []

    def __init__(self, person_id, stars, comment=None):
        self.person_id = person_id
        self.stars = stars
        self.comment = comment

    @classmethod
    def create_review(cls, person_id, stars, comment=None):
        review = cls(person_id, stars, comment)
        cls.reviews.append(review)
        return review

    @classmethod
    def get_reviews_by_person_id(cls, person_id):
        return [review for review in cls.reviews if review.person_id == person_id]
