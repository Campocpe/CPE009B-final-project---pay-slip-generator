"""Payslip calculations based on the provided template."""


# ---------- Earnings ----------

def basic_pay(monthly_salary, working_days, days_worked):
    """Basic pay = Monthly salary ÷ Working days × Days worked"""
    return monthly_salary / working_days * days_worked


def daily_rate(monthly_salary, working_days):
    """Daily rate = Monthly salary ÷ Working days"""
    return monthly_salary / working_days


def hourly_rate(daily_rate_value, hours_per_day):
    """Hourly rate = Daily rate ÷ Hours per day"""
    return daily_rate_value / hours_per_day


def overtime_pay(hourly_rate_value, ot_hours, ot_multiplier):
    """Overtime pay = Hourly rate × OT hours × OT multiplier"""
    return hourly_rate_value * ot_hours * ot_multiplier


def total_allowances(allowances):
    """Allowances = Allowance 1 + Allowance 2 + ...  (list of amounts)"""
    return sum(allowances)


def gross_pay(basic, overtime, allowances, other_earnings=0.0):
    """Gross pay = Basic pay + Overtime pay + Allowances + Other earnings"""
    return basic + overtime + allowances + other_earnings


# ---------- Deductions ----------

def sss(applicable_salary, sss_rate):
    """SSS = Applicable salary × SSS contribution rate"""
    return applicable_salary * sss_rate


def philhealth(applicable_salary, philhealth_rate):
    """PhilHealth = Applicable salary × PhilHealth contribution rate"""
    return applicable_salary * philhealth_rate


def pagibig(applicable_salary, pagibig_rate):
    """Pag-IBIG = Applicable salary × Pag-IBIG contribution rate"""
    return applicable_salary * pagibig_rate


def withholding_tax(taxable_compensation, tax_rate, applicable_deduction=0.0):
    """Withholding tax = Taxable compensation × Applicable tax rate − Applicable deduction"""
    return max(taxable_compensation * tax_rate - applicable_deduction, 0.0)


def total_deductions(sss_amt, philhealth_amt, pagibig_amt, tax_amt, other_deductions=0.0):
    """Total deductions = SSS + PhilHealth + Pag-IBIG + Withholding tax + Other deductions"""
    return sss_amt + philhealth_amt + pagibig_amt + tax_amt + other_deductions


# ---------- Final ----------

def net_pay(gross, deductions):
    """Net pay = Gross pay − Total deductions"""
    return gross - deductions


# ---------- Full computation ----------

def compute_payslip(
    monthly_salary,
    working_days,
    days_worked,
    hours_per_day,
    ot_hours=0.0,
    ot_multiplier=1.25,
    allowances=None,
    other_earnings=0.0,
    applicable_salary=None,
    sss_rate=0.0,
    philhealth_rate=0.0,
    pagibig_rate=0.0,
    taxable_compensation=None,
    tax_rate=0.0,
    tax_deduction=0.0,
    other_deductions=0.0,
):
    allowances = allowances or []
    applicable_salary = monthly_salary if applicable_salary is None else applicable_salary

    d_rate = daily_rate(monthly_salary, working_days)
    h_rate = hourly_rate(d_rate, hours_per_day)

    basic = basic_pay(monthly_salary, working_days, days_worked)
    ot = overtime_pay(h_rate, ot_hours, ot_multiplier)
    allow = total_allowances(allowances)
    gross = gross_pay(basic, ot, allow, other_earnings)

    sss_amt = sss(applicable_salary, sss_rate)
    ph_amt = philhealth(applicable_salary, philhealth_rate)
    pi_amt = pagibig(applicable_salary, pagibig_rate)

    # Default taxable compensation: gross minus mandatory contributions
    if taxable_compensation is None:
        taxable_compensation = gross - (sss_amt + ph_amt + pi_amt)
    tax_amt = withholding_tax(taxable_compensation, tax_rate, tax_deduction)

    deductions = total_deductions(sss_amt, ph_amt, pi_amt, tax_amt, other_deductions)
    net = net_pay(gross, deductions)

    return {
        "daily_rate": round(d_rate, 2),
        "hourly_rate": round(h_rate, 2),
        "basic_pay": round(basic, 2),
        "overtime_pay": round(ot, 2),
        "allowances": round(allow, 2),
        "other_earnings": round(other_earnings, 2),
        "gross_pay": round(gross, 2),
        "sss": round(sss_amt, 2),
        "philhealth": round(ph_amt, 2),
        "pagibig": round(pi_amt, 2),
        "taxable_compensation": round(taxable_compensation, 2),
        "withholding_tax": round(tax_amt, 2),
        "other_deductions": round(other_deductions, 2),
        "total_deductions": round(deductions, 2),
        "net_pay": round(net, 2),
    }


if __name__ == "__main__":
    # Example with placeholder rates -- replace with your actual rates/tables
    result = compute_payslip(
        monthly_salary=25000,
        working_days=22,
        days_worked=22,
        hours_per_day=8,
        ot_hours=5,
        ot_multiplier=1.25,
        allowances=[1000, 500],
        sss_rate=0.045,
        philhealth_rate=0.025,
        pagibig_rate=0.02,
        tax_rate=0.15,
        tax_deduction=0,
    )
    for key, value in result.items():
        print(f"{key:>22}: {value:,.2f}")