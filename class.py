class StudentRating:
    def __init__(self, rating):
        """Initialize with a list of student ratings"""
        self.ratings = rating

    def get_ratings(self):
        """Return the current list of ratings"""
        return self.ratings

    def set_ratings(self, new_ratings):
        """Set a new list of ratings"""
        self.ratings = new_ratings

    def add_rating(self, rating):
        """Adds a new rating to the list"""
        self.ratings.append(rating)

    def max_rating(self):
        """Return the maximum rating in the group"""
        return max(self.ratings)

    def min_rating(self):
        """Return the minimum rating in the group"""
        return min(self.ratings)

    def average_rating(self):
        """Return the average rating of the group"""
        return sum(self.ratings) / len(self.ratings)

    def count_above_average(self):
        """Count students with ratings over the average"""
        avg = self.average_rating()
        return sum(1 for rating in self.ratings if rating > avg)

    def count_below_average(self):
        """Count students with ratings below the average"""
        avg = self.average_rating()
        return sum(1 for rating in self.ratings if rating < avg)

    def count_excellent(self):
        """Count students with 'excellent' ratings """
        return sum(1 for rating in self.ratings if 91 <= rating <= 100)

    def count_very_good(self):
        """Count students with 'very good' ratings """
        return sum(1 for rating in self.ratings if 71 <= rating <= 90)

    def count_good(self):
        """Count students with 'good' ratings """
        return sum(1 for rating in self.ratings if 60 <= rating <= 70)

    def count_satisfactory(self):
        """Count students with 'satisfactory' ratings """
        return sum(1 for rating in self.ratings if 0 <= rating <= 59)

    def ratings_summary(self):
        """summary of ratings in terminal, including max, min, avr, and counts in various categories"""
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

# Example usage
test_list = [77, 30, 50, 20, 40, 95, 60, 88, 92, 72, 67, 10, 47, 0]
student_rating = StudentRating(test_list)

student_rating.ratings_summary()
