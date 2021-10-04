from django.http import HttpResponse
from django.template import Template, Context
import datetime
import json

def hello(request):
  return HttpResponse('Hello world from Django!')

def get_time(request):
  now = datetime.datetime.now()
  string = """
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Página desde Django</title>
</head>
<body>
  La fecha y hora actual es: %s
</body>
</html>
  """ % now
  return HttpResponse(string)

def get_image(request):
  return HttpResponse('<img src="https://www.elcarrocolombiano.com/wp-content/uploads/2020/05/20200805-TESLA-ROADSTER-PORTADA.jpg">')

def get_image_url_by_id(image_id: str)->str:
  filename = 'miPrimerProyecto/data/images.json'
  file = open(filename, 'r')
  file_content = file.read()
  file.close()
  images_list = json.loads(file_content)
  for image in images_list:
    if (image['id'] == image_id):
      return image['url']

def get_image_by_id(request, image_id):
  image_url = get_image_url_by_id(image_id)
  # image_url = 'https://www.elcarrocolombiano.com/wp-content/uploads/2020/05/20200805-TESLA-ROADSTER-PORTADA.jpg'
  return HttpResponse('<img src="%s">' % image_url)

def get_age(request, birth_year):
  age = 2021 - birth_year
  template_path = 'miPrimerProyecto/templates/my-first-template.html'
  template_file = open(template_path, 'r')
  template_content = template_file.read()
  template_file.close()
  template = Template(template_content)
  template_render = template.render(Context({
    'age': age,
  }))
  return HttpResponse(template_render)

def introduction(request, name, age, city, gender):
  template_path = 'miPrimerProyecto/templates/introduction.html'
  template_file = open(template_path, 'r')
  template = Template(template_file.read())
  template_file.close()
  template = template.render(Context({
    'name': name,
    'age': age,
    'city': city,
    'gender': gender,
  }))
  return HttpResponse(template)

def get_users_list(request):
  template_path = 'miPrimerProyecto/templates/user-list.html'
  file = open(template_path, 'r')
  template = Template(file.read())
  file.close()
  users = get_all_users()
  render = template.render(Context({
    'users': users,
  }))
  return HttpResponse(render)

def get_all_users():
  filename = 'miPrimerProyecto/data/users.json'
  file = open(filename, 'r')
  users = json.loads(file.read())
  file.close()
  print(users)
  return users

def get_user_details(request, user_id):
  user = get_user_by_id(user_id)
  if (not(user)):
    return HttpResponse("<h1>User not found</h1>")

  render = render_template('miPrimerProyecto/templates/user-details.html', user)
  return HttpResponse(render)

def get_user_by_id(user_id):
  users = get_all_users()
  for user in users:
    if (user['id'] == user_id):
      return user

def render_template(template_path: str, data: dict)-> any:
  file = open(template_path, 'r')
  template = Template(file.read())
  file.close()
  return template.render(Context(data))