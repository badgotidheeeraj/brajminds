from django_unicorn.components import UnicornView
from minds.models import send_data,dynamic_data

class HomeView(UnicornView):
    FullName=""
    Email=""
    PhoneNumber=""
    Name=""
    def save_book(self):
        success_message = None
        if self.FullName and self.Email and self.PhoneNumber and self.Name:
            book = send_data(FullName=self.FullName,Email=self.Email,PhoneNumber=self.PhoneNumber,Name=self.Name)
            if book:
                book.save()
                success_message = "Book saved successfully."
                self.reset()
            else:
                success_message = "Error creating book object."
        print('============>>',success_message)
        return success_message
    
