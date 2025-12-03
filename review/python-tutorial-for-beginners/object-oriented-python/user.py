"""_summary_
"""

class User:
    """_summary_
    """
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, newpassword):
        """_summary_

        Args:
            newpassword (_type_): _description_
        """
        self.password = newpassword

    def change_job_title(self, new_job_title):
        """_summary_

        Args:
            new_job_title (_type_): _description_
        """
        self.current_job_title = new_job_title
    def get_user_info(self):
        """_summary_
        """
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")
