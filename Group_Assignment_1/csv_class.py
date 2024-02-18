from dataclasses import dataclass

@dataclass
class Customer:
    custid:int
    firstName:str
    lastName:str
    company:str
    address:str
    city:str
    state:str
    zipCode:str

    def custNameAddress(self):
        """
        Returns an f-string with customer information.

        Returns
        -------
        str
            Customer name and address.

        """
        fullAddress = f"{self.state}" + ", " + f"{self.city}" + ", " + f"{self.address}" + ", " + f"{self.zipCode}"
        fullName = f"{self.firstName}" + " " + f"{self.lastName}"
        if self.company == "":
            return f"{fullName}\n{fullAddress}."
        else:
            return f"{fullName}\n{fullAddress}\n{self.company}."
