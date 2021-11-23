from django.shortcuts import render

# Create your views here.
people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

def person_view(request, person_id):
    peep = None
    for person in people:
        if person['id'] == person_id:
            peep = person
    return render(request, 'person.html', {'person': peep, 'id': person_id})


def people_view(request):
    sorted_people = sorted(people, key=lambda x:x['age'])
    return render(request, 'people.html', {'people': sorted_people})
