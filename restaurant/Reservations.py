from .Table import Table
import random
import uuid
class Reservations():

    def __init__(self):
        self.table_list = []
        self.bookings = {}
        for table in range(0,10):
            self.table_list.append(Table(2))


    '''
    loop over the list of tables - return a list of tables not reserved
    '''
    def get_free_tables(self):
        free_table_list = []
        for table in self.table_list:
            if table.reserved == False:
                free_table_list.append(table)
        return free_table_list

    '''check if there is more than 0
    '''
    def get_is_table_available(self):
        return len(self.get_free_tables()) > 0

    '''check if there is a table big enough for a bigger group size
    '''
    def get_free_tables_big_enough(self, group_size):
        free_tables = self.get_free_tables()
        free_tables_big_enough = []
        for table in free_tables:
            if table.seats >= group_size:
                free_tables_big_enough.append(table)
        return free_tables_big_enough

    '''same as above'''
    def get_is_table_available_for_group(self, group_size):
        free_tables = self.get_free_tables()
        large_enough_table_exists = False
        for table in free_tables:
            if table.seats >= group_size:
                large_enough_table_exists = True
        return large_enough_table_exists

    def get_num_free_tables(self):
        return len(self.get_free_tables())

    ''' returns smallest table in restaurant you can sit at '''

    def get_smallest_available_table(self, group_size):
        if self.get_is_table_available_for_group(group_size):
            tables = self.get_free_tables_big_enough(group_size)
            smallest_table = tables[0]
            for table in tables:
                if table.seats < smallest_table.seats:
                    smallest_table = table
        return smallest_table

    ''' check if table is available and make a booking '''

    def make_booking(self, group_size):
        if self.get_is_table_available_for_group(group_size):
            table_to_book = self.get_smallest_available_table(group_size)
            booking_reference = uuid.uuid4().hex[:64].upper()
            self.bookings[str(booking_reference)] = table_to_book
            table_to_book.reserved = True
            print(f"Table booked! Your booking reference is {booking_reference}")
            return {
                "response": 200,
                "booking_reference": booking_reference
            }
        else:
            print("Cannot accommodate a table for this size of a group")
            error_message = "no_tables" if self.get_num_free_tables() else "no_capacity"
            return {
                "response":400,
                "error_message": error_message
            }
    
    ''' used to initialise reservation object from database'''

    def hydrate_booking(self, group_size, booking_reference):
        table_to_book = self.get_smallest_available_table(group_size)
        self.bookings[str(booking_reference)] = table_to_book
        table_to_book.reserved = True

    def booking_exists(self, booking_reference):
        return self.bookings.__contains__(booking_reference)

    ''' cancel a booking if it exists '''

    def cancel_booking(self, booking_reference):

        if(self.booking_exists(booking_reference)):
            table_to_cancel = self.bookings[booking_reference]
            del self.bookings[booking_reference]
            table_to_cancel.reserved = False
            print("Cancelled your booking")
            return {
                "response": 200,
                "booking_reference": booking_reference
            }

        else:
            print(f"Could not find a booking for booking reference: {booking_reference}")
            return {
                "response": 404,
                "error_message": "no_booking"
            }




