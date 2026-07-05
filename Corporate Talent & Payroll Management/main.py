def calculate_bonus(base_salary, performance_rating):
  if(performance_rating==5):
    return base_salary*0.2
  elif(performance_rating==3 or performance_rating==4):
    return base_salary*0.1
  return 0

def calculate_tax(gross_salary):
  if(gross_salary>7000):
    return gross_salary*0.15
  elif(gross_salary>=3000):
    return gross_salary*0.1
  return 0

def main_hr_app():
  print("--- corporate payroll system ---\n")
  emp_name = input("\nEnter Employee name :  ")
  base_salary = float(input("\nEnter base salary (EGP) : "))
  rating = int(input("\nEnter rating (1-5) : "))
  if (rating < 1 or rating >5 or base_salary <0):
    print("\ninvalid input please restart and check your inputs ")
    return
  bonus = calculate_bonus(base_salary, rating)
  gross_salary = base_salary + bonus
  tax = calculate_tax(gross_salary)
  net_salary = gross_salary - tax

  print("\n" + "="*40)
  print("="*40)
  print(f"• Base Salary:       {base_salary:.2f} EGP")
  print(f"• Earned Bonus:      {bonus:.2f} EGP")
  print(f"• Tax Deductions:    {tax:.2f} EGP")
  print(f"📄 PAYROLL STATEMENT FOR: {emp_name}")
  print("-" * 40)
  print(f"💰 NET PAYABLE CASH: {net_salary:.2f} EGP")
  print("="*40)

main_hr_app()