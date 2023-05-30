from datetime import date

class Deposit:
    def __init__(self, amount, deposit_date):
        self.amount = amount
        self.deposit_date = deposit_date

class ROICalculator:
    def __init__(self, property_value, annual_rent, total_expenses, water_bill, electricity_bill, sewage_bill, stock_income, parking_fees,
                 interest_rate, compounded_interest_rate, deposits, tax_rate, laundry_fees, housekeeping_fees, hoa_fees, vacancy_fees,
                 repairs, mortgage, down_payment, closing_costs, miscellaneous_expenses):
        self.property_value = property_value
        self.annual_rent = annual_rent
        self.total_expenses = total_expenses
        self.water_bill = water_bill
        self.electricity_bill = electricity_bill
        self.sewage_bill = sewage_bill
        self.stock_income = stock_income
        self.parking_fees = parking_fees
        self.interest_rate = interest_rate
        self.compounded_interest_rate = compounded_interest_rate
        self.deposits = deposits
        self.tax_rate = tax_rate
        self.laundry_fees = laundry_fees
        self.housekeeping_fees = housekeeping_fees
        self.hoa_fees = hoa_fees
        self.vacancy_fees = vacancy_fees
        self.repairs = repairs
        self.mortgage = mortgage
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.miscellaneous_expenses = miscellaneous_expenses
    
    def calculate_net_income(self):
        total_expenses = self.total_expenses + self.water_bill + self.electricity_bill + self.sewage_bill + self.parking_fees + \
                         self.laundry_fees + self.housekeeping_fees + self.hoa_fees + self.vacancy_fees + self.repairs + self.mortgage
        
        net_income = self.annual_rent + self.stock_income - total_expenses
        return net_income
    
    def calculate_cash_flow(self):
        net_income = self.calculate_net_income()
        cash_flow = net_income - (self.tax_rate * net_income)
        return cash_flow
    
    def calculate_roi(self):
        cash_flow = self.calculate_cash_flow()
        down_payment_and_closing_costs = self.down_payment + self.closing_costs
        return (cash_flow / down_payment_and_closing_costs) * 100
    
    def calculate_compounded_interest(self):
        compounded_interest = 0
        today = date.today()
        
        for deposit in self.deposits:
            years_diff = (today - deposit.deposit_date).days / 365
            compounded_interest += deposit.amount * (1 + self.interest_rate) ** years_diff
        
        compounded_interest *= self.compounded_interest_rate
        return compounded_interest




property_value = 396000   
annual_rent = 14000      
total_expenses = 7000   # Total expenses (property taxes, insurance)
water_bill = 500        
electricity_bill = 300  
sewage_bill = 200       
stock_income = 500      
parking_fees = 75      
interest_rate = 0.05    # Interest rate
compounded_interest_rate = 0.1  # Compounded interest rate
deposits = [Deposit(1000, date(2020, 1, 1)), Deposit(2000, date(2021, 1, 1))]
tax_rate = 0.056        # Tax rate as a decimal
laundry_fees = 25       
housekeeping_fees = 200  
hoa_fees = 300          
vacancy_fees = 100      
repairs = 500           
mortgage = 1200         # Monthly mortgage payment
down_payment = 50000    # Down payment amount
closing_costs = 5000  
miscellaneous_expenses = 250   


roi_calculator = ROICalculator(property_value, annual_rent, total_expenses, water_bill, electricity_bill, sewage_bill, stock_income,
                               parking_fees, interest_rate, compounded_interest_rate, deposits, tax_rate, laundry_fees, housekeeping_fees,
                               hoa_fees, vacancy_fees, repairs, mortgage, down_payment, closing_costs, miscellaneous_expenses)


roi = roi_calculator.calculate_roi()
print(f"ROI: {roi:.2f}%")


compounded_interest = roi_calculator.calculate_compounded_interest()
print(f"Compounded Interest: {compounded_interest:.2f}")

