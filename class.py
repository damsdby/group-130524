class StudentRating:
    def __init__(self, rating: list[int]):
        """
        initialize StudentRating with a list of ratings

        :param rating: List of student ratings
        """
        self.ratings = rating

    def get_ratings(self) -> list[int]:
        """
        Get the list of student ratings

        :return: List of ratings
        """
        return self.ratings

    def set_ratings(self, new_ratings: list) -> None:
        """
        Set a new list of student ratings

        :param new_ratings: New list of ratings
        """
        self.ratings = new_ratings

    def add_rating(self, rating: int) -> None:
        """
        Add a new rating to the list

        :param rating: Rating to add
        """
        self.ratings.append(rating)

    def max_rating(self) -> int:
        """
        Get the maximum rating in the group

        :return: Maximum rating
        """
        return max(self.ratings)

    def min_rating(self) -> int:
        """
        Get the minimum rating in the group

        :return: Minimum rating
        """
        return min(self.ratings)

    def average_rating(self) -> float:
        """
        Calculate the average rating of the group

        :return: Average rating
        """
        return sum(self.ratings) / len(self.ratings)

    def count_above_average(self) -> int:
        """
        Count students with a rating above the average

        :return: Number of students with a rating above the average
        """
        avg = self.average_rating()
        return len([rating for rating in self.ratings if rating > avg])

    def count_below_average(self) -> int:
        """
        Count students with a rating below the average

        :return: Number of students with a rating below the average
        """
        avg = self.average_rating()
        return len([rating for rating in self.ratings if rating < avg])

    def count_excellent(self) -> int:
        """
        Count students with an excellent rating

        :return: Number of students with an excellent rating
        """
        return len([rating for rating in self.ratings if 91 <= rating <= 100])

    def count_very_good(self) -> int:
        """
        Count students with a very good rating

        :return: Number of students with a very good rating
        """
        return len([rating for rating in self.ratings if 71 <= rating <= 90])

    def count_good(self) -> int:
        """
        Count students with a good rating

        :return: Number of students with a good rating
        """
        return len([rating for rating in self.ratings if 60 <= rating <= 70])

    def count_satisfactory(self) -> int:
        """
        Count students with a satisfactory rating

        :return: Number of students with a satisfactory rating
        """
        return len([rating for rating in self.ratings if 0 <= rating <= 59])

    def ratings_summary(self) -> None:
        """
        Print a summary of student ratings etc
        :return: a summary of student ratings, including max, min, average, and category counts
        """

        print("Student Ratings:", self.ratings)
        print("Max Rating:", self.max_rating())
        print("Min Rating:", self.min_rating())
        print("Average Rating:", self.average_rating())
        print("Above Average:", self.count_above_average())
        print("Below Average:", self.count_below_average())
        print("Excellent (91-100):", self.count_excellent())
        print("Very Good (71-90):", self.count_very_good())
        print("Good (60-70):", self.count_good())
        print("Satisfactory (0-59):", self.count_satisfactory())


test_list = [77, 30, 50, 20, 40, 95, 60, 88, 92, 72, 67, 10, 47, 0]
student_rating = StudentRating(test_list)
student_rating.ratings_summary()
