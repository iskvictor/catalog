import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','catalog.settings')

import django
django.setup()

import random
import datetime

from employee.models import InformationEmployee, Position
from faker import Faker

fakegen = Faker('ru_RU')

position_list = ['Генеральный директор', 'Директор', "Начальник отдела", "Начальник группы", "Сотрудник"]
salary = [200000,100000,50000,25000,15000]

def get_chief(list_chiefs):
    chief = InformationEmployee.objects.filter(full_name=random.choice(list_chiefs))[0]
    return chief


def populate(number=1, pos=4, list_chiefs=None):
    for i in range(number):
        fake_name = fakegen.name()
        print('fake_name',fake_name)
        start_date = datetime.date(year=2015, month=1, day=1)
        fake_employment_day = fakegen.date_between_dates(date_start=start_date, date_end=None)
        if list_chiefs != None:
            chief = get_chief(list_chiefs)
        else:
            chief = None
        print('chief',chief)
        employee_position = Position.objects.get(name=position_list[pos])

        employee = InformationEmployee.objects.get_or_create(full_name=fake_name, employment_day=fake_employment_day,
                                                             position=employee_position,chief=chief,salary=salary[pos])[0]

def main():
    print("Populating data.. Please wait.")
    populate(number=1, pos=0)
    list_chiefs = InformationEmployee.objects.filter(position__name=position_list[0])
    populate(number=15, pos=1, list_chiefs=list_chiefs)
    list_chiefs = InformationEmployee.objects.filter(position__name=position_list[1])
    populate(number=225, pos=2, list_chiefs=list_chiefs)
    list_chiefs = InformationEmployee.objects.filter(position__name=position_list[2])
    populate(number=3375, pos=3, list_chiefs=list_chiefs)
    list_chiefs = InformationEmployee.objects.filter(position__name=position_list[3])
    print('lllllllllll',len(list_chiefs))
    populate(number=5000, pos=4,list_chiefs=list_chiefs)
    print("Populating Complete")


if __name__ =='__main__':
    main()
