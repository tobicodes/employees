from project import db

EmployeeDepartment = db.Table('employee_departments',
                              db.Column('id',
                                        db.Integer,
                                        primary_key=True),
                              db.Column('employee_id',
                                        db.Integer,
                                        db.ForeignKey('employees.id', ondelete="cascade")),
                              db.Column('department_id',
                                        db.Integer,
                                        db.ForeignKey('departments.id', ondelete="cascade")))


EmployeeBenefit = db.Table('employee_benefits',
                          db.Column('id', db.Integer, primary_key= True),
                          db.Column('employee_id', db.Integer, db.ForeignKey('employees.id', ondelete='cascade')),
                          db.Column('benefit_id', db.Integer, db.ForeignKey('benefits.id', ondelete='cascade')))


class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    years_at_company = db.Column(db.Integer)
    departments = db.relationship("Department",
                                  secondary=EmployeeDepartment,
                                  backref=db.backref('employees'))
    # benefits = db.relationship("Benefit",
    #                             secondary=EmployeeBenefit,
    #                             backref=db.backref('employees'))

    def __init__(self, name, years_at_company):
        self.name = name
        self.years_at_company = years_at_company


class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    all_employees = db.relationship(Employee, secondary=EmployeeDepartment, lazy="joined")


    def __init__(self, name):
        self.name = name

class Benefit(db.Model):
  __tablename__="benefits"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text)
  cost_per_employee = db.Column(db.Integer)
  employees = db.relationship('Employee', 
                              secondary = EmployeeBenefit,
                              backref=db.backref('benefits'))

  def __init__(self, name, cost_per_employee):
    self.name = name
    self.cost_per_employee = cost_per_employee

