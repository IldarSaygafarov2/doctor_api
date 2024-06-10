from django.core.management import BaseCommand
import json
from api.models import Doctor, DoctorInfo, DoctorDirection


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('test-data.json', mode='r', encoding='utf-8') as file:
            data = json.load(file)
        for line in data:
            first_name, last_name, surname = line['name'].split(' ')
            info = line['info'].split(', ')

            obj = Doctor.objects.create(
                first_name=first_name,
                last_name=last_name,
                surname=surname,
                age=line['age'],
                disease=line['disease'],
                doctor=line['doctor'],
                education=line['edication'],
                work=line['work'],
                information=line['information'],
            )
            obj.save()
            for direction in line['direction']:
                direction_obj = DoctorDirection.objects.create(
                    doctor_id=obj.pk,
                    direction=direction
                )
                direction_obj.save()

            for item in info:
                info_obj = DoctorInfo.objects.create(
                    doctor_id=obj.pk,
                    info=item
                )
                info_obj.save()
