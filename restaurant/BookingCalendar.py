import calendar
from .Reservations import Reservations

''' a lit of reservations for everyday of the month'''

class BookingCalendar:
    def __init__(self, month):
        self.initialise_month(month)

'''initialise a dictionary where the keys are the days of the month and the values are a reservation object'''

    def initialise_month(self, month):
        self.reservation_dict = {}
        self.month = calendar.monthcalendar(22, month)
        for week in self.month:
            for day in week:
                if day > 0:
                    self.reservation_dict[str(day)] = Reservations()

''' this will populate the reservation objects with data from the database'''

    def hydrate_bookings(self,booking_array):
        for entry in booking_array:
            date = entry["date"]
            group_size = entry["num_guests"]
            booking_reference = entry["booking_reference"]
            year, month, day = date.split("-")
            day = str(int(day))
            reservations_for_day  = self.reservation_dict[day]
            reservations_for_day.hydrate_booking(group_size, booking_reference)

''' make a booking for a specific day'''
    def make_booking_for_day(self, date, group_size):
        reservations_for_day  = self.reservation_dict[date]
        return reservations_for_day.make_booking(group_size)

''' cancel booking for specific day'''

    def cancel_booking_for_day(self, date, booking_reference):
        reservations_for_day = self.reservation_dict[date]
        return reservations_for_day.cancel_booking(booking_reference)

    def get_bookings_for_day(self, date):
        return self.reservation_dict[date]

    def get_num_free_seats_for_date(self, date):
        booking = self.get_bookings_for_day(date)
        return  booking.get_num_free_tables()


